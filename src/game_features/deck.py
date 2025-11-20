import random
from game_features.card import Card

class Deck():
    # Initialize the deck with 10 unique cards
    # Each card is represented as a tuple (suit, rank)
    # Example: ('♠', 'Ace')

    def __init__(self):
        self.deck = [] # acts as a stack
        self.build_deck()

    def build_deck(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.deck = [Card(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(self.deck)

    def shuffle(self):
        # shuffle the deck using random.shuffle
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card from the top of the deck
        if len(self.deck) == 0:
            raise ValueError("No more cards in the deck")
        return self.deck.pop()