from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import difflib

# Mock data: user balance and coin prices
USER_BALANCE = 1000000.0  # Let's assume the user has $1000 to spend
COIN_PRICES = {
    "Bitcoin": 50000.0,  # Price per 1 Bitcoin in USD
    "Ethereum": 4000.0,  # Price per 1 Ethereum in USD
    "Solaris": 100.0     # Price per 1 Solaris in USD
}

def get_closest_match(user_input, valid_options):
    """Find the closest match to the user input from the list of valid options."""
    matches = difflib.get_close_matches(user_input, valid_options, n=1, cutoff=0.6)
    return matches[0] if matches else None

class ActionBuyCrypto(Action):
    def name(self):
        return "action_buy_crypto"

    def run(self, dispatcher, tracker, domain):
        coin_type = tracker.get_slot("coin_type")
        amount = tracker.get_slot("amount")
        user_balance = tracker.get_slot("balance") or USER_BALANCE

        # Check if both coin type and amount are provided
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

        # Convert the amount to a float and handle invalid input
        try:
            amount = float(amount)
        except ValueError:
            dispatcher.utter_message(text="The amount should be a valid number.")
            return []

        # Calculate the cost of the transaction
        coin_price = COIN_PRICES[coin_type]
        total_cost = amount * coin_price

        # Check if the user has enough balance
        if total_cost > user_balance:
            dispatcher.utter_message(text=f"Insufficient balance. You need ${total_cost:.2f}, but you only have ${user_balance:.2f}.")
            return []

        # Simulate successful purchase
        new_balance = user_balance - total_cost
        current_coin_amount = tracker.get_slot(coin_type) or 0.0
        new_coin_amount = current_coin_amount + amount

        dispatcher.utter_message(text=f"You have successfully bought {amount} of {coin_type}. Your new balance is ${new_balance:.2f}.")
        
        return [SlotSet(coin_type, new_coin_amount), SlotSet("balance", new_balance)]


class ActionSellCrypto(Action):
    def name(self):
        return "action_sell_crypto"

    def run(self, dispatcher, tracker, domain):
        coin_type = tracker.get_slot("coin_type")
        amount = tracker.get_slot("amount")
        balance = tracker.get_slot("balance") or USER_BALANCE

        # Check if both coin type and amount are provided
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

        # Convert the amount to a float and handle invalid input
        try:
            amount = float(amount)
        except ValueError:
            dispatcher.utter_message(text="The amount should be a valid number.")
            return []

        # Get the current coin amount from the slot
        current_coin_amount = tracker.get_slot(coin_type) or 0.0

        # Check if the user has enough of the coin to sell
        if amount > current_coin_amount:
            dispatcher.utter_message(text=f"Insufficient {coin_type}. You only have {current_coin_amount} available.")
            return []

        # Simulate successful sale
        coin_price = COIN_PRICES[coin_type]
        total_value = amount * coin_price
        new_balance = balance + total_value
        new_coin_amount = current_coin_amount - amount

        dispatcher.utter_message(text=f"You have successfully sold {amount} of {coin_type}. Your new balance is ${new_balance:.2f}.")

        return [SlotSet(coin_type, new_coin_amount), SlotSet("balance", new_balance)]


class ActionCheckBitcoin(Action):
    def name(self):
        return "action_check_bitcoin"

    def run(self, dispatcher, tracker, domain):
        bitcoin = tracker.get_slot("Bitcoin") or 0.0
        message = f"You currently have {bitcoin} Bitcoin."
        dispatcher.utter_message(text=message)
        return []


class ActionCheckEthereum(Action):
    def name(self):
        return "action_check_ethereum"

    def run(self, dispatcher, tracker, domain):
        ethereum = tracker.get_slot("Ethereum") or 0.0
        message = f"You currently have {ethereum} Ethereum."
        dispatcher.utter_message(text=message)
        return []


class ActionCheckSolaris(Action):
    def name(self):
        return "action_check_solaris"

    def run(self, dispatcher, tracker, domain):
        solaris = tracker.get_slot("Solaris") or 0.0
        message = f"You currently have {solaris} Solaris."
        dispatcher.utter_message(text=message)
        return []


class ActionCheckBalance(Action):
    def name(self):
        return "action_check_balance"

    def run(self, dispatcher, tracker, domain):
        balance = tracker.get_slot("balance") or USER_BALANCE
        dispatcher.utter_message(text=f"Your current balance is ${balance:.2f}.")
        return []
