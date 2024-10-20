import { defineStore } from 'pinia';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    token: null,
  }),
  actions: {
    login(userData) {
      this.user = userData.user;
      this.token = userData.token;
      // Guardar en localStorage o cookies según se necesite
    },
    logout() {
      this.user = null;
      this.token = null;
      // Limpiar almacenamiento local
    },
  },
  getters: {
    isAuthenticated: (state) => !!state.token,
  },
});
