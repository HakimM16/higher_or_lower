from dealer import Dealer
from player import Player
from cpu import CPU

class Game:
    def __init__(self, dealer):
        self.dealer = dealer
        self.player = Player()
        self.cpu = CPU()

    def play_round(self):
        # Check if maximum rounds reached
        if self.dealer.rounds_played >= self.dealer.max_rounds:
            print("Maximum rounds reached. Game over.")
            return False

        print(f"Current card is: {self.dealer.display_current_card()}")
        
        # Player makes a guess
        player_guess = input("Will the next card be higher or lower? ").strip().lower()
        player_guess = self.player.make_guess(player_guess)
        
        # CPU makes a guess
        cpu_guess = self.cpu.make_guess()
        print(f"CPU guesses: {cpu_guess}")
        
        # Compare player's guess
        if self.dealer.compare_cards(player_guess):
            print("Player guessed correctly!")
            self.player.increment_score()
        else:
            print("Player guessed incorrectly.")
        
        # Compare CPU's guess
        if self.dealer.compare_cards(cpu_guess):
            print("CPU guessed correctly!")
            self.cpu.increment_score()
        else:
            print("CPU guessed incorrectly.")

        # set new card for next round
        self.dealer.set_new_card()
        print(f"The new card is: {self.dealer.display_current_card()}")
        print(f"Scores => Player: {self.player.get_score()}, CPU: {self.cpu.get_score()}")
        print("-" * 30)

        # increment rounds played
        self.dealer.rounds_played += 1
        return True
    
    def display_winner(self):
        player_score = self.player.get_score()
        cpu_score = self.cpu.get_score()
        print(f"Final Scores => Player: {player_score}, CPU: {cpu_score}")
        if player_score > cpu_score:
            print("Player wins!")
        elif cpu_score > player_score:
            print("CPU wins!")
        else:
            print("It's a tie!")

    def start_game(self):
        print("Starting Higher or Lower Game!")
        num_of_round = 0
        while self.play_round():
            print(f"Round {num_of_round + 1} completed.")
            num_of_round += 1
        self.display_winner()

if __name__ == "__main__":
    dealer = Dealer()
    game = Game(dealer)
    game.start_game()