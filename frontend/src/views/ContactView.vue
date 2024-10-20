<template>
  <Navbar />
  <div class="bg-white py-24 sm:py-32">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      <div class="mx-auto max-w-2xl space-y-16 divide-y divide-gray-100 lg:mx-0 lg:max-w-none">
        <div class="grid grid-cols-1 gap-x-8 gap-y-10 lg:grid-cols-3">
          <div>
            <h2 class="text-3xl font-bold tracking-tight text-gray-900">Contacto</h2>
            <p class="mt-4 leading-7 text-gray-600">Estamos aquí para ayudarte. Si tienes alguna pregunta o deseas colaborar con nosotros, no dudes en ponerte en contacto.</p>
          </div>
          <div class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:col-span-2 lg:gap-8">
            <div class="rounded-2xl bg-gray-50 p-10">
              <h3 class="text-base font-semibold leading-7 text-gray-900">Colaborar</h3>
              <dl class="mt-3 space-y-1 text-sm leading-6 text-gray-600">
                <div>
                  <dt class="sr-only">Correo</dt>
                  <dd><a class="font-semibold text-indigo-600" href="mailto:colaborar@iris.org">colaborar@iris.org</a></dd>
                </div>
                <div class="mt-1">
                  <dt class="sr-only">Número de teléfono</dt>
                  <dd>+34 (600) 123-456</dd>
                </div>
              </dl>
            </div>
            <div class="rounded-2xl bg-gray-50 p-10">
              <h3 class="text-base font-semibold leading-7 text-gray-900">Prensa</h3>
              <dl class="mt-3 space-y-1 text-sm leading-6 text-gray-600">
                <div>
                  <dt class="sr-only">Correo</dt>
                  <dd><a class="font-semibold text-indigo-600" href="mailto:prensa@iris.org">prensa@iris.org</a></dd>
                </div>
                <div class="mt-1">
                  <dt class="sr-only">Número de teléfono</dt>
                  <dd>+34 (600) 234-567</dd>
                </div>
              </dl>
            </div>
            <div class="rounded-2xl bg-gray-50 p-10">
              <h3 class="text-base font-semibold leading-7 text-gray-900">Únete a nuestro equipo</h3>
              <dl class="mt-3 space-y-1 text-sm leading-6 text-gray-600">
                <div>
                  <dt class="sr-only">Correo</dt>
                  <dd><a class="font-semibold text-indigo-600" href="mailto:carreras@iris.org">carreras@iris.org</a></dd>
                </div>
                <div class="mt-1">
                  <dt class="sr-only">Número de teléfono</dt>
                  <dd>+34 (600) 345-678</dd>
                </div>
              </dl>
            </div>
            <div class="rounded-2xl bg-gray-50 p-10">
              <h3 class="text-base font-semibold leading-7 text-gray-900">Saluda</h3>
              <dl class="mt-3 space-y-1 text-sm leading-6 text-gray-600">
                <div>
                  <dt class="sr-only">Correo</dt>
                  <dd><a class="font-semibold text-indigo-600" href="mailto:hola@iris.org">hola@iris.org</a></dd>
                </div>
                <div class="mt-1">
                  <dt class="sr-only">Número de teléfono</dt>
                  <dd>+34 (600) 456-789</dd>
                </div>
              </dl>
            </div>
          </div>
        </div>
        <div class="grid grid-cols-1 gap-x-8 gap-y-10 pt-16 lg:grid-cols-3">
          <div>
            <h2 class="text-3xl font-bold tracking-tight text-gray-900">Ubicaciones</h2>
            <p class="mt-4 leading-7 text-gray-600">Nos encontramos en varias ciudades para ofrecer soporte y colaboración en diferentes regiones.</p>
          </div>
          <div class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:col-span-2 lg:gap-8">
            <div class="rounded-2xl bg-gray-50 p-10">
              <h3 class="text-base font-semibold leading-7 text-gray-900">Madrid</h3>
              <address class="mt-3 space-y-1 text-sm not-italic leading-6 text-gray-600">
                <p>Calle de Alcalá, 45</p>
                <p>Madrid, España 28014</p>
              </address>
            </div>
            <div class="rounded-2xl bg-gray-50 p-10">
              <h3 class="text-base font-semibold leading-7 text-gray-900">Barcelona</h3>
              <address class="mt-3 space-y-1 text-sm not-italic leading-6 text-gray-600">
                <p>Avinguda Diagonal, 678</p>
                <p>Barcelona, España 08018</p>
              </address>
            </div>
            <div class="rounded-2xl bg-gray-50 p-10">
              <h3 class="text-base font-semibold leading-7 text-gray-900">Valencia</h3>
              <address class="mt-3 space-y-1 text-sm not-italic leading-6 text-gray-600">
                <p>Carrer de Colón, 89</p>
                <p>Valencia, España 46004</p>
              </address>
            </div>
            <div class="rounded-2xl bg-gray-50 p-10">
              <h3 class="text-base font-semibold leading-7 text-gray-900">Sevilla</h3>
              <address class="mt-3 space-y-1 text-sm not-italic leading-6 text-gray-600">
                <p>Calle Sierpes, 123</p>
                <p>Sevilla, España 41004</p>
              </address>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <Footer />
</template>

<script setup>
import Navbar from '../components/Navbar.vue';
import Footer from '../components/Footer.vue';
</script>
