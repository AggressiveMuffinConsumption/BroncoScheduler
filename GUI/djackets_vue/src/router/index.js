import { createRouter, createWebHistory } from 'vue-router'
import LogInView from '../views/LogInView.vue'

const routes = [
  {
    path: '/',
    name: 'login',
    component: LogInView
  },
  {
    path: '/history',
    name: 'history',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/HistoryView.vue')
  },
  {
    path: '/required',
    name: 'required',
    component: () => import('../views/RequiredView.vue')
  },
  {
    path: '/home',
    name: 'home',
    component: () => import('../views/LandingView.vue')
  },
  {
    path: '/profile',
    name: 'profile',
    component: () => import('../views/ProfileView.vue')
  },
  {
    path: '/create-account',
    name: 'create account',
    component: () => import('../views/CreateAccView.vue')
  },
  {
    path: '/forgot-password',
    name: 'forgot password',
    component: () => import('../views/ForgotPassView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
