<template>
    <!--
      This example requires updating your template:
  
      ```
      <html class="h-full">
      <body class="h-full">
      ```
    -->
    <main class="relative isolate min-h-full">
      <nav class="flex items-center justify-between p-6 lg:px-8" aria-label="Global">
        <div class="flex lg:flex-1">
          <router-link to="/" class="-m-1.5 p-1.5">
            <span class="sr-only">Iris</span>
            <img class="h-8 w-auto" :src="logo" alt="Iris Logo" />
          </router-link>
        </div>
        <div class="flex lg:hidden">
          <button
            type="button"
            class="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-gray-700"
            @click="mobileMenuOpen = true"
          >
            <span class="sr-only">Open main menu</span>
            <Bars3Icon class="h-6 w-6" aria-hidden="true" />
          </button>
        </div>
        <div class="hidden lg:flex lg:gap-x-12">
          <router-link
            v-for="item in navigation"
            :key="item.name"
            :to="item.to"
            class="text-sm font-semibold leading-6 text-gray-900"
          >
            {{ item.name }}
          </router-link>
        </div>
        <div class="hidden lg:flex lg:flex-1 lg:justify-end">
          <router-link to="/login" class="text-sm font-semibold leading-6 text-gray-900">
            Iniciar Sesión <span aria-hidden="true">&rarr;</span>
          </router-link>
        </div>
      </nav>
      <img src="https://images.unsplash.com/photo-1545972154-9bb223aac798?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=3050&q=80&exp=8&con=-15&sat=-75" alt="" class="absolute inset-0 -z-10 h-full w-full object-cover object-top" />
      <div class="mx-auto max-w-7xl px-6 py-32 text-center sm:py-40 lg:px-8">
        <p class="text-base font-semibold leading-8 text-white">404</p>
        <h1 class="mt-4 text-3xl font-bold tracking-tight text-white sm:text-5xl">Page not found</h1>
        <p class="mt-4 text-base text-white/70 sm:mt-6">Sorry, we couldn’t find the page you’re looking for.</p>
        <div class="mt-10 flex justify-center">
          <a href="#" class="text-sm font-semibold leading-7 text-white"><span aria-hidden="true">&larr;</span> Back to home</a>
        </div>
      </div>
      <Footer />
    </main>
  </template>
  

  <script setup>
    import { ref } from 'vue'
    import Navbar from '@/components/Navbar.vue'
    import Footer from '@/components/Footer.vue'
    import { Bars3Icon, XMarkIcon } from '@heroicons/vue/24/outline'
    import logo from '../assets/logo-404.svg'

  const navigation = [
    {name: 'Inicio', to: '/'},
    { name: 'Sobre Nosotros', to: '/about' },
  { name: 'Contacto', to: '/contact' },
  ]

  const mobileMenuOpen = ref(false)
  </script>