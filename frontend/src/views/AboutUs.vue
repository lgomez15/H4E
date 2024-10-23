<template>
  <div class="bg-gray-900">
    <!-- Header -->
    <header class="absolute inset-x-0 top-0 z-50">
      <nav class="mx-auto flex max-w-7xl items-center justify-between p-6 lg:px-8" aria-label="Global">
        <div class="flex lg:flex-1">
          <router-link to="/" class="-m-1.5 p-1.5">
            <span class="sr-only">Iris</span>
            <img class="h-8 w-auto" :src="logo" alt="Iris Logo" />
          </router-link>
        </div>
        <div class="flex lg:hidden">
          <button type="button" class="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-gray-400" @click="mobileMenuOpen = true">
            <span class="sr-only">Abrir menú principal</span>
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
        <DialogPanel class="fixed inset-y-0 right-0 z-50 w-full overflow-y-auto bg-gray-900 px-6 py-6 sm:max-w-sm sm:ring-1 sm:ring-white/10">
          <div class="flex items-center justify-between">
            <router-link to="/" class="-m-1.5 p-1.5">
              <span class="sr-only">Iris</span>
              <img class="h-8 w-auto" src="https://your-logo-url.com/logo.png" alt="Iris Logo" />
            </router-link>
            <button type="button" class="-m-2.5 rounded-md p-2.5 text-gray-400" @click="mobileMenuOpen = false">
              <span class="sr-only">Cerrar menú</span>
              <XMarkIcon class="h-6 w-6" aria-hidden="true" />
            </button>
          </div>
          <div class="mt-6 flow-root">
            <div class="-my-6 divide-y divide-gray-500/25">
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
    <main class="relative isolate">
      <!-- Background -->
      <div class="absolute inset-x-0 top-4 -z-10 flex transform-gpu justify-center overflow-hidden blur-3xl" aria-hidden="true">
        <div class="aspect-[1108/632] w-[69.25rem] flex-none bg-gradient-to-r from-[#80caff] to-[#4f46e5] opacity-25" style="clip-path: polygon(73.6% 51.7%, 91.7% 11.8%, 100% 46.4%, 97.4% 82.2%, 92.5% 84.9%, 75.7% 64%, 55.3% 47.5%, 46.5% 49.4%, 45% 62.9%, 50.3% 87.2%, 21.3% 64.1%, 0.1% 100%, 5.4% 51.1%, 21.4% 63.9%, 58.9% 0.2%, 73.6% 51.7%)" />
      </div>

      <!-- Header section -->
      <div class="px-6 pt-14 lg:px-8">
        <div class="mx-auto max-w-2xl pt-24 text-center sm:pt-40">
          <h2 class="text-4xl font-bold tracking-tight text-white sm:text-6xl">Monitorea y Previene el Abandono Escolar</h2>
          <p class="mt-6 text-lg leading-8 text-gray-300">Iris es una plataforma open source dedicada a la monitorización estudiantil, utilizando inteligencia artificial para prevenir el abandono escolar y fomentar el éxito académico.</p>
        </div>
      </div>

      <!-- Content section -->
      <div class="mx-auto mt-20 max-w-7xl px-6 lg:px-8">
        <div class="mx-auto max-w-2xl lg:mx-0 lg:max-w-none">
          <div class="grid max-w-xl grid-cols-1 gap-8 text-base leading-7 text-gray-300 lg:max-w-none lg:grid-cols-2">
            <div>
              <p>Iris proporciona herramientas avanzadas para analizar el rendimiento académico y detectar a tiempo a estudiantes en riesgo de abandono. Con datos precisos y recomendaciones personalizadas, nuestra plataforma apoya a docentes y padres en la creación de intervenciones efectivas.</p>
              <p class="mt-8">Nuestra misión es transformar los datos en acciones concretas que mejoren la retención escolar y promuevan un entorno educativo inclusivo y exitoso para todos los estudiantes.</p>
            </div>
            <div>
              <p>Mediante el uso de inteligencia artificial y técnicas de análisis predictivo, Iris identifica patrones y tendencias que pueden indicar posibles deserciones, permitiendo a las instituciones educativas tomar medidas preventivas y mejorar el apoyo a sus estudiantes.</p>
              <p class="mt-8">Únete a nosotros en nuestra misión de garantizar que cada estudiante tenga la oportunidad de alcanzar su máximo potencial académico.</p>
            </div>
          </div>
          <dl class="mt-16 grid grid-cols-1 gap-x-8 gap-y-12 sm:mt-20 sm:grid-cols-2 sm:gap-y-16 lg:mt-28 lg:grid-cols-4">
            <div v-for="(stat, statIdx) in stats" :key="statIdx" class="flex flex-col-reverse gap-y-3 border-l border-white/20 pl-6">
              <dt class="text-base leading-7 text-gray-300">{{ stat.label }}</dt>
              <dd class="text-3xl font-semibold tracking-tight text-white">{{ stat.value }}</dd>
            </div>
          </dl>
        </div>
      </div>

      <!-- Image section -->
      <div class="mt-32 sm:mt-40 xl:mx-auto xl:max-w-7xl xl:px-8">
        <img src="https://images.unsplash.com/photo-1521737852567-6949f3f9f2b5?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2894&q=80" alt="Monitorización Estudiantil" class="aspect-[9/4] w-full object-cover xl:rounded-3xl" />
      </div>

      <!-- Values section -->
      <div class="mx-auto mt-32 max-w-7xl px-6 sm:mt-40 lg:px-8">
        <div class="mx-auto max-w-2xl lg:mx-0">
          <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl">Nuestros Valores</h2>
          <p class="mt-6 text-lg leading-8 text-gray-300">En Iris, nos guiamos por principios fundamentales que aseguran el éxito y bienestar de los estudiantes:</p>
        </div>
        <dl class="mx-auto mt-16 grid grid-cols-1 gap-8 text-base leading-7 text-gray-300 sm:grid-cols-2 lg:mx-0 lg:max-w-none lg:gap-x-16">
          <div v-for="value in values" :key="value.name" class="relative pl-9">
            <dt class="inline font-semibold text-white">
              <component :is="value.icon" class="absolute left-1 top-1 h-5 w-5 text-indigo-500" aria-hidden="true" />
              {{ value.name }}
            </dt>
            {{ ' ' }}
            <dd class="inline">{{ value.description }}</dd>
          </div>
        </dl>
      </div>

      <!-- Team section -->
      <div class="mx-auto mt-32 max-w-7xl px-6 sm:mt-40 lg:px-8">
        <div class="mx-auto max-w-2xl lg:mx-0">
          <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl">Nuestro Equipo</h2>
          <p class="mt-6 text-lg leading-8 text-gray-300">Un equipo apasionado y comprometido con la educación y la tecnología, trabajando juntos para prevenir el abandono escolar y mejorar la experiencia educativa de los estudiantes.</p>
        </div>
        <ul role="list" class="mx-auto mt-20 grid max-w-2xl grid-cols-1 gap-x-8 gap-y-14 sm:grid-cols-2 lg:mx-0 lg:max-w-none lg:grid-cols-3 xl:grid-cols-4">
          <li v-for="person in team" :key="person.name">
            <img class="aspect-[14/13] w-full rounded-2xl object-cover" :src="person.imageUrl" alt="Imagen de {{ person.name }}" />
            <h3 class="mt-6 text-lg font-semibold leading-8 tracking-tight text-white">{{ person.name }}</h3>
            <p class="text-base leading-7 text-gray-300">{{ person.role }}</p>
            <p class="text-sm leading-6 text-gray-500">{{ person.location }}</p>
          </li>
        </ul>
      </div>

      <!-- CTA section -->
    </main>

    <!-- Footer -->
    <footer class="relative mt-32 sm:mt-40" aria-labelledby="footer-heading">
      <h2 id="footer-heading" class="sr-only">Footer</h2>
      <div class="mx-auto max-w-7xl px-6 pb-8 lg:px-8">
        <div class="xl:grid xl:grid-cols-3 xl:gap-8">
          <div class="space-y-8">
            <router-link to="/" class="-m-1.5 p-1.5">
              <span class="sr-only">Iris</span>
              <img class="h-8 w-auto" :src="logo" alt="Iris Logo" />
            </router-link>
            <p class="text-sm leading-6 text-gray-300">
              Iris es una plataforma de código abierto dedicada a la monitorización estudiantil, ayudando a prevenir el abandono escolar a través de intervenciones inteligentes.
            </p>
            <div class="flex space-x-6">
              <a
                v-for="item in footerNavigation.social"
                :key="item.name"
                :href="item.href"
                class="text-gray-500 hover:text-gray-400"
              >
                <span class="sr-only">{{ item.name }}</span>
                <component :is="item.icon" class="h-6 w-6" aria-hidden="true" />
              </a>
            </div>
          </div>
          <div class="mt-16 grid grid-cols-2 gap-8 xl:col-span-2 xl:mt-0">
            <div class="md:grid md:grid-cols-2 md:gap-8">
              <div class="mt-10 md:mt-0">
                <h3 class="text-sm font-semibold leading-6 text-white">Soporte</h3>
                <ul role="list" class="mt-6 space-y-4">
                  <li v-for="item in footerNavigation.support" :key="item.name">
                    <router-link :to="item.to" class="text-sm leading-6 text-gray-300 hover:text-white">
                      {{ item.name }}
                    </router-link>
                  </li>
                </ul>
              </div>
            </div>
            <div class="md:grid md:grid-cols-2 md:gap-8">
              <div>
                <h3 class="text-sm font-semibold leading-6 text-white">Empresa</h3>
                <ul role="list" class="mt-6 space-y-4">
                  <li v-for="item in footerNavigation.company" :key="item.name">
                    <router-link :to="item.to" class="text-sm leading-6 text-gray-300 hover:text-white">
                      {{ item.name }}
                    </router-link>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
        <div class="mt-16 border-t border-white/10 pt-8 sm:mt-20 lg:mt-24">
          <p class="text-xs leading-5 text-gray-400">&copy; 2024 Iris. Todos los derechos reservados.</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, h } from 'vue'
