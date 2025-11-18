# the dealer class for the Higher or Lower game
from deck import Deck

class Dealer:
    def __init__(self):
        self.rounds_played = 0
        self.max_rounds = 10
        self.deck = Deck()
        self.current_card = self.deck.deal_card()

    def display_current_card(self):
        return f"{self.current_card.rank} of {self.current_card.suit}."
    
    def set_new_card(self):
        self.current_card = self.deck.deal_card()

    def compare_cards(self, guess):
        # Deal a new card and compare it with the current card
        new_card = self.deck.deal_card()
        old_card = self.current_card
        # check if new card is higher or lower
        if guess == "higher":
            result = new_card.rank_val > old_card.rank_val
        else:  # guess == "lower"
            result = new_card.rank_val < old_card.rank_val
        self.current_card = new_card
        return result

