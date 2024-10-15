<template>
    <div>
      <HeaderComponent />
      <ServiceComponent />
      <AboutComponent />
      <WhyComponent />
      <TeamComponent />
      <ClientComponent />
      <InfoComponent />
      <FooterComponent />
      <FloatingButton @toggle-chatbot="toggleChatbot" />
      <ChatbotBubble :isVisible="isChatbotVisible" @toggle-chatbot="toggleChatbot" />
    </div>
  </template>
  
  <script>
  import HeaderComponent from '@/components/HeaderComponent.vue'
  import ServiceComponent from '@/components/ServiceComponent.vue'
  import AboutComponent from '@/components/AboutComponent.vue'
  import WhyComponent from '@/components/WhyComponent.vue'
  import TeamComponent from '@/components/TeamComponent.vue'
  import ClientComponent from '@/components/ClientComponent.vue'
  import InfoComponent from '@/components/InfoComponent.vue'
  import FooterComponent from '@/components/FooterComponent.vue'
  import FloatingButton from '@/components/FloatingButton.vue'
  import ChatbotBubble from '@/components/ChatbotBubble.vue'
  
  export default {
    name: 'HomeView',
    components: {
      HeaderComponent,
      ServiceComponent,
      AboutComponent,
      WhyComponent,
      TeamComponent,
      ClientComponent,
      InfoComponent,
      FooterComponent,
      FloatingButton,
      ChatbotBubble
    },
    data() {
      return {
        isChatbotVisible: false
      };
    },
    methods: {
      toggleChatbot() {
        this.isChatbotVisible = !this.isChatbotVisible;
      }
    }
  }

</script>
  
  <style scoped>
  /* Add relevant styles if needed */
  </style>
  