# the dealer class for the Higher or Lower game
from deck import Deck

class Dealer:
    def __init__(self, max_rounds=10):
        self.rounds_played = 0
        self.max_rounds = max_rounds
        self.deck = Deck()
        self.current_card = self.deck.deal_card()

    def display_current_card(self):
        suit_icon = self.current_card.suit_val
        icon = f" {suit_icon}" if suit_icon else ""
        return f"{self.current_card.rank} of {self.current_card.suit}{icon}"

    def draw_next_card(self):
        # Central draw helper so both player and CPU react to the same card
        return self.deck.deal_card()

    def update_current_card(self, new_card):
        self.current_card = new_card

    def evaluate_guess(self, guess, next_card):
        old_card = self.current_card
        old_value = self._effective_rank(old_card)
        next_value = self._effective_rank(next_card, reference_card=old_card)

        if next_value == old_value:
            return False

        if guess == "higher":
            return next_value > old_value
        return next_value < old_value

    def _effective_rank(self, card, reference_card=None):
        if card.rank == 'A' and reference_card is not None:
            # Ace behaves like described in notes: low after face cards, high otherwise
            if reference_card.rank in ('J', 'Q', 'K'):
                return 1
            return 14
        return card.rank_val