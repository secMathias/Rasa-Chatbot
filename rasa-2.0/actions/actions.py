from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import difflib

# Mock data: Initial balance for users and coin prices
USER_DATA = {}
COIN_PRICES = {
    "Bitcoin": 50000.0,  # Price per 1 Bitcoin in USD
    "Ethereum": 4000.0,  # Price per 1 Ethereum in USD
    "Solaris": 100.0     # Price per 1 Solaris in USD
}

def get_user_data(sender_id):
    """Retrieve or initialize user data based on sender_id."""
    if sender_id not in USER_DATA:
        USER_DATA[sender_id] = {
            "balance": 1000000.0,  # Let's assume the user starts with $1000000
            "Bitcoin": 0.0,
            "Ethereum": 0.0,
            "Solaris": 0.0
        }
    return USER_DATA[sender_id]

def get_closest_match(user_input, valid_options):
    """Find the closest match to the user input from the list of valid options."""
    matches = difflib.get_close_matches(user_input, valid_options, n=1, cutoff=0.6)
    return matches[0] if matches else None

class ActionBuyCrypto(Action):
    def name(self):
        return "action_buy_crypto"

    def run(self, dispatcher, tracker, domain):
        sender_id = tracker.sender_id

        user_data = get_user_data(sender_id)
        balance = user_data["balance"]
        coin_type = tracker.get_slot("coin_type")
        amount = tracker.get_slot("amount")

        if not coin_type:
            dispatcher.utter_message(text="Please specify the coin type you want to buy.")
            return []
        
        if not amount:
            dispatcher.utter_message(text="Please specify the amount of cryptocurrency you want to buy.")
            return []

        # Get closest match for the coin type
        coin_type = get_closest_match(coin_type, COIN_PRICES.keys())
        if not coin_type:
            dispatcher.utter_message(text="Sorry, we couldn't find a matching cryptocurrency.")
            return []

        try:
            amount = float(amount)
        except ValueError:
            dispatcher.utter_message(text="The amount should be a valid number.")
            return []

        # Calculate the cost of the transaction
        coin_price = COIN_PRICES[coin_type]
        total_cost = amount * coin_price

        if total_cost > balance:
            dispatcher.utter_message(text=f"Insufficient balance. You need ${total_cost:.2f}, but you only have ${balance:.2f}.")
            return []

        # Update balance and coin amount
        user_data["balance"] -= total_cost
        user_data[coin_type] += amount

        dispatcher.utter_message(text=f"You have successfully bought {amount} of {coin_type}. Your new balance is ${user_data['balance']:.2f}.")
        
        return [SlotSet(coin_type, user_data[coin_type]), SlotSet("balance", user_data["balance"])]


class ActionSellCrypto(Action):
    def name(self):
        return "action_sell_crypto"

    def run(self, dispatcher, tracker, domain):
        # Get sender_id and retrieve user-specific data
        sender_id = tracker.sender_id
        print(f"Sender ID: {sender_id}")  # Print the sender_id for debugging

        user_data = get_user_data(sender_id)
        balance = user_data["balance"]
        coin_type = tracker.get_slot("coin_type")
        amount = tracker.get_slot("amount")

        if not coin_type:
            dispatcher.utter_message(text="Please specify the coin type you want to sell.")
            return []
        
        if not amount:
            dispatcher.utter_message(text="Please specify the amount of cryptocurrency you want to sell.")
            return []

        # Get closest match for the coin type
        coin_type = get_closest_match(coin_type, COIN_PRICES.keys())
        if not coin_type:
            dispatcher.utter_message(text="Sorry, we couldn't find a matching cryptocurrency.")
            return []

        try:
            amount = float(amount)
        except ValueError:
            dispatcher.utter_message(text="The amount should be a valid number.")
            return []

        # Check if the user has enough of the coin to sell
        if amount > user_data[coin_type]:
            dispatcher.utter_message(text=f"Insufficient {coin_type}. You only have {user_data[coin_type]} available.")
            return []

        # Update balance and coin amount after selling
        coin_price = COIN_PRICES[coin_type]
        total_value = amount * coin_price
        user_data["balance"] += total_value
        user_data[coin_type] -= amount

        dispatcher.utter_message(text=f"You have successfully sold {amount} of {coin_type}. Your new balance is ${user_data['balance']:.2f}.")

        return [SlotSet(coin_type, user_data[coin_type]), SlotSet("balance", user_data["balance"])]


class ActionCheckBitcoin(Action):
    def name(self):
        return "action_check_bitcoin"

    def run(self, dispatcher, tracker, domain):
        sender_id = tracker.sender_id
        user_data = get_user_data(sender_id)
        bitcoin = user_data["Bitcoin"]
        message = f"You currently have {bitcoin} Bitcoin."
        dispatcher.utter_message(text=message)
        return []


class ActionCheckEthereum(Action):
    def name(self):
        return "action_check_ethereum"

    def run(self, dispatcher, tracker, domain):
        sender_id = tracker.sender_id
        user_data = get_user_data(sender_id)
        ethereum = user_data["Ethereum"]
        message = f"You currently have {ethereum} Ethereum."
        dispatcher.utter_message(text=message)
        return []


class ActionCheckSolaris(Action):
    def name(self):
        return "action_check_solaris"

    def run(self, dispatcher, tracker, domain):
        sender_id = tracker.sender_id
        user_data = get_user_data(sender_id)
        solaris = user_data["Solaris"]
        message = f"You currently have {solaris} Solaris."
        dispatcher.utter_message(text=message)
        return []


class ActionCheckBalance(Action):
    def name(self):
        return "action_check_balance"

    def run(self, dispatcher, tracker, domain):
        sender_id = tracker.sender_id
        user_data = get_user_data(sender_id)
        balance = user_data["balance"]
        dispatcher.utter_message(text=f"Your current balance is ${balance:.2f}.")
        return []
