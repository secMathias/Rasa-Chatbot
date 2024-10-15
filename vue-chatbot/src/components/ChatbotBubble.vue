<template>
  <div v-if="isVisible" class="chatbot-bubble">
    <div class="chatbot-header">
      <h4>Chatbot</h4>
      <button @click="closeChatbot" class="close-btn">&times;</button>
    </div>
    <div class="chatbot-body" ref="chatBody">
      <div 
        v-for="message in messages" 
        :key="message.id" 
        :class="['message', message.isUser ? 'user-message' : 'chatbot-message']"
      >
        <p>{{ message.text }}</p>
      </div>
    </div>
    <div class="chatbot-footer">
      <form @submit.prevent="sendMessage">
        <input 
          type="text" 
          v-model="newMessage" 
          placeholder="Type a message..." 
          @keyup.enter="sendMessage"
        />
        <button type="submit" class="send-btn">Send</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ChatbotBubble',
  props: ['isVisible'],
  data() {
    return {
      newMessage: '',
      messages: [
        { id: 0, text: 'Hello! I am the chatbot in service of Elite. Ask me something.', isUser: false }
      ]
    };
  },
  methods: {
    closeChatbot() {
      this.$emit('toggle-chatbot');
    },
    async sendMessage() {
      if (this.newMessage.trim() !== '') {
        const userMessage = { id: Date.now(), text: this.newMessage, isUser: true };
        this.messages.push(userMessage);
        this.newMessage = '';
        this.scrollToBottom();

        try {
          // Send the message to Rasa's REST endpoint
          const response = await axios.post('http://localhost:5005/webhooks/rest/webhook', {
            sender: 'user', // a unique identifier for each conversation
            message: userMessage.text
          });

          // Rasa returns an array of responses, which could contain multiple messages
          if (response.data && response.data.length) {
            response.data.forEach((botMessage) => {
              this.messages.push({
                id: Date.now(),
                text: botMessage.text,
                isUser: false
              });
            });
          } else {
            this.messages.push({
              id: Date.now(),
              text: "Sorry, I didn't get that.",
              isUser: false
            });
          }

          this.scrollToBottom();
        } catch (error) {
          console.error('Error connecting to the Rasa server:', error);
          this.messages.push({
            id: Date.now(),
            text: 'Error: Could not connect to the server.',
            isUser: false
          });
        }
      }
    },
    scrollToBottom() {
      this.$nextTick(() => {
        const chatBody = this.$refs.chatBody;
        chatBody.scrollTop = chatBody.scrollHeight;
      });
    }
  }
};
</script>

<style scoped>
/* Add your existing styles here */
.chatbot-bubble {
  position: fixed;
  bottom: 110px;
  right: 40px;
  width: 300px;
  height: 450px;
  background-color: #f9f9f9;
  border: 1px solid #e0e0e0;
  border-radius: 15px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  z-index: 1000;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  font-family: 'Roboto', sans-serif;
}

.chatbot-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  background-color: #007bff;
  color: white;
  border-radius: 15px 15px 0 0;
  font-size: 18px;
}

.chatbot-header h4 {
  margin: 0;
  font-size: 18px;
  font-weight: 500;
}

.chatbot-header .close-btn {
  background: transparent;
  border: none;
  font-size: 24px;
  color: white;
  cursor: pointer;
}

.chatbot-body {
  flex: 1;
  padding: 10px;
  overflow-y: auto;
  font-size: 14px;
  line-height: 1.4;
  color: #333;
  display: flex;
  flex-direction: column;
}

.message {
  margin: 3px 0;
  padding: 8px 10px;
  border-radius: 10px;
  max-width: 70%;
  word-wrap: break-word;
  display: inline-block;
}

.user-message {
  background-color: #007bff;
  color: white;
  align-self: flex-end;
  text-align: right;
}

.chatbot-message {
  background-color: #0056b3;
  color: white;
  align-self: flex-start;
  text-align: left;
}

.chatbot-footer {
  padding: 10px;
  border-top: 1px solid #e0e0e0;
  background-color: #f1f1f1;
}

.chatbot-footer form {
  display: flex;
}

.chatbot-footer input {
  flex: 1;
  padding: 8px 10px;
  border: 1px solid #ccc;
  border-radius: 25px;
  font-size: 14px;
  transition: border-color 0.3s;
}

.chatbot-footer input:focus {
  border-color: #007bff;
  outline: none;
}

.chatbot-footer .send-btn {
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 25px;
  padding: 8px 15px;
  margin-left: 10px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.chatbot-footer .send-btn:hover {
  background-color: #0056b3;
}
</style>
