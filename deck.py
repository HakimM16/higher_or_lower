import random
from card import Card

class Deck():
    # Initialize the deck with 10 unique cards
    # Each card is represented as a tuple (suit, rank)
    # Example: ('♠', 'Ace')

    def __init__(self):
        self.deck = self.create_deck()

    def create_deck(self):
        # Create a standard deck of 10 cards to represent 10 rounds
        deck = []
        for _ in range(10):
            card = Card()
            # Check for duplicates before adding
            while card.val in deck:
                card = Card()
            deck.append(card.val)
        return deck


    def shuffle(self):
        # shuffle the deck using random.shuffle
        random.shuffle(self.deck)