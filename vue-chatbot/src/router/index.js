import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import ServiceView from '../views/ServiceView.vue'
import WhyView from '../views/WhyView.vue'
import TeamView from '../views/TeamView.vue'

const routes = [
  { path: '/', name: 'Home', component: HomeView },
  { path: '/about', name: 'About', component: AboutView },
  { path: '/service', name: 'Service', component: ServiceView },
  { path: '/why', name: 'Why', component: WhyView },
  { path: '/team', name: 'Team', component: TeamView }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
