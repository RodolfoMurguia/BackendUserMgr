<template lang = 'html'>
    <div class = 'container'>
        <div class = 'row'>
            <div class = 'col text-left'>

                <img src="../assets/add-user.png" alt="create user" height="100px" width="100px">
                <h1>Editar usuario</h1>

                    <form @submit="">

                        <div class= "form-group row">
                            <label for="Title" class="col-sm-2 col-form-label">Nombre de usuario: </label>
                            <div class= "col-sm-6">
                                <input type="text"  placeholder="usuario: " name="username" value="" class="form-control" >
                            </div>
                        </div>

                        <div class= "form-group row">
                            <label for="Title" class="col-sm-2 col-form-label">Nombre: </label>
                            <div class= "col-sm-6">
                                <input type="text"  placeholder="Nombre: " name="firstname" value="" class="form-control" >
                            </div>
                        </div>

                        <div class= "form-group row">
                            <label for="Title" class="col-sm-2 col-form-label">Apellidos: </label>
                            <div class= "col-sm-6">
                                <input type="text"  placeholder="Apellidos: " name="lastname" value="" class="form-control" >
                            </div>
                        </div>

                        <div class= "form-group row">
                            <label for="Title" class="col-sm-2 col-form-label">Correo electronico: </label>
                            <div class= "col-sm-6">
                                <input type="email"  placeholder="Correo electronico: " name="email" value="" class="form-control" >
                            </div>
                        </div>

                        <div class= "form-group row">
                            <label for="Title" class="col-sm-2 col-form-label">Contraseña: </label>
                            <div class= "col-sm-6">
                                <input type="password"  placeholder="Contraseña: " name="password" value="" class="form-control" >
                            </div>
                        </div>

                        <div class="rows">
                            <div class="col text-center">

                                <b-button size='lg' type="submit" variant="primary">Guardar Datos</b-button>
                                <b-button size='lg' type="submit" class="btn-large-space" :to="{ name: 'Main' }">Volver a inicio</b-button>

                            </div>
                        </div>
                    </form>
            </div>
        </div>
    </div>
    
</template>

<script>
import axios from 'axios';
import swal from 'sweetalert'

//var userId = this.$route.params.userId;

export default {

    data(){
        return{
            userId: this.$route.params.userId,
            form:{
                email:null,
                reg: /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,24}))$/ 
            }   
            
        }
    },
    methods: {
        
        //Genero el post para 
        onSubmit(evt){
           evt.preventDefault;

           userdata = {
                "user": this.form.user,
                "password": this.form.password,
                "email": this.form.email,
                "firstName": this.form.firstName,
                "lastName": this.form.lastName,
                "isAdmin": false
           }

           const path = `http://localhost:8000/api/users/`

           axios.post(path, this.form.data).then((response) => {

               if (response.code == 200){

                   swal("Usuario: " + this.form.username + " creado exitosamente", "", "success")

               }

            }).catch((error) =>{

                console.log("Ha ocurrido un error" + error);

            })
       },
       getUser(){
           const path = `http://localhost:8000/api/users/${this.userId}/`

           axios.get(path).then((response) => {
                console.log(response.data)

                this.form.username = response.data.user;
                this.form.firstname = response.data.firstName
                this.form.lastname = response.data.lastName;
                this.form.email = response.data.email;
                this.form.password = response.data.password;

            }).catch((error) =>{

                console.log("Ha ocurrido un error" + error);

            })
       }
    },
    created(){
        this.getUser();
    }

}
</script>

<style scoped>

</style>