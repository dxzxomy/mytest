import Vue from 'vue'
import Router from 'vue-router'


Vue.use(Router)

import Layout from '@/views/Layout/Index'
import Home from '@/views/Home/Index'
import Login from '@/views/Login/Index'

const routes = [
  {
    path: "/login",
    name: "login",
    component: Login,
  },
  {
    path: '/',
    component: Layout,
    children: [
      {
        path: '',
        name: 'Home',
        component: Home
      }

    ],
  }
]


export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})
