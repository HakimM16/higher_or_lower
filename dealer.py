# the dealer class for the Higher or Lower game
from deck import Deck

class Dealer:
    def __init__(self):
        self.rounds_played = 0
        self.max_rounds = 10
        self.deck = Deck()

    def show_current_card(self, card):
        # card is a tuple (suit, rank)
        suit, rank = card
        return f"Current card is: {rank} of {suit}"
    
    def show_next_card(self, card):
        # card is a tuple (suit, rank)
        suit, rank = card
        return f"Next card is: {rank} of {suit}"