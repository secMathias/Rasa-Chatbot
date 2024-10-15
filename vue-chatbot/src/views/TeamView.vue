<template>
    <div>
      <HeaderComponent />
      <TeamComponent />
      <FooterComponent />
    </div>
  </template>
  
  <script>
  import HeaderComponent from '@/components/HeaderComponent.vue'
  import TeamComponent from '@/components/TeamComponent.vue'
  import FooterComponent from '@/components/FooterComponent.vue'
  
  export default {
    name: 'TeamView',
    components: {
      HeaderComponent,
      TeamComponent,
      FooterComponent
    }
  }
  </script>
  
  <style scoped>
  /* Add relevant styles if needed */
  </style>
  