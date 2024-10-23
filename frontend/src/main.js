// src/main.js
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import pinia from './store';
import axios from 'axios';
import './assets/index.css';
import VueApexCharts from 'vue3-apexcharts';

// Configurar Axios
axios.defaults.baseURL = 'http://127.0.0.1:8000';
axios.defaults.withCredentials = true;

// Configurar el token de Axios si está almacenado en localStorage
const token = localStorage.getItem('token');
if (token) {
  axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
}

const app = createApp(App);
app.use(VueApexCharts);
app.use(pinia);
app.use(router);

app.mount('#app');
