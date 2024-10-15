<template>
    <div class="floating-button" @click="toggleChatbot">
      <i class="fa fa-comment"></i>
    </div>
  </template>
  
  <script>
  export default {
    name: 'FloatingButton',
    methods: {
      toggleChatbot() {
        this.$emit('toggle-chatbot');
      }
    }
  }
  </script>
  
  <style scoped>
  .floating-button {
    position: fixed;
    bottom: 40px;
    right: 40px;
    width: 60px;
    height: 60px;
    background-color: #007bff;
    color: white;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 24px;
    cursor: pointer;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
    z-index: 1000;
  }
  .floating-button:hover {
    background-color: #0056b3;
  }
  </style>
  