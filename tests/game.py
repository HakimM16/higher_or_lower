import pathlib

from dealer import Dealer
from player import Player
from cpu import CPU


RULES_PATH = pathlib.Path(__file__).with_name("rules.md")


class Game:
    def __init__(self, dealer):
        self.dealer = dealer
        self.player = Player()
        self.cpu = CPU()

    def play_round(self):
        if self.dealer.rounds_played >= self.dealer.max_rounds:
            print("⏱️ Maximum rounds reached. Game over.")
            return False

        print(f"🃏 Current card: {self.dealer.display_current_card()}")
        player_guess = self._prompt_player_guess()

        cpu_guess = self.cpu.make_guess()
        print(f"🤖 CPU guesses: {cpu_guess}")

        next_card = self.dealer.draw_next_card()
        print(f"✨ Next card: {next_card.rank} of {next_card.suit} {next_card.suit_val}")

        player_correct = self.dealer.evaluate_guess(player_guess, next_card)
        cpu_correct = self.dealer.evaluate_guess(cpu_guess, next_card)

        self._handle_result("Player", player_correct, self.player, next_card)
        self._handle_result("CPU", cpu_correct, self.cpu, next_card)

        self.dealer.update_current_card(next_card)
        self.dealer.rounds_played += 1

        print(f"📊 Scores ⇒ Player: {self.player.get_score()} | CPU: {self.cpu.get_score()}")
        print("-" * 30)
        return True

    def _prompt_player_guess(self):
        while True:
            try:
                guess = input("🔮 Will the next card be higher or lower? ").strip().lower()
                return self.player.make_guess(guess)
            except ValueError:
                print("⚠️ Please type 'higher' or 'lower'.")

    def _handle_result(self, label, is_correct, participant, next_card):
        if is_correct:
            participant.increment_score()
            print(f"✅ {label} guessed correctly!")
        else:
            print(f"❌ {label} guessed incorrectly.")
            if self._joker_triggered(next_card):
                participant.reset_score()
                print(f"🃏 Joker penalty! {label}'s score resets to 0.")

    @staticmethod
    def _joker_triggered(next_card):
        # Any revealed Jack resets the score
        return next_card.rank == 'J'

    def display_winner(self):
        player_score = self.player.get_score()
        cpu_score = self.cpu.get_score()
        print(f"🏁 Final Scores ⇒ Player: {player_score}, CPU: {cpu_score}")
        if player_score > cpu_score:
            print("🎉 Player wins!")
        elif cpu_score > player_score:
            print("🤖 CPU wins this time!")
        else:
            print("🤝 It's a tie!")

    def start_game(self):
        print("🎮 Starting Higher or Lower!")
        round_counter = 0
        while self.play_round():
            round_counter += 1
            print(f"✅ Round {round_counter} completed.")
        self.display_winner()


def choose_rounds():
    while True:
        choice = input("🔁 How many rounds would you like to play? ").strip()
        if choice.isdigit() and int(choice) > 0:
            return int(choice)
        print("⚠️ Please enter a positive number.")


def show_rules():
    print("📖 Game Rules:")
    try:
        # Keep a single source of truth by reading the markdown directly
        print(RULES_PATH.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print("Rules file not found. Please ensure 'rules.md' exists.")


def show_menu():
    while True:
        print("\n=== 🎴 Higher or Lower Menu ===")
        print("1. ▶️ Play Game")
        print("2. 📘 View Rules")
        print("3. 🚪 Exit")
        selection = input("Select an option (1-3): ").strip()

        if selection == "1":
            rounds = choose_rounds()
            dealer = Dealer(max_rounds=rounds)
            game = Game(dealer)
            game.start_game()
        elif selection == "2":
            show_rules()
        elif selection == "3":
            print("👋 Thanks for playing!")
            break
        else:
            print("⚠️ Invalid option. Choose 1, 2, or 3.")


if __name__ == "__main__":
    show_menu()