<!-- src/components/Descripcion.vue -->
<template>
  <div>
    <!-- Información del Estudiante -->
    <div class="mb-6">
      <h2 class="text-2xl font-bold text-gray-900">{{ estudiante.nombre }} {{ estudiante.apellido }}</h2>
      <p class="text-gray-600">Fecha de nacimiento: {{ estudiante.fecha_nacimiento }}</p>
      <p class="text-gray-600 mb-4">Email: {{ estudiante.email }}</p>

      <!-- Información adicional -->
      <div class="mb-6">
        <!-- Media de las Notas -->
        <div class="flex items-center mb-4">
          <h3 class="text-lg font-bold text-indigo-600 mr-4">Media de Notas:</h3>
          <span 
            :class="{
              'bg-green-100 text-green-800': mediaNota >= 85,
              'bg-yellow-100 text-yellow-800': mediaNota >= 70 && mediaNota < 85,
              'bg-red-100 text-red-800': mediaNota < 70
            }"
            class="px-3 py-1 rounded-full text-sm font-semibold"
          >
            {{ mediaNota }}
          </span>
        </div>

        <!-- Predicción de Riesgo -->
        <div class="flex items-center mb-4">
          <h3 class="text-lg font-bold text-indigo-600 mr-4">Predicción de Riesgo:</h3>
          <span 
            :class="{
              'bg-green-100 text-green-800': riesgo === 'bajo riesgo',
              'bg-yellow-100 text-yellow-800': riesgo === 'medio riesgo',
              'bg-red-100 text-red-800': riesgo === 'alto riesgo'
            }"
            class="px-3 py-1 rounded-full text-sm font-semibold"
          >
            {{ riesgo }}
          </span>
        </div>

        <!-- Resumen de Asistencias -->
        <div>
          <h3 class="text-lg font-bold text-indigo-600 mb-2">Resumen de Asistencias</h3>
          <ul class="list-disc pl-5">
            <li v-for="asistencia in asistencias" :key="asistencia.id" class="mb-1">
              <span class="font-semibold">{{ asistencia.fecha }}:</span>
              <span :class="asistencia.presente ? 'text-green-600' : 'text-red-600'">
                {{ asistencia.presente ? 'Presente' : 'Ausente' }}
              </span>
              <span v-if="asistencia.observaciones" class="text-gray-500">({{ asistencia.observaciones }})</span>
            </li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Gráfico de Notas vs Media con ApexCharts -->
    <div class="mb-6">
      <apexchart
        v-if="seriesNotas.length"
        :options="chartOptionsNotas"
        :series="seriesNotas"
        type="bar"
        height="350"
      ></apexchart>
    </div>

    <!-- Gráfico de Calificaciones con ApexCharts -->
    <div class="mb-6">
      <apexchart
        v-if="seriesCalificaciones.length"
        :options="chartOptionsCalificaciones"
        :series="seriesCalificaciones"
        type="line"
        height="350"
      ></apexchart>
    </div>

    <!-- Imagen de Explicación de la IA -->
    <div class="mt-6">
      <h3 class="text-lg font-bold text-indigo-600 mb-2">Explicación de la IA</h3>
      <img 
        :src="explicacion" 
        alt="Explicación de la IA" 
        class="w-full h-auto rounded-md shadow-md"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import ApexCharts from 'vue3-apexcharts';
import explicacion from '../assets/explicacion.png'; // Asegúrate de que la ruta es correcta

// Definir las props que recibe el componente
const props = defineProps({
  estudiante: {
    type: Object,
    required: true,
  },
});

// Variables reactivas para los gráficos y datos adicionales
const seriesNotas = ref([]);
const chartOptionsNotas = ref({
  chart: { type: 'bar', height: 350 },
  plotOptions: {
    bar: { horizontal: false, columnWidth: '55%', endingShape: 'rounded' },
  },
  dataLabels: { enabled: false },
  stroke: { show: true, width: 2, colors: ['transparent'] },
  xaxis: { categories: [] },
  fill: { opacity: 1 },
  tooltip: {
    y: {
      formatter: (val) => `${val} puntos`,
    },
  },
});

const seriesCalificaciones = ref([]);
const chartOptionsCalificaciones = ref({
  chart: { type: 'line', height: 350 },
  stroke: { width: 2, curve: 'smooth' },
  xaxis: { categories: [] },
  tooltip: {
    y: {
      formatter: (val) => `${val} puntos`,
    },
  },
});

// Variables para asistencias, media de notas y predicción de riesgo
const asistencias = ref([]);
const mediaNota = ref(null);
const riesgo = ref('');

// Funciones para obtener los datos desde las APIs
const fetchNotasConMedia = async (estudianteId) => {
  try {
    const response = await axios.get(`http://127.0.0.1:8000/calificaciones/detalle/${estudianteId}`);
    const notas = response.data;

    const labels = notas.map((nota) => nota.examen);
    const notasEstudiante = notas.map((nota) => nota.nota_estudiante);
    const mediasExamen = notas.map((nota) => nota.media_examen);

    chartOptionsNotas.value.xaxis.categories = labels;
    seriesNotas.value = [
      { name: 'Nota Estudiante', data: notasEstudiante },
      { name: 'Media Examen', data: mediasExamen },
    ];
  } catch (error) {
    console.error('Error al obtener las notas con la media:', error);
  }
};

const fetchCalificaciones = async (estudianteId) => {
  try {
    const response = await axios.get(`http://127.0.0.1:8000/calificaciones/alumno/${estudianteId}`);
    const calificaciones = response.data;

    const notas = calificaciones.map((calificacion) => calificacion.nota);
    const labels = calificaciones.map((_, index) => `Calificación ${index + 1}`);

    chartOptionsCalificaciones.value.xaxis.categories = labels;
    seriesCalificaciones.value = [{ name: 'Calificación', data: notas }];
  } catch (error) {
    console.error('Error al obtener las calificaciones:', error);
  }
};

const fetchAsistencias = async (estudianteId) => {
  try {
    const response = await axios.get(`http://127.0.0.1:8000/estudiantes/asistencias/${estudianteId}`);
    asistencias.value = response.data;
  } catch (error) {
    console.error('Error al obtener las asistencias:', error);
  }
};

const fetchMediaNota = async (estudianteId) => {
  try {
    const response = await axios.get(`http://127.0.0.1:8000/calificaciones/media/${estudianteId}`);
    mediaNota.value = response.data;
  } catch (error) {
    console.error('Error al obtener la media de notas:', error);
  }
};

const fetchPrediccionRiesgo = async (estudianteId) => {
  try {
    const response = await axios.get(`http://127.0.0.1:8000/estudiantes/prediccion/${estudianteId}`);
    riesgo.value = response.data.riesgo;
  } catch (error) {
    console.error('Error al obtener la predicción de riesgo:', error);
  }
};

// Llamar a las funciones al montar el componente
onMounted(() => {
  if (props.estudiante.id) {
    fetchNotasConMedia(props.estudiante.id);
    fetchCalificaciones(props.estudiante.id);
    fetchAsistencias(props.estudiante.id);
    fetchMediaNota(props.estudiante.id);
    fetchPrediccionRiesgo(props.estudiante.id);
  }
});
</script>

<style scoped>
/* Estilos personalizados para el componente Descripcion */

/* Estilos para la lista de asistencias */
ul.list-disc {
  margin-top: 0.5rem;
}

/* Responsividad y ajustes adicionales si son necesarios */
img {
  max-width: 100%;
  height: auto;
}
</style>
