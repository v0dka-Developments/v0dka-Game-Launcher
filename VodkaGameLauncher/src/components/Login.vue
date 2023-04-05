
<template>
  <Toast />
  <div class="grid fade-out">
    <div class="col-fixed logo fillme" style="width:500px"></div>
    <div class="col">
      <div class="grid fade-in">
        <div class="col-12 text-center login-form">
          <div class="grid">
            <div class="col-12"><h1>Vodka Game Launcher</h1></div>
            <div class="col-12">
              <div class="grid">
                <div class="col-3"></div>
                <div class="col-6 ">
                  <div class="card flex justify-content-center center_login">
                    <form @submit="onSubmit" class="flex flex-column gap-2" style="width: 100%;">
                      <span class="p-float-label"> 
                        <InputText id="username" v-model="username" type="text" :class="{ 'p-invalid': usernameError }" aria-describedby="username-error" style="width: 100%;" autocomplete="off"/>
                        <label for="username">Username</label>
                      </span>
                      <small class="p-error" id="username-error">{{ usernameError || '&nbsp;' }}</small>

                      <span class="p-float-label"> 
                        <InputText id="password" type="password" v-model="password" :class="{ 'p-invalid': passwordError }" aria-describedby="password-error" style="width: 100%;" />
                        <label for="password">Password</label>
                      </span>
                      <small class="p-error" id="password-error">{{ passwordError || '&nbsp;' }}</small>

                      
                      <Button type="submit" severity="success" label="Submit" />
                    </form>
                  </div>
                </div>
                <div class="col-3"></div>
              </div>
            </div>
          </div>
          <div class="grid">
            <div class="col-12 bottom">Developed by vodka 😀 ❤️</div>
          </div>
        </div>  
      </div>
    </div>
  </div>
</template>


<script setup>
   import { onMounted } from 'vue';
  import router from '../router';

  import { useToast } from 'primevue/usetoast';
  import { useField, useForm } from 'vee-validate';
  import { invoke } from "@tauri-apps/api/tauri";

  import { getClient, Body, ResponseType } from '@tauri-apps/api/http';

  const { handleSubmit, resetForm } = useForm();
  const { value: username, errorMessage: usernameErrorMessage } = useField('username', validateUsername);
  const { value: password, errorMessage: passwordErrorMessage } = useField('password', validatePassword);
  const toast = useToast();
  const domain = "http://127.0.0.1:8090/"
  const body = document.querySelector('body');



  
  function validateUsername(value) {
    if (!value) {
      return 'Username is required.';
    }
    return true;
  }

  function validatePassword(value) {
    if (!value) {
      return 'Password is required.';
    }
    return true;
  }

  const onSubmit = handleSubmit(async (values) => {
  if (values.username && values.username.length > 0 && values.password && values.password.length > 0) {
    try{
    const client = await getClient();
    console.log(domain+'userlogin');
    const response = await client.post(domain+'userlogin', {
      headers: {
        'Content-Type': 'application/json'
      },
      type: "Json",
      payload: ({username: values.username,password:values.password}),
      responseType: ResponseType.Json,
    });
    console.log(response.data.success);

    if(response.data.success){
        toast.add({ severity: 'success', summary: 'Login', detail: `You have successfully been logged in `, life: 3000 });
        setTimeout(() => {
            document.querySelector('.fade-out').classList.add('active');
            }, 2000);
            setTimeout(() => {
              router.push({ name: 'loggedin' });
            }, 3000);
    }else{
      toast.add({ severity: 'error', summary: 'Login', detail: response.data.message, life: 3000 });
    }
  }catch{
    toast.add({ severity: 'error', summary: 'Login', detail: "unable to contact login server", life: 3000 });
  }

  }
});
  
  onMounted(() => {
    setTimeout(() => {
      document.querySelector('.fade-in').classList.add('active');
      /* enable this code when going live so people cant middle click */
      //const link = document.querySelector('a');

     // link.addEventListener('auxclick', (event) => {
     //   if (event.button === 1) { // Check if middle mouse button was clicked
     //     event.preventDefault(); // Prevent default action of opening a new window   
     //   }
    //  });
    }, 1000);
  });

  </script>

<style>
@import 'primeflex/primeflex.css';
@import "primevue/resources/themes/lara-light-indigo/theme.css";    



.fillme {
    display: flex;
    height: 100vh; /* Set the height to fill the viewport height */
  }

.logo {
  background-image: url("../assets/logo.png");
  background-repeat: no-repeat;
  background-size: auto;
  overflow:hidden;
}
.container{
  position: relative;
}

  .bottom {
   
    margin-top: 9vh;
    text-align: center;
  }
  .p-float-label > label {
    color: rgb(0, 0, 0) !important;
  }

  .center_login {
  display: flex;
  height: 70vh;
  align-items: center;
}
.fade-in {
  opacity: 0;
  transition: opacity 1s ease-in-out;
}

.fade-in.active {
  opacity: 1;
}

.fade-out {
  opacity: 1;
  transition: opacity 1s ease-in-out;
}

.fade-out.active {
  opacity: 0;
}

</style>