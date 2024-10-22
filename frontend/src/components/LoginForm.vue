<!-- src/components/LoginForm.vue -->

<template>
  <div class="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">
        Inicia sesión en tu cuenta
      </h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form @submit.prevent="handleLogin" class="space-y-6">
        <div>
          <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Correo electrónico</label>
          <div class="mt-2">
            <input
              v-model="email"
              id="email"
              name="email"
              type="email"
              autocomplete="email"
              required
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 
              placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            />
          </div>
        </div>

        <div>
          <div class="flex items-center justify-between">
            <label for="password" class="block text-sm font-medium leading-6 text-gray-900">Contraseña</label>
            <div class="text-sm">
              <a href="#" class="font-semibold text-indigo-600 hover:text-indigo-500">¿Olvidaste tu contraseña?</a>
            </div>
          </div>
          <div class="mt-2">
            <input
              v-model="password"
              id="password"
              name="password"
              type="password"
              autocomplete="current-password"
              required
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 
              placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            />
          </div>
        </div>

        <div>
          <button
            type="submit"
            class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold 
            leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 
            focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
          >
            Iniciar sesión
          </button>
        </div>
      </form>

      <p class="mt-10 text-center text-sm text-gray-500">
        ¿No tienes una cuenta?
        <a href="#" class="font-semibold leading-6 text-indigo-600 hover:text-indigo-500">Regístrate ahora</a>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useAuthStore } from '../store/auth';
import { useRouter } from 'vue-router';

// Definir referencias para los campos de entrada
const email = ref('');
const password = ref('');

// Acceder al store de autenticación
const authStore = useAuthStore();

// Acceder al router para redireccionar después del login
const router = useRouter();

/**
 * Función para manejar el inicio de sesión.
 */
const handleLogin = async () => {
  try {
    // Crear los parámetros para la petición form-urlencoded
    const params = new URLSearchParams();
    params.append('username', email.value); // OAuth2PasswordRequestForm usa 'username' para el email
    params.append('password', password.value);

    // Realizar la petición POST al backend
    const response = await axios.post('http://127.0.0.1:8000/auth/jwt/login', params, {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      withCredentials: true, // Si estás usando cookies para almacenar el token
    });

    console.log('Respuesta del backend:', response.data); // Log para verificar la respuesta

    // Verificar que la respuesta contiene el objeto 'user'
    if (!response.data.user) {
      throw new Error('No se recibió la información del usuario desde el backend.');
    }

    // Pasar todo el objeto 'user' al store para almacenar los campos específicos
    authStore.login(response.data.user);

    console.log('Usuario autenticado:', authStore.user); // Verificar en consola

    // Redirigir al Dashboard
    router.push({ name: 'Dashboard' });
  } catch (error) {
    console.error(error);
    alert(error.response?.data?.detail || error.message || 'Error al iniciar sesión');
  }
};
</script>

<style scoped>
/* Puedes agregar estilos personalizados aquí */
</style>
