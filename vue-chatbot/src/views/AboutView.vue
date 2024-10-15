<template>
    <div>
      <HeaderComponent />
      <AboutComponent />
      <FooterComponent />
    </div>
  </template>
  
  <script>
  import HeaderComponent from '@/components/HeaderComponent.vue'
  import AboutComponent from '@/components/AboutComponent.vue'
  import FooterComponent from '@/components/FooterComponent.vue'
  
  export default {
    name: 'AboutView',
    components: {
      HeaderComponent,
      AboutComponent,
      FooterComponent
    }
  }
  </script>
  
  <style scoped>
  /* Add relevant styles if needed */
  </style>
  