<template>
    <div class="relative isolate overflow-hidden bg-white px-6 py-24 sm:py-32 lg:overflow-visible lg:px-0">

      <div class="mx-auto grid max-w-2xl grid-cols-1 gap-x-8 gap-y-16 lg:mx-0 lg:max-w-none lg:grid-cols-2 lg:items-start lg:gap-y-10">
        <div class="lg:col-span-2 lg:col-start-1 lg:row-start-1 lg:mx-auto lg:grid lg:w-full lg:max-w-7xl lg:grid-cols-2 lg:gap-x-8 lg:px-8">
          <div class="lg:pr-4">
            <div class="lg:max-w-lg">
              <p class="text-base font-semibold leading-7 text-indigo-600">Open Source Monitoring</p>
              <h1 class="mt-2 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">Monitorización Estudiantil Simplificada</h1>
              <p class="mt-6 text-xl leading-8 text-gray-700">Iris es una plataforma open source que facilita el seguimiento académico de los estudiantes, proporcionando insights y datos en tiempo real para apoyar el éxito educativo.</p>
            </div>
          </div>
        </div>
        <div class="-ml-12 -mt-12 p-12 lg:sticky lg:top-4 lg:col-start-2 lg:row-span-2 lg:row-start-1 lg:overflow-hidden">
          <img class="w-[48rem] max-w-none rounded-xl bg-gray-900 shadow-xl ring-1 ring-gray-400/10 sm:w-[57rem]" src="https://www.desarketing.com/wp-content/uploads/2015/03/googlecharts.png" alt="Iris Platform Screenshot" />
        </div>
        <div class="lg:col-span-2 lg:col-start-1 lg:row-start-2 lg:mx-auto lg:grid lg:w-full lg:max-w-7xl lg:grid-cols-2 lg:gap-x-8 lg:px-8">
          <div class="lg:pr-4">
            <div class="max-w-xl text-base leading-7 text-gray-700 lg:max-w-lg">
              <p>Iris permite a los educadores y administradores visualizar y gestionar el progreso estudiantil en tiempo real, ayudando a identificar áreas de mejora y a tomar decisiones informadas.</p>
              <ul role="list" class="mt-8 space-y-8 text-gray-600">
                <li class="flex gap-x-3">
                  <CloudArrowUpIcon class="mt-1 h-5 w-5 flex-none text-indigo-600" aria-hidden="true" />
                  <span><strong class="font-semibold text-gray-900">Implementación rápida.</strong> Fácil de integrar en tu infraestructura actual y personalizable según las necesidades de tu institución.</span>
                </li>
                <li class="flex gap-x-3">
                  <LockClosedIcon class="mt-1 h-5 w-5 flex-none text-indigo-600" aria-hidden="true" />
                  <span><strong class="font-semibold text-gray-900">Datos seguros.</strong> Protegemos la privacidad de los estudiantes con las mejores prácticas de seguridad y cifrado de datos.</span>
                </li>
                <li class="flex gap-x-3">
                  <ServerIcon class="mt-1 h-5 w-5 flex-none text-indigo-600" aria-hidden="true" />
                  <span><strong class="font-semibold text-gray-900">Backups automáticos.</strong> Mantén la información de los estudiantes segura con backups regulares y gestión de datos en la nube.</span>
                </li>
              </ul>
              <p class="mt-8">Además de ser una herramienta de monitoreo, Iris fomenta la transparencia y colaboración entre docentes, estudiantes y familias, promoviendo un entorno educativo más inclusivo y adaptativo.</p>
              <h2 class="mt-16 text-2xl font-bold tracking-tight text-gray-900">Listo para cualquier entorno</h2>
              <p class="mt-6">Iris está diseñado para ser flexible, adaptable a diversas plataformas y contextos educativos, sin necesidad de infraestructura compleja o costosa. Implementa de forma sencilla en cualquier institución.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script setup>
import { CloudArrowUpIcon, LockClosedIcon, ServerIcon } from '@heroicons/vue/20/solid'
</script>
