<template lang = 'html'>
    <div class = 'container'>
        <div class = 'row'>
            <div class = 'col text-left'>
                <h2>Usuarios</h2>
                <div class='col-md-12'>
                    <b-table striped hover  :items = "users" :fields = "fields">
                        <template v-slot:cell(Acciones)="data">
                            <b-button size="sm"  variant="light" :to="{ name: 'EditUser', params: {userId: data.item.userId}}"><img src="../assets/edit.png" alt="" height="20px" width="20px"></b-button>
                            <b-button size="sm"  variant="light" v-on:click="userDelete(data.item.userId)" ><img src="../assets/delete.png" alt="" height="20px" width="20px"></b-button>
                        </template>
                    </b-table>
                </div>
            </div>
        </div>
    </div>
    
</template>

<script>
import axios from 'axios';
import Swal from 'sweetalert2'
const path = "http://127.0.0.1:8000/api/users/"
import { tokenService } from '../storage/tokenService'

export default {

    data(){
        return{
            fields:[
                { key: 'userId', label: 'Id' },
                { key: 'user', label: 'Nombre de Usuario' },
                { key: 'email', label: 'Email'},
                { key: 'firstName', label: 'Nombre'},
                { key: 'lastName', label: 'Apellido'},
                { key: 'Acciones', label: 'Acciones'},
            ],
            users:[]
        }
    },
    methods: {

        //Obteno Lista de usuarios
        getUsers(){
            axios.get(path)
            .then(response => (this.users = response.data))
            .catch(err => (console.log("Error: " + err)))
        },

        //Para eliminar usuarios
        userDelete(usertoDelete){
            //console.log(usertoDelete)
            var postData = {userId: usertoDelete}

            //hacemos request para eliminar usuario
            axios.delete(`http://127.0.0.1:8000/api/users/${usertoDelete}/`, {headers: {'Authorization': `token ${this.token}`}})
            .then(response => {

                //console.log(response.data)

                Swal.fire({
                          icon: 'success',
                          title: 'Excelente!',
                          text: 'Usuario eliminado exitosamente'})
            
            })
            .catch(err => {
                
                Swal.fire({icon: 'error',
                          title: 'Oops...',
                          text: 'Ha ocurrido un error al ejecutar el proceso. Intente nuevamente'})
                
            })

        }
    },
    created() {
            let token;
            this.token = tokenService.getToken();
            this.getUsers()

    }

}
</script>

<style scoped>

</style>