import { createApp } from 'vue'
import './style.scss'
import App from './App.vue'
import router from './router'
import 'font-awesome/css/font-awesome.min.css'

const app = createApp(App)

app.use(router)
app.mount('#app')
