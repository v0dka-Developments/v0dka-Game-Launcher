import os
import hashlib
import json
def generate_directory_structure(directory_path, parent_path=""):
    directory_structure = {}
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        if os.path.isfile(item_path):
            with open(item_path, 'rb') as f:
                md5_hash = hashlib.md5(f.read()).hexdigest()
            if parent_path:
                directory_structure[parent_path+"/"+item] = md5_hash
            else:
                directory_structure[item] = md5_hash
        elif os.path.isdir(item_path):
            subdirectory_structure = generate_directory_structure(item_path, item)
            for key, value in subdirectory_structure.items():
                if parent_path:
                    directory_structure[parent_path+"/"+key] = value
                else:
                    directory_structure[key] = value
    return directory_structure
def compare_json(user_directory, manifest):
    try:
        obj1 = json.loads(user_directory)
        obj2 = json.loads(manifest)
    except json.JSONDecodeError as e:
        return {"error": str(e)}
    diff = {}
    for key, value in obj1.items():
        found = False
        no_match = True
        unmatched_key = None
        for key2, value2 in obj2.items():
            if key == key2:
                found = True
                if value == value2:
                    no_match = False
                else:
                    unmatched_key = value2
                break
        if not found:
            diff[key] = {"status": "not found"}
        elif no_match:
            diff[key] = {"status": "hash does not match"}
    return diff
res = json.dumps(generate_directory_structure("D:\\ffs\\tauri\\PythonWebServer\\Version\\v1-13-12"))
url_stuff = '{"test/bin/im_bin.txt": "a8f5f167f44f4964e6c998dee827110c","test/game_directory/test.txt": "c4ca4238a0b923820dcc509a6f75849b","test/game_directory/test2.txt": "c81e728d9d4c2f636f067f89cc14862c","test/game_directory/test3.txt": "eccbc87e4b5ce2fe28308fd9f2a7baf3","test/super_dooper.txt": "3069a5d8e643bd21b3b3318efc71433a"}'
print(compare_json(res,url_stuff))
