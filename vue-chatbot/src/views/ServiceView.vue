<template>
    <div>
      <HeaderComponent />
      <ServiceComponent />
      <FooterComponent />
    </div>
  </template>
  
  <script>
  import HeaderComponent from '@/components/HeaderComponent.vue'
  import ServiceComponent from '@/components/ServiceComponent.vue'
  import FooterComponent from '@/components/FooterComponent.vue'
  
  export default {
    name: 'ServiceView',
    components: {
      HeaderComponent,
      ServiceComponent,
      FooterComponent
    }
  }
  </script>
  
  <style scoped>
  /* Add relevant styles if needed */
  </style>
  