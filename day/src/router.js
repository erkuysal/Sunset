import { createMemoryHistory, createRouter } from 'vue-router'

import HomeView from './components/HomeView.vue'
import SunriseView from './components/SunriseView.vue'

const routes = [
  { path: '/', component: HomeView },
  { path: '/sunrise', component: SunriseView },
]

const router = createRouter({
  history: createMemoryHistory(),
  routes,
})

export default router