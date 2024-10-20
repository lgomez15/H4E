
<script setup>
import { ref } from 'vue'
import { Bars3Icon, XMarkIcon } from '@heroicons/vue/24/outline'
import logo from '../assets/logo.svg'

const navigation = [
  { name: 'Características', to: '/features' },
  { name: 'Sobre Nosotros', to: '/about' },
  { name: 'Contacto', to: '/contact' },
]

const mobileMenuOpen = ref(false)
</script>


<template>
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
</template>

<script setup>
</script>