from flask import Flask, request, send_file, render_template, redirect, url_for, session, flash, Response
from werkzeug.utils import secure_filename
import os
from pathlib import Path
import zipfile
import hashlib
import json
import datetime
import config
import re
import uuid
import tempfile




current_directory = os.getcwd()
UPLOAD_FOLDER = current_directory + "/" + config.Zip_Upload_Folder + "/"
VERSION_FOLDER = current_directory + "/" + config.Versions + "/"
VERSION_FILE = current_directory +"/"+config.Version_Json
ALLOWED_EXTENSIONS = {'zip'}
ALLOWED_EXTENSIONS_IMAGES = {'png'}

app = Flask(__name__)
app.static_folder = 'static'
app.secret_key = config.AppSecretKey
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# because i have no fuck space on my ssd :|
tempfile.tempdir = UPLOAD_FOLDER

######################################################################

#                          FUNCTIONS                                 #
#   bunch of functions to help with tasks thoughout the app          #


######################################################################


# regular expression to make sure version is correct
def is_valid_version(version):
    VERSION_REGEX = r'^v\d+-\d+-\d+$'
    return bool(re.match(VERSION_REGEX, version))

# function for checking allowed file types for image upload in admin panel
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# function for checking allowed file types for upload in admin panel
def allowed_file_images(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS_IMAGES
# function for us to find the most recent version by folder name
def get_latest_version(directory):
    versions = []
    for filename in os.listdir(directory):
        if filename.startswith('v'):
            # extract the version number from the filename
            version_parts = filename[1:].split('-')
            version_number = tuple(int(part) for part in version_parts)
            versions.append(version_number)
    if versions:
        # sort the versions and return the highest one
        return 'v' + '-'.join(str(part) for part in max(versions))
    else:
        # no versions found
        return "no version"
# list all the versions this is used to populate the version selector in the admin panel
def get_all_versions():
    versions = []

    for folder in os.listdir(VERSION_FOLDER):
        if os.path.isdir(os.path.join(VERSION_FOLDER, folder)):
            versions.append(folder)

    return versions
## gets the current live version from the json file in the root directory
def get_current_live_version():
    with open(VERSION_FILE, "r") as f:
        data = json.load(f)

    return(data)
## updates the current live version in the json file
def set_current_live_version(new_version):

    data = {"version": new_version}

    with open("version.json", "w") as f:
        json.dump(data, f)

    return "updated to version "+new_version


# used to generate the directory_listings.json
def generate_directory_structure(directory_path, parent_path=""):
    directory_structure = {}
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        if os.path.isfile(item_path):
            # calculate md5 hash of file
            with open(item_path, 'rb') as f:
                md5_hash = hashlib.md5(f.read()).hexdigest()
            # add file to directory structure
            if parent_path:
                directory_structure[parent_path+"/"+item] = md5_hash
            else:
                directory_structure[item] = md5_hash
        elif os.path.isdir(item_path):
            # recursively generate directory structure
            subdirectory_structure = generate_directory_structure(item_path, item)
            # add subdirectory files to directory structure
            for key, value in subdirectory_structure.items():
                if parent_path:
                    directory_structure[parent_path+"/"+key] = value
                else:
                    directory_structure[key] = value
    return directory_structure


def setup_version(zip_file_path, version):
    # create the path for the version folder
    pattern = r'^v\d+-\d+-\d+$'  # regex pattern to match format vX-Y-Z
    if re.match(pattern, version):
        version_folder_path = VERSION_FOLDER + version
        # check if the version folder already exists
        if os.path.exists(version_folder_path):
            res = (f"Error: This '{version}' already exists please select another.")
            return res
        # create the new version folder
        os.makedirs(version_folder_path)
        # extract the zip file to the version folder
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(version_folder_path)

        # generate directory structure and save to JSON file
        json_data = generate_directory_structure(version_folder_path)
        if not json_data:
            # remove empty version directory
            os.rmdir(version_folder_path)
            res = "Error: version directory is empty."
        else:
            # save directory structure to JSON file
            json_path = os.path.join(version_folder_path, 'directory_structure.json')
            with open(json_path, 'w') as f:
                json.dump(json_data, f, indent=4)
            res = f"Zip file uploaded, extracted to version folder '{version}' and json file built successfully."
        return res
    else:
        res = "Invalid version type, version follows syntax v1-0-0"
        return res


#####################################################################################




#                                   APP ROUTES                                      #
#   handles all the requests to the actual web app                                  #



#####################################################################################


#main login page http://domain/control_me
@app.route("/control_me",  methods=['GET', 'POST'])
def control_me():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
    return render_template('login.html', error=error)

#dashboard
@app.route("/dashboard")
def dashboard():
    if 'logged_in' in session and session['logged_in']:
        return render_template("dashboard.html")
    else:
        return redirect(url_for('control_me'))

#upload build page
@app.route("/upload_build", methods=['GET', 'POST'])
def upload_build():
    if 'logged_in' in session and session['logged_in']:
        if request.method == "POST":
            if 'file' not in request.files:
                flash("failed select file please")
                return redirect(request.url)
            file = request.files['file']
            if file.filename == '':
                flash("failed select file please")
                return redirect(request.url)
            if file and allowed_file(file.filename):
                user_version_request = "v1-0-0"
                if request.form.get('major') and request.form.get('minor') and request.form.get('major'):
                    major = request.form.get('major')
                    minor = request.form.get('minor')
                    micro = request.form.get('micro')
                    user_version_request = "v"+major+"-"+minor+"-"+micro


                current_time = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
                filename = current_time + '_' + file.filename
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                # alert the user to success...
                flash(setup_version(UPLOAD_FOLDER+filename, user_version_request))
                return redirect(request.url)
            else:
                flash("sorry this file could not be allowed for upload")
                return redirect(request.url)

        else:
            version_directory = Path(current_directory + "/" + config.Versions)
            current_version = get_latest_version(version_directory)



            if current_version == "no version":
                return render_template("upload_build.html", show_no_version=True)
            else:
                version_parts = current_version.split('-')

                major_version = int(version_parts[0][1:])
                minor_version = int(version_parts[1])
                micro_version = int(version_parts[2])
                print(get_latest_version(version_directory))
                return render_template("upload_build.html", show_version=True, version_number=current_version,major=major_version,minor=minor_version,micro=micro_version)
    else:
        return redirect(url_for('control_me'))

# set current live version
@app.route("/set_version", methods=['GET', 'POST'])
def set_version():
    if 'logged_in' in session and session['logged_in']:
        if request.method == "POST":
            if request.form.get('live_version'):
                user_version_request = request.form.get('live_version')
                set_current_live_version(user_version_request)
        return render_template("set_version.html",versions=get_all_versions(),current_version=get_current_live_version())
    else:
        return redirect(url_for('control_me'))

@app.route("/logout")
def logout():
    session.pop('logged_in', None)
    return redirect(url_for("control_me"))


#
#
#
#
#   public download route
#   you can wrap this in auth but for this i have not
#   server will fetch file on behalf of user and not expose the direct file path
#   and stream it in chunks currently of 256mb which is overkill
#   if you was using this in production drop down to 1-5mb otherwise goodbye ram...
#
#
#
@app.route('/download', methods=['GET'])
def download_file():
    if request.args.get('version') and request.args.get('filename'):
        version = request.args.get('version')
        filename = request.args.get('filename')
        current_version = get_current_live_version()
        if not is_valid_version(version):
            return 'Error: Invalid version format'
        if not version or not filename:
            return 'Error: version and filename parameters are required'
        if version != current_version['version']:
            return 'Error: You are requesting a version which is not available'
        filename = os.path.normpath(filename)
        directory = os.path.join(VERSION_FOLDER, version)
        file_path = os.path.join(directory, filename)
        if not os.path.exists(file_path):
            return 'File Must be removed'

        def generate():
            with open(file_path, 'rb') as f:
                while True:
                    chunk = f.read(256*1024*1024) # read 256MB at a time note you might wanna change this in production
                    if not chunk:
                        break
                    yield chunk

        return Response(generate(), headers={
            'Content-Disposition': f'attachment; filename={filename}'
        })

    else:
        return "Error: invalid paramaters"


## returns the current live version
@app.route('/request_version')
def request_version():
    return get_current_live_version()

# returns the "manifest" file which is the directory_structure.json
@app.route('/request_version_details', methods=['GET'])
def request_version_details():
    if request.args.get('version'):
        current_version = get_current_live_version()
        if current_version['version'] == request.args.get('version'):

            version_details = Path(VERSION_FOLDER + "/" + current_version['version']+ "/directory_structure.json")

            if not version_details.is_file():
                return "Error: invalid json file"#
            else:
                with open(version_details, "r") as f:
                    data = json.load(f)

                return (data)


        else:
            return "Error: Invalid version"
    else:
        return "Error: give me a version"

@app.route('/store_feed',methods=['GET','POST'])
def store_feed():
    if 'logged_in' in session and session['logged_in']:
        options = ""
        if os.path.exists('store.json'):
            with open('store.json', 'r') as f:
                options = json.load(f)
        if request.method == "POST":
          if request.form.get("req_type2") and request.form.get("req_type2") == "create2":
              if 'image' not in request.files:

                  flash("failed select an image file please")
                  return render_template("store_feed.html",options=options)
              file = request.files['image']
              if file.filename == '':

                  flash("failed to select file please try again")
                  return render_template("store_feed.html",options=options)
              if file and allowed_file_images(file.filename):

                  file_extension = file.filename.split('.')[-1]
                  new_filename = secure_filename(file.filename).replace('.png', '', 1) + "-" + str(uuid.uuid4()) + '.' + file_extension
                  file.filename = new_filename
                  # save the file to the static folder
                  file.save(os.path.join(current_directory+"/static", new_filename))

                  if not os.path.exists('store.json'):
                      # Create an empty dictionary and write it to the news.json file
                      with open('store.json', 'w') as f:
                          json.dump({}, f)

                  # Load the existing JSON data from the file
                  with open('store.json', 'r') as f:
                      store_data = json.load(f)

                  # Add the new news item to the dictionary
                  store_item = {
                      'title': request.form['title'],
                      'description': request.form['content'],
                      'image': new_filename
                  }
                  store_data[len(store_data) + 1] = store_item

                  # Write the updated JSON data back to the file
                  with open('store.json', 'w') as f:
                      json.dump(store_data, f)

                  flash("file succesfully uploaded and content successfully added")
                  return render_template("store_feed.html",options=store_data)

          if request.form.get("req_type2") and request.form.get("req_type2") == "delete":
            if options != "":
                key = request.form['delete_store']
                with open('store.json') as f:
                    data = json.load(f)
                if key in data:
                    del data[key]
                    with open('store.json', 'w') as f:
                        json.dump(data, f)
                    message = f"News item {key} has been deleted."
                else:
                    message = f"News item {key} not found."

                if os.path.exists('store.json'):
                    with open('store.json', 'r') as f:
                        options = json.load(f)
                flash(message)
                return render_template('store_feed.html',options=options)
          if request.form.get("req_type2") and request.form.get("req_type2") == "modify":
              for key in options.keys():
                  if key == request.form.get("modify_store"):
                      if request.form.get("title") and request.form.get("content"):

                          # Update the JSON for the key with the new title and content
                          options[key]["title"] = request.form.get("title")
                          options[key]["content"] = request.form.get("description")
                          # Write the updated JSON to a file
                          with open('store.json', 'w') as f:
                              json.dump(options, f)
                          return redirect(url_for('store_feed'))
                      else:

                          return redirect(url_for('store_feed', modify="start", title=options[key]["title"], content=options[key]["description"]))

        return render_template("store_feed.html",options=options)
    else:
        return redirect(url_for('control_me'))
@app.route('/request_store',methods=['GET'])
def request_store():
    # Check if the news.json file exists
    if not os.path.exists('store.json'):
        return Response('No news', mimetype='text/plain')

    # Load the existing JSON data from the file
    with open('store.json', 'r') as f:
        news_data = json.load(f)

    # Get the last 5 news items
    last_five_items = list(news_data.values())[-5:]

    # Convert the last 5 news items to a JSON string
    json_str = json.dumps(last_five_items)

    # Return the JSON string as a Flask response
    return Response(json_str, mimetype='application/json')


@app.route('/add_store',methods=['GET','POST'])
def add_store():
    if 'logged_in' in session and session['logged_in']:
        if not os.path.exists('store.json'):
            # Create an empty dictionary and write it to the news.json file
            with open('store.json', 'w') as f:
                json.dump({}, f)

        # Load the existing JSON data from the file
        with open('store.json', 'r') as f:
            store_data = json.load(f)

        # Add the new news item to the dictionary
        store_item = {
            'title': request.form['title'],
            'description': request.form['description'],
            'image': request.form['image']
        }
        store_data[len(store_data)+1] = store_item

        # Write the updated JSON data back to the file
        with open('storer.json', 'w') as f:
            json.dump(store_data, f)
    else:
        return redirect(url_for('control_me'))
### example news for the app.. need to create view for this tomorrow...
@app.route('/add_news',methods=['GET','POST'])
def add_news():
    if 'logged_in' in session and session['logged_in']:
        if not os.path.exists('news.json'):
            # Create an empty dictionary and write it to the news.json file
            with open('news.json', 'w') as f:
                json.dump({}, f)

        # Load the existing JSON data from the file
        with open('news.json', 'r') as f:
            news_data = json.load(f)

        # Add the new news item to the dictionary
        news_item = {
            'title': request.form['title'],
            'description': request.form['description'],
            'image': request.form['image']
        }
        news_data[len(news_data)+1] = news_item

        # Write the updated JSON data back to the file
        with open('news.json', 'w') as f:
            json.dump(news_data, f)
    else:
        return redirect(url_for('control_me'))

@app.route('/request_news',methods=['GET'])
def request_news():
    # Check if the news.json file exists
    if not os.path.exists('news.json'):
        return Response('No news', mimetype='text/plain')

    # Load the existing JSON data from the file
    with open('news.json', 'r') as f:
        news_data = json.load(f)

    # Get the last 5 news items
    last_five_items = list(news_data.values())[-5:]

    # Convert the last 5 news items to a JSON string
    json_str = json.dumps(last_five_items)

    # Return the JSON string as a Flask response
    return Response(json_str, mimetype='application/json')



@app.route('/news_feed',methods=['GET','POST'])
def news_feed():
    if 'logged_in' in session and session['logged_in']:
        options = ""
        if os.path.exists('news.json'):
            with open('news.json', 'r') as f:
                options = json.load(f)
        if request.method == "POST":
          if request.form.get("req_type") and request.form.get("req_type") == "create":
              if 'image' not in request.files:

                  flash("failed select an image file please")
                  return render_template("news_feed.html",options=options)
              file = request.files['image']
              if file.filename == '':

                  flash("failed to select file please try again")
                  return render_template("news_feed.html",options=options)
              if file and allowed_file_images(file.filename):

                  file_extension = file.filename.split('.')[-1]
                  new_filename = secure_filename(file.filename).replace('.png', '', 1) + "-" + str(uuid.uuid4()) + '.' + file_extension
                  file.filename = new_filename
                  # save the file to the static folder
                  file.save(os.path.join(current_directory+"/static", new_filename))

                  if not os.path.exists('news.json'):
                      # Create an empty dictionary and write it to the news.json file
                      with open('news.json', 'w') as f:
                          json.dump({}, f)

                  # Load the existing JSON data from the file
                  with open('news.json', 'r') as f:
                      news_data = json.load(f)

                  # Add the new news item to the dictionary
                  news_item = {
                      'title': request.form['title'],
                      'description': request.form['content'],
                      'image': new_filename
                  }
                  news_data[len(news_data) + 1] = news_item

                  # Write the updated JSON data back to the file
                  with open('news.json', 'w') as f:
                      json.dump(news_data, f)

                  flash("file succesfully uploaded and content successfully added")
                  return render_template("news_feed.html",options=news_data)

          if request.form.get("req_type") and request.form.get("req_type") == "delete":
            if options != "":
                key = request.form['delete_news']
                with open('news.json') as f:
                    data = json.load(f)
                if key in data:
                    del data[key]
                    with open('news.json', 'w') as f:
                        json.dump(data, f)
                    message = f"News item {key} has been deleted."
                else:
                    message = f"News item {key} not found."

                if os.path.exists('news.json'):
                    with open('news.json', 'r') as f:
                        options = json.load(f)
                flash(message)
                return render_template('news_feed.html',options=options)
          if request.form.get("req_type") and request.form.get("req_type") == "modify":
              for key in options.keys():
                  if key == request.form.get("modify_news"):
                      if request.form.get("title") and request.form.get("content"):

                          # Update the JSON for the key with the new title and content
                          options[key]["title"] = request.form.get("title")
                          options[key]["content"] = request.form.get("description")
                          # Write the updated JSON to a file
                          with open('news.json', 'w') as f:
                              json.dump(options, f)
                          return redirect(url_for('news_feed'))
                      else:

                          return redirect(url_for('news_feed', modify="start", title=options[key]["title"], content=options[key]["description"]))

        return render_template("news_feed.html",options=options)
    else:
        return redirect(url_for('control_me'))


## login this should really be to another service but it is an example
## built into this package for a demo
@app.route("/userlogin", methods=['POST'])
def userlogin():
    if request.is_json:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        if username and password:
            if username == "admin" and password == "pass":
                return {"success": True}
            else:
                return {"success": False, "message": "Invalid username or password"}
        else:
            return {"success": False, "message": "Missing username or password"}
    else:
        return {"success": False, "message": "Request must contain JSON data"}





if __name__ == "__main__":

    start_message = '''
        \x1b[6;30;42m############################################################################\x1b[0m
        \x1b[6;30;42m#                       V0dka Public Game Manager                          #\x1b[0m
        \x1b[6;30;42m#                                Version 1.0.0                             #\x1b[0m
        \x1b[6;30;42m############################################################################\x1b[0m
    '''

    print(start_message)
    build_exist = False
    version_exist = False
    version_file = False
    news_exist = False


    build_directory = Path(current_directory + "/" + config.Zip_Upload_Folder)
    version_directory = Path(current_directory + "/" + config.Versions)
    version_file = Path(current_directory + "/"+config.Version_Json)
    news_file = Path(current_directory + "/news.json")
    ## inital launch we make sure files exist that we need...
    if not version_file.is_file():
        print('\033[91m' + "Making Version File" + '\033[0m')
        data = {"version": "none"}
        with open(version_file, "w") as f:
            json.dump(data, f)

    if not build_directory.is_dir():
        print('\033[91m' + "build directory does not exist creating directory" + '\033[0m')
        os.mkdir(build_directory)
        build_exist = True

    else:
        print("build directory exists")
        build_exist = True

    if not version_directory.is_dir():
        print('\033[91m' + "Version directory does not exist creating directory" + '\033[0m')
        os.mkdir(version_directory)
        version_exist = True
    else:
        print("version directory exists")
        version_exist = True
    if not news_file.is_file():
        print('\033[91m' + "news file does not exist making it now" + '\033[0m')

        data = {}
        with open(news_file, "w") as f:
            json.dump(data, f)
    else:
        print("news file exists")
        news_exist = True


    if version_exist and build_directory:
        print("success starting")
        app.run(host=config.IP, port=config.Port, debug=config.Debug)
    else:
        print("something went wrong")