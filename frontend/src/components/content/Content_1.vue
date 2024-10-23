<template>
  <div class="bg-gray-900 py-24 sm:py-32">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      <div class="mx-auto max-w-2xl lg:text-center">
        <h2 class="text-base font-semibold leading-7 text-indigo-400">Monitorización Inteligente</h2>
        <p class="mt-2 text-3xl font-bold tracking-tight text-white sm:text-4xl">Iris: Plataforma OpenSource de Monitorización Estudiantil</p>
        <p class="mt-6 text-lg leading-8 text-gray-300">
          Iris utiliza inteligencia artificial para predecir y prevenir el abandono escolar, ofreciendo intervenciones personalizadas que mejoran la retención y el éxito académico de los estudiantes.
        </p>
      </div>
      <div class="mx-auto mt-16 max-w-2xl sm:mt-20 lg:mt-24 lg:max-w-none">
        <dl class="grid max-w-xl grid-cols-1 gap-x-8 gap-y-16 lg:max-w-none lg:grid-cols-3">
          <div v-for="feature in features" :key="feature.name" class="flex flex-col">
            <dt class="flex items-center gap-x-3 text-base font-semibold leading-7 text-white">
              <component :is="feature.icon" class="h-5 w-5 flex-none text-indigo-400" aria-hidden="true" />
              {{ feature.name }}
            </dt>
            <dd class="mt-4 flex flex-auto flex-col text-base leading-7 text-gray-300">
              <p class="flex-auto">{{ feature.description }}</p>
              <p class="mt-6">
                <a :href="feature.href" class="text-sm font-semibold leading-6 text-indigo-400">Aprende más <span aria-hidden="true">→</span></a>
              </p>
            </dd>
          </div>
        </dl>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ChartBarIcon, LightBulbIcon, UserGroupIcon } from '@heroicons/vue/20/solid'

const features = [
  {
    name: 'Predicción de Abandono Escolar',
    description:
      'Utiliza modelos de inteligencia artificial para identificar estudiantes en riesgo de abandonar la escuela, permitiendo intervenciones tempranas y efectivas.',
    href: '#',
    icon: ChartBarIcon,
  },
  {
    name: 'Interfaz Intuitiva',
    description:
      'Una interfaz de usuario amigable y accesible para docentes y padres, facilitando el monitoreo continuo y la toma de decisiones informadas.',
    href: '#',
    icon: LightBulbIcon,
  },
  {
    name: 'Código Abierto',
    description:
      'Desarrollada como una plataforma de código abierto, fomentando la colaboración y la mejora continua por parte de la comunidad educativa.',
    href: '#',
    icon: UserGroupIcon,
  },
]
</script>

<style scoped>
/* Puedes agregar estilos personalizados aquí si es necesario */
</style>
