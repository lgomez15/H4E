<!--
  Este ejemplo requiere algunas configuraciones en tu proyecto:

  1. Asegúrate de que Tailwind CSS esté configurado con el plugin de formularios:

  // tailwind.config.js
  module.exports = {
    // ...
    plugins: [
      // ...
      require('@tailwindcss/forms'),
    ],
  }
-->
<template>
  <!--
    Este ejemplo requiere actualizar tu plantilla:

    Asegúrate de que tu archivo principal (por ejemplo, `App.vue` o el archivo de entrada) incluya las clases `h-full bg-white` en las etiquetas `<html>` y `<body>`.
  
    ```
    <html class="h-full bg-white">
    <body class="h-full">
    ```
  -->
  <div class="relative overflow-hidden rounded-[20px]">
    <!-- Gradiente Animado -->
    <div class="absolute inset-0 z-0 bg-gradient-to-r from-[#121826] via-[#1e213a] to-[#121826] animate-gradient-animation"></div>
    
    <!-- Encabezado -->
    <header class="absolute inset-x-0 top-0 z-50">
      <nav class="flex items-center justify-between p-6 lg:px-8" aria-label="Global">
        <div class="flex lg:flex-1">
          <router-link to="/" class="-m-1.5 p-1.5">
            <span class="sr-only">Iris</span>
            <img class="h-8 w-auto" :src="logo" alt="Iris Logo" />
          </router-link>
        </div>
        <div class="flex lg:hidden">
          <button type="button" class="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-white" @click="mobileMenuOpen = true">
            <span class="sr-only">Open main menu</span>
            <Bars3Icon class="h-6 w-6" aria-hidden="true" />
          </button>
        </div>
        <div class="hidden lg:flex lg:gap-x-12">
          <router-link
            v-for="item in navigation"
            :key="item.name"
            :to="item.to"
            class="text-sm font-semibold leading-6 text-white"
          >
            {{ item.name }}
          </router-link>
        </div>
        <div class="hidden lg:flex lg:flex-1 lg:justify-end">
          <router-link to="/login" class="text-sm font-semibold leading-6 text-white">
            Iniciar Sesión <span aria-hidden="true">&rarr;</span>
          </router-link>
        </div>
      </nav>
      <Dialog class="lg:hidden" @close="mobileMenuOpen = false" :open="mobileMenuOpen">
        <div class="fixed inset-0 z-50" />
        <DialogPanel class="fixed inset-y-0 right-0 z-50 w-full overflow-y-auto bg-gray-900 px-6 py-6 sm:max-w-sm sm:ring-1 sm:ring-gray-900/10">
          <div class="flex items-center justify-between">
            <router-link to="/" class="-m-1.5 p-1.5">
              <span class="sr-only">Iris</span>
              <img class="h-8 w-auto" :src="logo" alt="Iris Logo" />
            </router-link>
            <button type="button" class="-m-2.5 rounded-md p-2.5 text-white" @click="mobileMenuOpen = false">
              <span class="sr-only">Cerrar menú</span>
              <XMarkIcon class="h-6 w-6" aria-hidden="true" />
            </button>
          </div>
          <div class="mt-6 flow-root">
            <div class="-my-6 divide-y divide-gray-700/10">
              <div class="space-y-2 py-6">
                <router-link
                  v-for="item in navigation"
                  :key="item.name"
                  :to="item.to"
                  class="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-white hover:bg-gray-800"
                >
                  {{ item.name }}
                </router-link>
              </div>
              <div class="py-6">
                <router-link to="/login" class="-mx-3 block rounded-lg px-3 py-2.5 text-base font-semibold leading-7 text-white hover:bg-gray-800">
                  Iniciar Sesión
                </router-link>
              </div>
            </div>
          </div>
        </DialogPanel>
      </Dialog>
    </header>

    <!-- Contenido principal -->
    <div class="relative isolate px-6 pt-14 lg:px-8">
      <!-- Fondos de gradiente animado (omito por brevedad) -->

      <div class="mx-auto max-w-2xl py-32 sm:py-48 lg:py-56">
        <div class="hidden sm:mb-8 sm:flex sm:justify-center">
          <div class="relative rounded-full px-3 py-1 text-sm leading-6 text-white ring-1 ring-gray-900/10 hover:ring-gray-900/20">
            ¡Bienvenidos a Iris! 
            <router-link to="/learn-more" class="font-semibold text-indigo-400 hover:text-indigo-300">
              <span class="absolute inset-0" aria-hidden="true"></span>
              Descubre más <span aria-hidden="true">&rarr;</span>
            </router-link>
          </div>
        </div>
        <div class="text-center">
          <h1 class="text-4xl font-bold tracking-tight text-white sm:text-6xl">Monitorea y Previene el Abandono Escolar</h1>
          <p class="mt-6 text-lg leading-8 text-gray-300">
            Iris utiliza inteligencia artificial para predecir y prevenir el abandono escolar, ofreciendo intervenciones personalizadas que mejoran la retención y el éxito académico de los estudiantes.
          </p>
          <div class="mt-10 flex items-center justify-center gap-x-6">
            <router-link to="/start" class="rounded-md bg-indigo-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">
              Comienza Ahora
            </router-link>
            <router-link to="/learn-more" class="text-sm font-semibold leading-6 text-white hover:text-gray-300">
              Aprende Más <span aria-hidden="true">→</span>
            </router-link>
          </div>
        </div>
      </div>

      <!-- Más fondos de gradiente animado (opcional) -->
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { Dialog, DialogPanel } from '@headlessui/vue'
import { Bars3Icon, XMarkIcon } from '@heroicons/vue/24/outline'
import logo from '../assets/logo-dark.svg'

const navigation = [
  { name: 'Características', to: '/features' },
  { name: 'Sobre Nosotros', to: '/about' },
  { name: 'Contacto', to: '/contact' },
]

const mobileMenuOpen = ref(false)
</script>

<style scoped>
@keyframes gradient-animation {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}

.animate-gradient-animation {
  background-size: 200% 200%;
  animation: gradient-animation 15s ease infinite;
}

/* Opcional: Ajustes adicionales de estilos */
</style>
