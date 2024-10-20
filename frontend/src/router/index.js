import { createRouter, createWebHistory } from 'vue-router';
import LandingView from '../views/LandingView.vue';
import AboutUs from '../views/AboutUs.vue';
import Contact from '../views/ContactView.vue';
import LoginView from '../views/LoginView.vue';
import Dashboard from '../views/Dashboard.vue';
import NotFoundView from '../views/NotFoundView.vue';


const routes = [
  { path: '/', name: 'Landing', component: LandingView },
  {path: '/about', name: 'AboutUs', component: AboutUs},
  {path: '/contact', name: 'Contact', component: Contact},
  {path: '/login', name: 'Login', component: LoginView},
  {path: '/dashboard', name: 'Dashboard', component: Dashboard},
  {path: '/:pathMatch(.*)*', name: 'NotFound', component: NotFoundView},


];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Navegación Guardada para rutas protegidas
router.beforeEach((to, from, next) => {
  const isAuthenticated = false; // Reemplazar con lógica real de autenticación
  if (to.meta.requiresAuth && !isAuthenticated) {
    next({ name: 'Login' });
  } else {
    next();
  }
});

export default router;


