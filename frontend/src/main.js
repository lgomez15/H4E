// main.js
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import pinia from './store';
import axios from 'axios';
import './assets/index.css';

axios.defaults.baseURL = 'http://127.0.0.1:8000';
axios.defaults.withCredentials = true;

const app = createApp(App);

app.use(pinia);
app.use(router);

app.mount('#app');