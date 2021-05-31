import Vue from 'vue'
import Router from 'vue-router'

//Importacion de componentes
import Main from '@/components/main'
import ListUsers from '@/components/ListUsers'
import AddUser from '@/components/AddUser'
import EditUser from '@/components/EditUser'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Main',
      component: Main
    },{
      path: '/list_users',
      name: 'ListUsers',
      component: ListUsers
    },{
      path: '/add_user',
      name: 'AddUser',
      component: AddUser
    },
    ,{
      path: '/edit_user',
      name: 'EditUser',
      component: EditUser
    }
  ],
  mode: 'history'
})
