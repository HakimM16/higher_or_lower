class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    @property
    def suit_val(self):
        # Map suit names to symbols
        suit_map = {
            "Hearts": "♥",            
            "Diamonds": "♦",
            "Clubs": "♣",            
            "Spades": "♠"
        }
        return suit_map.get(self.suit, "")
    
    @property
    def rank_val(self):
        # Map ranks to numerical values for comparison
        rank_map = {
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'J': 11,
            'Q': 12,
            'K': 13,
            'A': 14
        }
        return rank_map.get(self.rank, 0)

    
    