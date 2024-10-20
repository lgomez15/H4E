<template>
    <div class="bg-white py-24 sm:py-32">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="mx-auto max-w-2xl lg:text-center">
          <h2 class="text-base font-semibold leading-7 text-indigo-600">Monitorización Inteligente</h2>
          <p class="mt-2 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">Todo lo que necesitas para prevenir el abandono escolar</p>
          <p class="mt-6 text-lg leading-8 text-gray-600">
            Iris utiliza inteligencia artificial para identificar y apoyar a los estudiantes en riesgo de abandonar la escuela, proporcionando intervenciones personalizadas que mejoran la retención y el éxito académico.
          </p>
        </div>
        <div class="mx-auto mt-16 max-w-2xl sm:mt-20 lg:mt-24 lg:max-w-4xl">
          <dl class="grid max-w-xl grid-cols-1 gap-x-8 gap-y-10 lg:max-w-none lg:grid-cols-2 lg:gap-y-16">
            <div v-for="feature in features" :key="feature.name" class="relative pl-16">
              <dt class="text-base font-semibold leading-7 text-gray-900">
                <div class="absolute left-0 top-0 flex h-10 w-10 items-center justify-center rounded-lg bg-indigo-600">
                  <component :is="feature.icon" class="h-6 w-6 text-white" aria-hidden="true" />
                </div>
                {{ feature.name }}
              </dt>
              <dd class="mt-2 text-base leading-7 text-gray-600">{{ feature.description }}</dd>
            </div>
          </dl>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ChartBarIcon, LightBulbIcon, UserGroupIcon, ShieldCheckIcon } from '@heroicons/vue/24/outline'
  
  const features = [
    {
      name: 'Predicción Inteligente',
      description:
        'Utiliza modelos avanzados de inteligencia artificial para identificar a los estudiantes en riesgo de abandonar la escuela, permitiendo intervenciones tempranas y efectivas.',
      icon: ChartBarIcon,
    },
    {
      name: 'Intervenciones Personalizadas',
      description:
        'Proporciona recomendaciones y acciones específicas basadas en el análisis de datos individuales, adaptándose a las necesidades de cada estudiante.',
      icon: LightBulbIcon,
    },
    {
      name: 'Interfaz Intuitiva',
      description:
        'Ofrece una interfaz amigable y accesible para docentes y padres, facilitando el monitoreo continuo y la toma de decisiones informadas.',
      icon: UserGroupIcon,
    },
    {
      name: 'Seguridad y Privacidad',
      description:
        'Garantiza la protección de los datos personales de los estudiantes mediante medidas avanzadas de seguridad y cumplimiento de normativas de privacidad.',
      icon: ShieldCheckIcon,
    },
  ]
  </script>
  
  <style scoped>
  /* Puedes agregar estilos personalizados aquí si es necesario */
  </style>
  