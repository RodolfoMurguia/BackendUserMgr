<template lang = 'html'>
    <div class = 'container'>
        <div class = 'row'>
            <div class = 'col text-left'>
                <img src="../assets/userManagement.png"  alt="" height="100px" width="100px">
                <h1>Administracion de usuarios</h1>

     
                    <form @submit.prevent="loginUser">

                        <div class= "form-group row">
                            <label for="Title" class="col-sm-2 col-form-label" >Nombre de usuario: </label>
                            <div class= "col-sm-6">
                                <input type="text"  placeholder="usuario: " name="username" value="" class="form-control" v-model="userName">
                            </div>
                        </div>

                        <div class= "form-group row">
                            <label for="Title" class="col-sm-2 col-form-label" >Contraseña: </label>
                            <div class= "col-sm-6">
                                <input type="password"  placeholder="Contraseña: " name="password" value="" class="form-control" v-model="password">
                            </div>
                        </div>

                         <b-button type="submit" size="lg">Iniciar Sesion</b-button>
                    </form>

            </div>
        </div>
    </div>
    
</template>

<script>

import axios from 'axios';
import Swal from 'sweetalert2'
const path = "http://127.0.0.1:8000/auth/"

export default {

    data(){
        return{
            userName: '',
            password: '',
            userToken: null
        }
    },methods:{

        //Implementacion de Login
        loginUser(){
            axios.post(path ,{
                username: this.userName,
                password: this.password
            
            }).then(res => {
                //almaceno token
                this.userToken = res.data.token;

                //Lo enviamos a LS
                localStorage.setItem('user-token', this.userToken);

                //Alerta a user
                Swal.fire({
                          icon: 'success',
                          title: 'Excelente!',
                          text: 'Sesion iniciada correctamente, redirigiendo...'})

                window.location.href = "http://localhost:8080/list_users/";
            
            }).catch(err => {

                //Notifico Error de sesion
                console.log(err)
                
                //Alerta a user
                Swal.fire({icon: 'error',
                          title: 'Oops...',
                          text: 'No se pudo iniciar sesion, por favor, valide sus credenciales'})

                //Removemos el token de LS (por cualquier cosa)
                localStorage.removeItem('user-token', this.userToken);
            })
        }

    },created(){
        
    }

}
</script>

<style scoped>

</style>