# Rasa-Chatbot

<img width="1757" alt="Bildschirmfoto 2024-10-11 um 22 29 32" src="https://github.com/user-attachments/assets/e3d1ba7e-c271-4217-98e6-f467cb4b9c7b">

It seems like there was an issue with the image you tried to share. However, I can help you extend your README for the Rasa chatbot you're about to publish.

Here’s a basic structure to follow, which we can expand further based on the specifics of your chatbot project.

---

# Rasa Chatbot

## Introduction
This project is a Rasa-based chatbot designed for [purpose of your chatbot, e.g., handling user queries related to funding options for international students at DIT]. It uses story-based dialogue management and employs a modular structure to manage user interactions efficiently.

## Features
- **Modular Structure**: The bot is built with a modular story design, using checkpoints for essential tasks such as greetings, coin selection, and transactions.
- **Customizable Stories**: Includes predefined stories for typical use cases, and easily extendable to handle additional conversation flows.
- **Rasa Core & NLU**: The chatbot uses Rasa Core for dialogue management and Rasa NLU for understanding intents and extracting entities.

## Prerequisites
Before running the chatbot, ensure you have the following installed:
- [Rasa](https://rasa.com/docs/rasa/)
- Docker (optional, for containerized setup)
- Python 3.8 or later
- PostgreSQL (if used in combination with database integration)

To install Rasa:
```bash
pip install rasa
```

## Setup
1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd [project-folder]
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Train the chatbot:
   ```bash
   rasa train
   ```
4. Run the chatbot:
   ```bash
   rasa run
   ```

## How It Works

### 1. **Story Flow**
The bot uses a story-based framework to manage the conversation. Key stories include:
- **Greetings**: Initiates conversation with a welcome message.
- **Coin Selection**: Guides the user through selecting coins in a transaction flow.
- **Transactions**: Handles user transactions and confirmations.
  
Stories are organized using checkpoints to allow flexible transitions between conversation paths.

### 2. **Domain**
The domain file (`domain.yml`) defines the intents, entities, actions, and responses. Example intents:
- `greet`: For greeting the user.
- `coin_selection`: For selecting coins.
- `transaction`: For handling transactions.

### 3. **Custom Actions**
Custom actions are defined in the `actions.py` file. These handle backend logic, such as querying a database, calculating values, or processing transactions.

### 4. **NLU Model**
The NLU model is trained to understand user intents and extract relevant entities from user inputs. It uses intents like `greet`, `coin_selection`, and `transaction` to manage dialogue flow.

## Usage
After setting up, you can start interacting with the chatbot:
```bash
rasa shell
```

You can also test your stories using:
```bash
rasa test
```

## Deployment
You can deploy the chatbot using Docker or any cloud service. Follow these steps for Docker deployment:
1. Build the Docker image:
   ```bash
   docker build -t rasa-chatbot .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 5005:5005 rasa-chatbot
   ```

## Future Enhancements
- **Multi-language support**: Extend the bot to handle multiple languages.
- **Integration with APIs**: Connect the chatbot to external APIs for more dynamic content.
- **Improved NLU**: Enhance the NLU model to handle a broader set of user queries.

## Contributing
Feel free to open issues or submit pull requests to improve the chatbot.

---

Let me know if you need to adjust or add any other sections.