import { Dialog, DialogPanel } from '@headlessui/vue'
import logo from '../assets/logo-dark.svg'
import foto_andreia from '../assets/fotos/andreia.jpg'
import foto_luis from '../assets/fotos/luis.jpg'
import foto_alejandro from '../assets/fotos/alejandro.jpg'
import foto_efrain from  '../assets/fotos/efrain.jpg'
import foto_nuno from '../assets/fotos/nuno.jpg'
import { Bars3Icon, XMarkIcon } from '@heroicons/vue/24/outline'
import {
  AcademicCapIcon,
  HandRaisedIcon,
  RocketLaunchIcon,
  UserGroupIcon,
} from '@heroicons/vue/20/solid'

// Definición de navegación
const navigation = [
{name: 'Inicio', to: '/'},
  { name: 'Sobre Nosotros', to: '/about' },
  { name: 'Contacto', to: '/contact' },
]

// Definición de estadísticas
const stats = [
  { label: 'Año de Fundación', value: '2024' },
  { label: 'Equipo', value: '50+' },
  { label: 'Usuarios Activos', value: '10k+' },
  { label: 'Intervenciones Realizadas', value: '5k+' },
]

// Definición de valores
const values = [
  {
    name: 'Innovación Continua',
    description: 'Desarrollamos herramientas avanzadas para mejorar la monitorización estudiantil.',
    icon: RocketLaunchIcon,
  },
  {
    name: 'Responsabilidad Social',
    description: 'Comprometidos con la prevención del abandono escolar y el éxito académico.',
    icon: HandRaisedIcon,
  },
  {
    name: 'Colaboración Abierta',
    description: 'Fomentamos la colaboración mediante nuestra plataforma de código abierto.',
    icon: UserGroupIcon,
  },
  {
    name: 'Seguridad y Privacidad',
    description: 'Protegemos los datos personales con medidas avanzadas de seguridad.',
    icon: AcademicCapIcon,
  },
]

