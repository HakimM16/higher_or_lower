# This will the player class for the Higher or Lower game
class Player:
    def __init__(self):
        self.score = 0

    def make_guess(self, guess):
        # guess should be either "higher" or "lower"
        if guess.lower() in ["higher", "lower"]:
            return guess.lower()
        else:
            raise ValueError("Guess must be 'higher' or 'lower'")

    def increment_score(self):
        self.score += 1

    def reset_score(self):
        # Used when Joker penalty triggers and wipes the current score
        self.score = 0

    def get_score(self):
        return self.score