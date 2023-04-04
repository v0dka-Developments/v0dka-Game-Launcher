import { createRouter, createWebHistory } from 'vue-router';
import Login from '../components/Login.vue';
import LoggedIn from '../components/Logged_in.vue';

const routes = [
  {
    path: '/',
    name: 'login',
    component: Login
  },
  {
    path: '/logged_in',
    name: 'loggedin',
    component: LoggedIn
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