// Definición del equipo
const team = [
{
    name: 'Alejandro Gómez',
    role: 'Grado en Ingeniería Informática, USAL',
    imageUrl: foto_alejandro,
    location: 'Salamanca, España',
  },
  {
    name: 'Luis Gómez',
    role: 'Doble Grado en Administración y Dirección de Empresas e Ingeniería Informática, USAL',
    imageUrl: foto_luis,
    location: 'Ciudad de Panamá, Panamá',
  },
  {
    name: 'Andreia Barbosa',
    role: 'Relaciones Internacionales, Máster en Políticas Públicas, USAL',
    imageUrl: foto_andreia,
    location: 'Oporto, Portugal',
  },
  {
    name: 'Nuño Escudero',
    role: 'Doble Grado en Administración y Dirección de Empresas e Ingeniería Informática, USAL',
    imageUrl: foto_nuno,
    location: 'Burgos, España',
  },
  {
    name: 'Efraín Rujano',
    role: 'Psicólogo Clínico, Máster en Neuropsicología, Doctorado en Biomedicina Clínica y Experimental Salud, Enfermedad y Sociedad, USAL',
    imageUrl: foto_efrain,
    location: 'Ciudad de Panamá, Panamá',
  }



  // Agrega más miembros del equipo según sea necesario
]

// Definición de navegación del footer
const footerNavigation = {
  support: [
    { name: 'Documentación', to: '/documentation' },
    { name: 'Soporte Técnico', to: '/support' },
    { name: 'FAQ', to: '/faq' },
  ],
  company: [
    { name: 'Acerca de Iris', to: '/about' },
    { name: 'Carreras', to: '/careers' },
    { name: 'Blog', to: '/blog' },
  ],
  social: [
    {
      name: 'GitHub',
      href: 'https://github.com/tu-usuario/Iris',
      icon: {
        // SVG icon for GitHub
        render: () =>
          h('svg', { fill: 'currentColor', viewBox: '0 0 24 24' }, [
            h('path', {
              'fill-rule': 'evenodd',
              d: 'M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z',
              'clip-rule': 'evenodd',
            }),
          ]),
      },
    },
    // Agrega más redes sociales si es necesario
  ],
}

const mobileMenuOpen = ref(false)
</script>

<style scoped>
/* Puedes agregar estilos personalizados aquí si es necesario */
</style>
