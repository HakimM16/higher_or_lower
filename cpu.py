# This will be the CPU class for the Higher or Lower game
import random

class CPU:
    def __init__(self):
        self.score = 0

    def make_guess(self):
        # CPU randomly guesses "higher" or "lower"
        return random.choice(["higher", "lower"])
    
    def increment_score(self):
        self.score += 1

    def get_score(self):
        return self.score