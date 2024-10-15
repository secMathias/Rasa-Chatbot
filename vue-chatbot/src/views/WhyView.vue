<template>
    <div>
      <HeaderComponent />
      <WhyComponent />
      <FooterComponent />
    </div>
  </template>
  
  <script>
  import HeaderComponent from '@/components/HeaderComponent.vue'
  import WhyComponent from '@/components/WhyComponent.vue'
  import FooterComponent from '@/components/FooterComponent.vue'
  
  export default {
    name: 'WhyView',
    components: {
      HeaderComponent,
      WhyComponent,
      FooterComponent
    }
  }
  </script>
  
  <style scoped>
  /* Add relevant styles if needed */
  </style>
  