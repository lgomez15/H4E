<!-- src/components/Dashboard.vue -->

<template>
  <div>
    <!-- Modal para la Descripción del Estudiante -->
    <transition name="modal">
      <div v-if="estudianteSeleccionado" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
        <div class="bg-white rounded-lg shadow-lg w-3/4 max-w-md p-6 relative">
          <button
            class="absolute top-2 right-2 text-gray-500 hover:text-gray-700"
            @click="cerrarModal"
          >
            <XMarkIcon class="h-6 w-6" />
          </button>
          <Descripcion :estudiante="estudianteSeleccionado" />
        </div>
      </div>
    </transition>

    <TransitionRoot as="template" :show="sidebarOpen">
      <Dialog class="relative z-50 lg:hidden" @close="sidebarOpen = false">
        <TransitionChild
          as="template"
          enter="transition-opacity ease-linear duration-300"
          enter-from="opacity-0"
          enter-to="opacity-100"
          leave="transition-opacity ease-linear duration-300"
          leave-from="opacity-100"
          leave-to="opacity-0"
        >
          <div class="fixed inset-0 bg-gray-900/80" />
        </TransitionChild>

        <div class="fixed inset-0 flex">
          <TransitionChild
            as="template"
            enter="transition ease-in-out duration-300 transform"
            enter-from="-translate-x-full"
            enter-to="translate-x-0"
            leave="transition ease-in-out duration-300 transform"
            leave-from="translate-x-0"
            leave-to="-translate-x-full"
          >
            <DialogPanel class="relative mr-16 flex w-full max-w-xs flex-1">
              <TransitionChild
                as="template"
                enter="ease-in-out duration-300"
                enter-from="opacity-0"
                enter-to="opacity-100"
                leave="ease-in-out duration-300"
                leave-from="opacity-100"
                leave-to="opacity-0"
              >
                <div class="absolute left-full top-0 flex w-16 justify-center pt-5">
                  <button type="button" class="-m-2.5 p-2.5" @click="sidebarOpen = false">
                    <span class="sr-only">Close sidebar</span>
                    <XMarkIcon class="h-6 w-6 text-white" aria-hidden="true" />
                  </button>
                </div>
              </TransitionChild>
              <!-- Sidebar component -->
              <div class="flex grow flex-col gap-y-5 overflow-y-auto bg-gray-900 px-6 pb-4 ring-1 ring-white/10">
                <div class="flex h-16 shrink-0 items-center">
                  <img class="h-8 w-auto" :src="logo" alt="Iris Logo" />
                </div>
                <nav class="flex flex-1 flex-col">
                  <ul role="list" class="flex flex-1 flex-col gap-y-7">
                    <li>
                      <ul role="list" class="-mx-2 space-y-1">
                        <!-- Renderizar las clases dinámicamente -->
                        <li v-for="clase in clases" :key="clase.id">
                          <a
                            href="#"
                            :class="[
                              claseSeleccionada && claseSeleccionada.id === clase.id
                                ? 'bg-gray-700 text-white'
                                : 'text-gray-400 hover:bg-gray-800 hover:text-white',
                              'group flex gap-x-3 rounded-md p-2 text-sm font-semibold leading-6 cursor-pointer'
                            ]"
                            @click.prevent="seleccionarClase(clase.id)"
                          >
                            <!-- Puedes agregar un icono personalizado para las clases -->
                            <UsersIcon class="h-6 w-6 shrink-0" aria-hidden="true" />
                            {{ clase.nombre }}
                          </a>
                        </li>
                      </ul>
                    </li>
                    <li>
                      <div class="text-xs font-semibold leading-6 text-gray-400">Tu Organización</div>
                      <ul role="list" class="-mx-2 mt-2 space-y-1">
                        <li>
                          <a
                            href="#"
                            :class="[
                              'text-gray-400 hover:bg-gray-800 hover:text-white',
                              'group flex gap-x-3 rounded-md p-2 text-sm font-semibold leading-6 cursor-pointer'
                            ]"
                          >
                            <!-- Información de la organización -->
                            <HomeIcon class="h-6 w-6 shrink-0" aria-hidden="true" />
                            {{ organizacion.nombre }}
                          </a>
                        </li>
                      </ul>
                    </li>
                    <li class="mt-auto">
                      <a
                        href="#"
                        class="group -mx-2 flex gap-x-3 rounded-md p-2 text-sm font-semibold leading-6 text-gray-400 hover:bg-gray-800 hover:text-white"
                      >
                        <Cog6ToothIcon class="h-6 w-6 shrink-0" aria-hidden="true" />
                        Configuración
                      </a>
                    </li>
                  </ul>
                </nav>
              </div>
            </DialogPanel>
          </TransitionChild>
        </div>
      </Dialog>
    </TransitionRoot>

    <!-- Static sidebar for desktop -->
    <div class="hidden lg:fixed lg:inset-y-0 lg:z-50 lg:flex lg:w-72 lg:flex-col">
      <!-- Sidebar component -->
      <div class="flex grow flex-col gap-y-5 overflow-y-auto bg-gray-900 px-6 pb-4">
        <div class="flex h-16 shrink-0 items-center">
          <img class="h-8 w-auto" :src="logo" alt="Iris Logo" />
        </div>
        <nav class="flex flex-1 flex-col">
          <ul role="list" class="flex flex-1 flex-col gap-y-7">
            <li>
              <ul role="list" class="-mx-2 space-y-1">
                <!-- Renderizar las clases dinámicamente -->
                <li v-for="clase in clases" :key="clase.id">
                  <a
                    href="#"
                    :class="[
                      claseSeleccionada && claseSeleccionada.id === clase.id
                        ? 'bg-gray-700 text-white'
                        : 'text-gray-400 hover:bg-gray-800 hover:text-white',
                      'group flex gap-x-3 rounded-md p-2 text-sm font-semibold leading-6 cursor-pointer'
                    ]"
                    @click.prevent="seleccionarClase(clase.id)"
                  >
                    <!-- Puedes agregar un icono personalizado para las clases -->
                    <UsersIcon class="h-6 w-6 shrink-0" aria-hidden="true" />
                    {{ clase.nombre }}
                  </a>
                </li>
              </ul>
            </li>
            <li>
              <div class="text-xs font-semibold leading-6 text-gray-400">Tu Organización</div>
              <ul role="list" class="-mx-2 mt-2 space-y-1">
                <li>
                  <a
                    href="#"
                    :class="[
                      'text-gray-400 hover:bg-gray-800 hover:text-white',
                      'group flex gap-x-3 rounded-md p-2 text-sm font-semibold leading-6 cursor-pointer'
                    ]"
                  >
                    <!-- Información de la organización -->
                    <HomeIcon class="h-6 w-6 shrink-0" aria-hidden="true" />
                    {{ organizacion.nombre }}
                  </a>
                </li>
              </ul>
            </li>
            <li class="mt-auto">
              <a
                href="#"
                class="group -mx-2 flex gap-x-3 rounded-md p-2 text-sm font-semibold leading-6 text-gray-400 hover:bg-gray-800 hover:text-white"
              >
                <Cog6ToothIcon class="h-6 w-6 shrink-0" aria-hidden="true" />
                Configuración
              </a>
            </li>
          </ul>
        </nav>
      </div>
    </div>

    <div class="lg:pl-72">
      <div class="sticky top-0 z-40 flex h-16 shrink-0 items-center gap-x-4 border-b border-gray-200 bg-white px-4 shadow-sm sm:gap-x-6 sm:px-6 lg:px-8">
        <button type="button" class="-m-2.5 p-2.5 text-gray-700 lg:hidden" @click="sidebarOpen = true">
          <span class="sr-only">Abrir Navegador</span>
          <Bars3Icon class="h-6 w-6" aria-hidden="true" />
        </button>

        <!-- Separator -->
        <div class="h-6 w-px bg-gray-900/10 lg:hidden" aria-hidden="true" />

        <div class="flex flex-1 gap-x-4 self-stretch lg:gap-x-6">
          <form class="relative flex flex-1" action="#" method="GET">
            <label for="search-field" class="sr-only">Buscar</label>
            <MagnifyingGlassIcon class="pointer-events-none absolute inset-y-0 left-0 h-full w-5 text-gray-400" aria-hidden="true" />
            <input
              id="search-field"
              class="block h-full w-full border-0 py-0 pl-8 pr-0 text-gray-900 placeholder:text-gray-400 focus:ring-0 sm:text-sm"
              placeholder="Buscar..."
              type="search"
              name="search"
            />
          </form>
          <div class="flex items-center gap-x-4 lg:gap-x-6">
            <button type="button" class="-m-2.5 p-2.5 text-gray-400 hover:text-gray-500">
              <span class="sr-only">Ver Notificaciones</span>
              <BellIcon class="h-6 w-6" aria-hidden="true" />
            </button>

            <!-- Separator -->
            <div class="hidden lg:block lg:h-6 lg:w-px lg:bg-gray-900/10" aria-hidden="true" />

            <!-- Profile dropdown -->
            <Menu as="div" class="relative">
              <MenuButton class="-m-1.5 flex items-center p-1.5">
                <span class="sr-only">Abrir el menú de usuario</span>
                <img class="h-8 w-8 rounded-full bg-gray-50" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" />
                <span class="hidden lg:flex lg:items-center">
                  <span class="ml-4 text-sm font-semibold leading-6 text-gray-900" aria-hidden="true">{{ userName }}</span>
                  <ChevronDownIcon class="ml-2 h-5 w-5 text-gray-400" aria-hidden="true" />
                </span>
              </MenuButton>
              <transition
                enter-active-class="transition ease-out duration-100"
                enter-from-class="transform opacity-0 scale-95"
                enter-to-class="transform opacity-100 scale-100"
                leave-active-class="transition ease-in duration-75"
                leave-from-class="transform opacity-100 scale-100"
                leave-to-class="transform opacity-0 scale-95"
              >
                <MenuItems class="absolute right-0 z-10 mt-2.5 w-32 origin-top-right rounded-md bg-white py-2 shadow-lg ring-1 ring-gray-900/5 focus:outline-none">
                  <MenuItem
                    v-for="item in userNavigation"
                    :key="item.name"
                    v-slot="{ active }"
                    @click="handleUserNavigation(item)"
                  >
                    <a :href="item.href" :class="[active ? 'bg-gray-50' : '', 'block px-3 py-1 text-sm leading-6 text-gray-900']">
                      {{ item.name }}
                    </a>
                  </MenuItem>
                </MenuItems>
              </transition>
            </Menu>
          </div>
        </div>
      </div>

      <main class="py-10">
        <div class="px-4 sm:px-6 lg:px-8">
          <!-- Título del Dashboard -->
          <h1 class="text-2xl font-semibold text-gray-900 mb-6">Bienvenido, {{ userName }}</h1>

          <!-- Lista de Estudiantes -->
          <div v-if="claseSeleccionada" class="bg-white shadow overflow-hidden sm:rounded-md">
            <ul role="list" class="divide-y divide-gray-200">
              <li v-for="estudiante in estudiantes" :key="estudiante.id" class="px-4 py-4 sm:px-6 cursor-pointer hover:bg-gray-50" @click="seleccionarEstudiante(estudiante.id)">
                <div class="flex items-center justify-between">
                  <p class="text-sm font-medium text-indigo-600 truncate">{{ estudiante.nombre }} {{ estudiante.apellido }}</p>
                  <div class="ml-2 flex-shrink-0 flex">
                    <p class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
                      {{ estudiante.email }}
                    </p>
                  </div>
                </div>
                <div class="mt-2 sm:flex sm:justify-between">
                  <div class="sm:flex">
                    <p class="flex items-center text-sm text-gray-500">
                      <CalendarIcon class="flex-shrink-0 mr-1.5 h-5 w-5 text-gray-400" aria-hidden="true" />
                      Fecha de Nacimiento: {{ estudiante.fecha_nacimiento }}
                    </p>
                  </div>
                </div>
              </li>
            </ul>
          </div>

          <!-- Mensaje cuando no hay una clase seleccionada -->
          <div v-else class="text-gray-500">
            Selecciona una clase en la barra lateral para ver la lista de estudiantes.
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useAuthStore } from '../store/auth';
import Descripcion from '../components/Descripcion.vue';
import logo from "../assets/logo-dark.svg";
import {
  Dialog,
  DialogPanel,
  Menu,
  MenuButton,
  MenuItem,
  MenuItems,
  TransitionChild,
  TransitionRoot,
} from '@headlessui/vue';
import {
  Bars3Icon,
  BellIcon,
  Cog6ToothIcon,
  HomeIcon,
  UsersIcon,
  XMarkIcon,
  ChevronDownIcon,
  MagnifyingGlassIcon,
  CalendarIcon
} from '@heroicons/vue/24/outline';
import { PaperClipIcon } from '@heroicons/vue/20/solid' // Para Descripcion.vue

