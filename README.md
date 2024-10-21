# **Elite Crypto Broker Assistant - Rasa Chatbot**

<img width="1757" alt="Bildschirmfoto 2024-10-11 um 22 29 32" src="https://github.com/user-attachments/assets/e3d1ba7e-c271-4217-98e6-f467cb4b9c7b">

---

## **Introduction**

This project is a Rasa-based chatbot built to assist users in getting started with **Elite Crypto Broker**. The bot is designed to streamline common tasks such as selecting cryptocurrencies, making transactions, and checking account balances. With a story-based dialogue system and modular architecture, it ensures flexibility and scalability in handling user interactions.

## **Features**

- **Modular Structure**: The chatbot is constructed using a modular story design, leveraging checkpoints for key interactions like greetings, coin selection, and transactions.
- **Customizable Stories**: The bot comes with predefined stories for common user scenarios and can be easily extended to support additional conversation flows.
- **Rasa Core & NLU**: Built on Rasa Core for dialogue management and Rasa NLU for understanding user intents and extracting relevant entities like cryptocurrencies and amounts.
  
## **Prerequisites**

Before running the chatbot, make sure you have the following installed:

- **Rasa** (latest version)
- **Python 3.10 or later**

To install Rasa, run the following command:

```bash
pip install rasa
```

## **Setup**

1. **Clone the repository**:
   ```bash
   git clone [repository-url]
   cd [project-folder]
   ```

2. **Install dependencies**:
   ```bash
   pip install rasa
   ```

3. **Train the chatbot**:
   ```bash
   rasa train
   ```

4. **Run the chatbot**:
   ```bash
   rasa run --enable-api --cors="*" --port 5005
   ```

## **How It Works**

### 1. **Story Flow**

The chatbot uses a story-driven framework to manage conversations. Key stories include:

- **Greetings**: Welcomes the user with a friendly message.
- **Coin Selection**: Guides users through the process of selecting the right cryptocurrency for their needs.
- **Transactions**: Manages cryptocurrency transactions, including buying, selling, and confirming actions.

Each story is organized using **checkpoints**, allowing the bot to flexibly navigate conversation paths based on user inputs.

### 2. **Domain**

The `domain.yml` file defines the core components of the chatbot:
- **Intents**: User intentions, such as `greet`, `buy_coin`, and `sell_coin`.
- **Entities**: Extracted data points, like cryptocurrency names (e.g., Bitcoin, Ethereum).
- **Slots**: Store information about the conversation state (e.g., selected coin type, amount).
- **Responses**: Predefined replies triggered by specific user intents or actions.

### 3. **Custom Actions**

Custom logic is handled in the `actions.py` file. This includes tasks like:
- Querying databases for transaction data.
- Calculating values.
- Processing user transactions.

### 4. **NLU Model**

The **NLU model** is trained to understand user intents and extract entities from user inputs. It processes conversation aspects like:
- Recognizing a greeting (`greet` intent).
- Extracting the type of cryptocurrency (e.g., Bitcoin, Ethereum) in coin selection.
- Identifying the amount of cryptocurrency in a transaction.

## **Usage**

Once the chatbot is trained and running, you can start the action server by executing:

```bash
python3 -m rasa_sdk --actions actions
```

To test your stories and ensure the chatbot behaves as expected:

```bash
rasa test
```

## **Deployment**

You can deploy this chatbot using Docker or a cloud platform for wider access. Follow these steps to deploy with Docker:

1. **Build the Docker image**:
   ```bash
   docker build -t rasa-chatbot .
   ```

2. **Run the Docker container**:
   ```bash
   docker run -p 5005:5005 rasa-chatbot
   ```

## **Future Enhancements**

- **Multi-language Support**: Extend the bot to handle conversations in multiple languages.
- **API Integration**: Connect the chatbot to external APIs for real-time data, such as cryptocurrency price feeds or user portfolio tracking.
- **Enhanced NLU**: Improve the NLU model to cover a wider variety of user queries, enhancing the chatbot's accuracy and responsiveness.

## **Contributing**

We welcome contributions! Please feel free to open issues or submit pull requests to suggest new features or improve existing functionality.

---
