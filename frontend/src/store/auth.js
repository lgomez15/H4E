// src/store/auth.js

import { defineStore } from 'pinia';
import axios from 'axios';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    // Información del usuario autenticado
    user: JSON.parse(localStorage.getItem('user')) || {
      id: null,
      id_profesor: null,
      email: '',
      nombre: '',
      apellido: '',
      departamento: '',
      telefono: '',
    },
    // Lista de clases asignadas al profesor
    clases: [],
    // Clase actualmente seleccionada
    claseSeleccionada: null,
    // Lista de estudiantes de la clase seleccionada
    estudiantes: [],
    // Estudiante actualmente seleccionado para mostrar detalles
    estudianteSeleccionado: null,
  }),
  actions: {
    /**
     * Acción para almacenar los datos del usuario después del login.
     * @param {Object} userData - Datos del usuario recibidos del backend.
     */
    login(userData) {
      this.user = {
        id: userData.id,
        id_profesor: userData.id_profesor,
        email: userData.email,
        nombre: userData.profesor.nombre,
        apellido: userData.profesor.apellido,
        departamento: userData.profesor.departamento,
        telefono: userData.profesor.telefono,
      };
      localStorage.setItem('user', JSON.stringify(this.user));
      console.log('Usuario autenticado:', this.user);

      // Después de iniciar sesión, cargar las clases asociadas
      this.fetchClases();
    },
    /**
     * Acción para limpiar los datos del usuario al hacer logout.
     */
    logout() {
      this.user = {
        id: null,
        id_profesor: null,
        email: '',
        nombre: '',
        apellido: '',
        departamento: '',
        telefono: '',
      };
      this.clases = [];
      this.claseSeleccionada = null;
      this.estudiantes = [];
      this.estudianteSeleccionado = null;
      localStorage.removeItem('user');
      console.log('Usuario desconectado');
    },
    /**
     * Acción para cargar los datos del usuario desde localStorage al iniciar la aplicación.
     */
    loadUserFromStorage() {
      try {
        const storedUser = localStorage.getItem('user');
        if (storedUser) {
          this.user = JSON.parse(storedUser);
          console.log('Usuario cargado desde localStorage:', this.user);
          // Después de cargar el usuario, cargar las clases asociadas
          this.fetchClases();
        }
      } catch (error) {
        console.error('Error al cargar el usuario desde localStorage:', error);
        this.user = {
          id: null,
          id_profesor: null,
          email: '',
          nombre: '',
          apellido: '',
          departamento: '',
          telefono: '',
        };
      }
    },
    /**
     * Acción para obtener las clases asociadas al profesor desde el backend.
     */
    async fetchClases() {
      if (!this.user.id_profesor) {
        console.error('No se ha establecido el ID del profesor.');
        return;
      }

      try {
        const response = await axios.get(`/profesores/${this.user.id_profesor}/clases`);
        this.clases = response.data; // Asumiendo que la respuesta es un array de clases
        console.log('Clases obtenidas:', this.clases);
      } catch (error) {
        console.error('Error al obtener las clases:', error);
      }
    },
    /**
     * Acción para seleccionar una clase y obtener sus estudiantes.
     * @param {Number} claseId - ID de la clase seleccionada.
     */
    async seleccionarClase(claseId) {
      // Buscar la clase en la lista de clases
      const clase = this.clases.find(c => c.id === claseId);
      if (!clase) {
        console.error(`Clase con ID ${claseId} no encontrada.`);
        return;
      }

      this.claseSeleccionada = clase;
      console.log('Clase seleccionada:', this.claseSeleccionada);

      // Obtener los estudiantes de la clase seleccionada
      await this.fetchEstudiantes(claseId);
    },
    /**
     * Acción para obtener los estudiantes de una clase desde el backend.
     * @param {Number} claseId - ID de la clase.
     */
    async fetchEstudiantes(claseId) {
      try {
        const response = await axios.get(`/clases/${claseId}`);
        this.estudiantes = response.data.estudiantes; // Asumiendo que la respuesta tiene un campo 'estudiantes' que es un array
        console.log(`Estudiantes de la clase ${claseId}:`, this.estudiantes);
      } catch (error) {
        console.error(`Error al obtener los estudiantes de la clase ${claseId}:`, error);
      }
    },
    /**
     * Acción para seleccionar un estudiante y obtener sus detalles.
     * @param {Number} estudianteId - ID del estudiante seleccionado.
     */
    async seleccionarEstudiante(estudianteId) {
      try {
        const response = await axios.get(`/estudiantes/${estudianteId}`);
        this.estudianteSeleccionado = response.data; // Asumiendo que la respuesta es un objeto con los datos del estudiante
        console.log('Estudiante seleccionado:', this.estudianteSeleccionado);
      } catch (error) {
        console.error(`Error al obtener los datos del estudiante ${estudianteId}:`, error);
      }
    },
  },
  getters: {
    /**
     * Getter para verificar si el usuario está autenticado.
     * @param {Object} state - Estado actual del store.
     * @returns {Boolean} - Verdadero si el usuario está autenticado.
     */
    isAuthenticated: (state) => !!state.user.id,
    
    /**
     * Getter para obtener el nombre completo del usuario.
     * @param {Object} state - Estado actual del store.
     * @returns {String} - Nombre completo del usuario o 'Usuario' por defecto.
     */
    getUserName: (state) => `${state.user.nombre} ${state.user.apellido}` || 'Usuario',
    
    /**
     * Getter para obtener el correo electrónico del usuario.
     * @param {Object} state - Estado actual del store.
     * @returns {String} - Correo electrónico del usuario o 'No Email' por defecto.
     */
    getUserEmail: (state) => state.user.email || 'No Email',
    
    /**
     * Getter para obtener el departamento del usuario.
     * @param {Object} state - Estado actual del store.
     * @returns {String} - Departamento del usuario o 'Sin Departamento' por defecto.
     */
    getUserDepartment: (state) => state.user.departamento || 'Sin Departamento',
    
    /**
     * Getter para obtener el teléfono del usuario.
     * @param {Object} state - Estado actual del store.
     * @returns {String} - Teléfono del usuario o 'Sin Teléfono' por defecto.
     */
    getUserPhone: (state) => state.user.telefono || 'Sin Teléfono',
    
    /**
     * Getter para obtener el ID del usuario.
     * @param {Object} state - Estado actual del store.
     * @returns {Number} - ID del usuario o null.
     */
    getUserId: (state) => state.user.id || null,
    
    /**
     * Getter para obtener el ID del profesor.
     * @param {Object} state - Estado actual del store.
     * @returns {Number} - ID del profesor o null.
     */
    getProfesorId: (state) => state.user.id_profesor || null,
    
    /**
     * Getter para obtener las clases asignadas al profesor.
     * @param {Object} state - Estado actual del store.
     * @returns {Array} - Lista de clases.
     */
    getClases: (state) => state.clases,
    
    /**
     * Getter para obtener la clase actualmente seleccionada.
     * @param {Object} state - Estado actual del store.
     * @returns {Object} - Clase seleccionada.
     */
    getClaseSeleccionada: (state) => state.claseSeleccionada,
    
    /**
     * Getter para obtener los estudiantes de la clase seleccionada.
     * @param {Object} state - Estado actual del store.
     * @returns {Array} - Lista de estudiantes.
     */
    getEstudiantes: (state) => state.estudiantes,
    
    /**
     * Getter para obtener el estudiante actualmente seleccionado.
     * @param {Object} state - Estado actual del store.
     * @returns {Object} - Estudiante seleccionado.
     */
    getEstudianteSeleccionado: (state) => state.estudianteSeleccionado,
  },
});
