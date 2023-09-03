import { createRouter, createWebHistory } from 'vue-router'
import HistoryView from './views/HistoryView.vue'
import ConversionView from './views/ConversionView.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HistoryView
  },
  {
    path: '/history',
    name: 'History',
    component: HistoryView
  },
  {
    path: '/conversion',
    name: 'Conversion',
    component: ConversionView
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