// Datos de navegación
const navigation = [
  { name: 'Organizaciones', href: '#', icon: HomeIcon, current: false },
  { name: 'Clases', href: '#', icon: UsersIcon, current: true },
];
const teams = [
  { id: 1, name: 'Primero B', href: '#', initial: '1B', current: false },
  { id: 2, name: 'Tercero A', href: '#', initial: '3A', current: false },
];
const userNavigation = [
  { name: 'Tu perfil', href: '#' },
  { name: 'Cerrar sesión', href: '#', action: 'logout' },
];

const sidebarOpen = ref(false);
const authStore = useAuthStore();

// Computed properties para acceder a las clases, usuario y estudiantes
const clases = computed(() => authStore.clases);
const claseSeleccionada = computed(() => authStore.claseSeleccionada);
const estudiantes = computed(() => authStore.estudiantes);
const estudianteSeleccionado = computed(() => authStore.estudianteSeleccionado);
const organizacion = computed(() => {
  if (clases.value.length > 0) {
    return clases.value[0].organizacion; // Asumiendo que todas las clases pertenecen a la misma organización
  }
  return { nombre: 'Sin Organización', direccion: '', telefono: '', id: null };
});
const userName = computed(() => authStore.getUserName);
const userEmail = computed(() => authStore.getUserEmail);
const userDepartment = computed(() => authStore.getUserDepartment);
const userPhone = computed(() => authStore.getUserPhone);

// Función para seleccionar una clase
const seleccionarClase = async (claseId) => {
  await authStore.seleccionarClase(claseId);
};

// Función para seleccionar un estudiante
const seleccionarEstudiante = async (estudianteId) => {
  await authStore.seleccionarEstudiante(estudianteId);
};

// Función para cerrar el modal de descripción
const cerrarModal = () => {
  authStore.estudianteSeleccionado = null;
};

// Manejar la acción de cerrar sesión
const handleUserNavigation = (item) => {
  if (item.action === 'logout') {
    authStore.logout();
    router.push({ name: 'Login' });
  } else {
    // Manejar otras acciones si es necesario
  }
};

// Importar useRouter para redirigir después de cerrar sesión
import { useRouter } from 'vue-router';
const router = useRouter();

// Cargar los datos del usuario al montar el componente
onMounted(() => {
  if (authStore.isAuthenticated && authStore.clases.length === 0) {
    authStore.fetchClases();
  }
});
</script>

<style scoped>
/* Transición para el modal */
.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.3s;
}
.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}
</style>
