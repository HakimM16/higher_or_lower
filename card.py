import random

class Card():
    def __init__(self):
        self.val = self.generate_card()

    def generate_card(self):
        ranks = ["Ace", "1", "2", "3", "4", "5", "6", 
                   "7", "8", "9", "10", "Jack", "Queen", "King"]
        suits = ["♠", "♥", "♦", "♣"]
        
        random_rank = random.randint(0, len(ranks) - 1)
        random_suit = random.randint(0, len(suits) - 1)

        rank = ranks[random_rank]
        suit = suits[random_suit]

        # Card will be always be stored in a tuple with a suit and rank
        card = (suit, rank)

        return card
    
    