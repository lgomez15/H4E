// src/components/MyComponent.vue
<script setup>
import { ref } from 'vue'

import Hero from '../components/Hero.vue'
import Footer from '../components/Footer.vue'
import Bento from '../components/Bento.vue'
import Content_1 from '@/components/content/Content_1.vue'
import Content_2 from '@/components/content/Content_2.vue'
</script>

<template>
  <div class="hero">
    <Hero />
  </div>
  <div class="bento">
    <Bento />
  </div>
  <div class="content">
    <Content_1 />
    <Content_2 />
  </div>
  <Footer />
</template>

<style scoped>

.hero {
padding: 20px;

}

.bento {
  padding-top: 50px;  /* Esto solo afecta al contenido dentro de Bento */
  margin-bottom: 50px; /* Espacio entre Bento y Content_1 */
}

.content {
  padding-top: 50px; /* Espacio interno en Content_1 */
}
</style>

