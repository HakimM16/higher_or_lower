import unittest
from unittest.mock import Mock, patch, MagicMock
from io import StringIO
from game import Game, choose_rounds, show_rules
from dealer import Dealer
from player import Player
from cpu import CPU
from card import Card


class TestGame(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.dealer = Dealer(max_rounds=3)
        self.game = Game(self.dealer)

    def test_game_initialization(self):
        """Test that game is initialized with dealer, player, and cpu."""
        self.assertIsInstance(self.game.dealer, Dealer)
        self.assertIsInstance(self.game.player, Player)
        self.assertIsInstance(self.game.cpu, CPU)

    def test_joker_triggered_with_jack(self):
        """Test that _joker_triggered returns True for Jack."""
        jack = Card("Hearts", "J")
        self.assertTrue(Game._joker_triggered(jack))

    def test_joker_triggered_with_other_cards(self):
        """Test that _joker_triggered returns False for non-Jack cards."""
        ace = Card("Hearts", "A")
        king = Card("Diamonds", "K")
        five = Card("Clubs", "5")
        
        self.assertFalse(Game._joker_triggered(ace))
        self.assertFalse(Game._joker_triggered(king))
        self.assertFalse(Game._joker_triggered(five))

    @patch('builtins.print')
    def test_display_winner_player_wins(self, mock_print):
        """Test display_winner when player has higher score."""
        self.game.player.score = 5
        self.game.cpu.score = 3
        
        self.game.display_winner()
        
        # Check that the correct messages were printed
        print_calls = [str(call) for call in mock_print.call_args_list]
        self.assertTrue(any("Player wins!" in str(call) for call in print_calls))

    @patch('builtins.print')
    def test_display_winner_cpu_wins(self, mock_print):
        """Test display_winner when CPU has higher score."""
        self.game.player.score = 2
        self.game.cpu.score = 7
        
        self.game.display_winner()
        
        print_calls = [str(call) for call in mock_print.call_args_list]
        self.assertTrue(any("CPU wins" in str(call) for call in print_calls))

    @patch('builtins.print')
    def test_display_winner_tie(self, mock_print):
        """Test display_winner when scores are equal."""
        self.game.player.score = 5
        self.game.cpu.score = 5
        
        self.game.display_winner()
        
        print_calls = [str(call) for call in mock_print.call_args_list]
        self.assertTrue(any("tie" in str(call).lower() for call in print_calls))

    @patch('builtins.print')
    @patch('builtins.input', return_value='higher')
    def test_play_round_increments_rounds_played(self, mock_input, mock_print):
        """Test that play_round increments rounds_played."""
        initial_rounds = self.dealer.rounds_played
        self.game.play_round()
        self.assertEqual(self.dealer.rounds_played, initial_rounds + 1)

    @patch('builtins.print')
    def test_play_round_returns_false_when_max_rounds_reached(self, mock_print):
        """Test that play_round returns False when max rounds reached."""
        self.dealer.rounds_played = self.dealer.max_rounds
        result = self.game.play_round()
        self.assertFalse(result)

    @patch('builtins.print')
    @patch('builtins.input', return_value='higher')
    def test_play_round_updates_current_card(self, mock_input, mock_print):
        """Test that play_round updates the dealer's current card."""
        old_card = self.dealer.current_card
        self.game.play_round()
        new_card = self.dealer.current_card
        
        # The current card should have changed
        self.assertIsNot(old_card, new_card)

    @patch('builtins.input', side_effect=['invalid', 'not a guess', 'higher'])
    @patch('builtins.print')
    def test_prompt_player_guess_retries_on_invalid_input(self, mock_print, mock_input):
        """Test that _prompt_player_guess retries on invalid input."""
        result = self.game._prompt_player_guess()
        
        self.assertEqual(result, 'higher')
        # Should have called input 3 times
        self.assertEqual(mock_input.call_count, 3)

    @patch('builtins.input', return_value='LOWER')
    def test_prompt_player_guess_case_insensitive(self, mock_input):
        """Test that _prompt_player_guess handles uppercase input."""
        result = self.game._prompt_player_guess()
        self.assertEqual(result, 'lower')

    @patch('builtins.print')
    def test_handle_result_correct_guess_increments_score(self, mock_print):
        """Test that _handle_result increments score for correct guess."""
        initial_score = self.game.player.get_score()
        next_card = Card("Hearts", "5")
        
        self.game._handle_result("Player", True, self.game.player, next_card)
        
        self.assertEqual(self.game.player.get_score(), initial_score + 1)

    @patch('builtins.print')
    def test_handle_result_incorrect_guess_no_increment(self, mock_print):
        """Test that _handle_result doesn't increment score for incorrect guess."""
        initial_score = self.game.player.get_score()
        next_card = Card("Hearts", "5")
        
        self.game._handle_result("Player", False, self.game.player, next_card)
        
        self.assertEqual(self.game.player.get_score(), initial_score)

    @patch('builtins.print')
    def test_handle_result_joker_resets_score(self, mock_print):
        """Test that _handle_result resets score on Joker."""
        self.game.player.increment_score()
        self.game.player.increment_score()
        self.game.player.increment_score()
        self.assertEqual(self.game.player.get_score(), 3)
        
        jack = Card("Hearts", "J")
        self.game._handle_result("Player", False, self.game.player, jack)
        
        self.assertEqual(self.game.player.get_score(), 0)

    @patch('builtins.print')
    def test_handle_result_no_joker_penalty_on_correct_guess(self, mock_print):
        """Test that Joker doesn't reset score if guess was correct."""
        self.game.player.increment_score()
        self.game.player.increment_score()
        initial_score = self.game.player.get_score()
        
        jack = Card("Hearts", "J")
        self.game._handle_result("Player", True, self.game.player, jack)
        
        # Score should increment, not reset
        self.assertEqual(self.game.player.get_score(), initial_score + 1)


class TestChooseRounds(unittest.TestCase):
    @patch('builtins.input', return_value='5')
    def test_choose_rounds_valid_input(self, mock_input):
        """Test choose_rounds with valid numeric input."""
        result = choose_rounds()
        self.assertEqual(result, 5)

    @patch('builtins.input', side_effect=['0', '-1', 'abc', '10'])
    @patch('builtins.print')
    def test_choose_rounds_retries_on_invalid_input(self, mock_print, mock_input):
        """Test choose_rounds retries on invalid input."""
        result = choose_rounds()
        self.assertEqual(result, 10)
        # Should have called input 4 times
        self.assertEqual(mock_input.call_count, 4)

    @patch('builtins.input', return_value='100')
    def test_choose_rounds_large_number(self, mock_input):
        """Test choose_rounds accepts large valid numbers."""
        result = choose_rounds()
        self.assertEqual(result, 100)


class TestShowRules(unittest.TestCase):
    @patch('pathlib.Path.read_text')
    @patch('builtins.print')
    def test_show_rules_displays_rules(self, mock_print, mock_read):
        """Test show_rules displays the rules from file."""
        mock_read.return_value = "Game rules here"
        
        show_rules()
        
        mock_read.assert_called_once()
        # Check that print was called with the rules content
        self.assertTrue(any("Game rules here" in str(call) for call in mock_print.call_args_list))

    @patch('pathlib.Path.read_text', side_effect=FileNotFoundError)
    @patch('builtins.print')
    def test_show_rules_handles_missing_file(self, mock_print, mock_read):
        """Test show_rules handles missing rules file gracefully."""
        # Should not raise an exception
        try:
            show_rules()
        except FileNotFoundError:
            self.fail("show_rules() raised FileNotFoundError unexpectedly")


if __name__ == '__main__':
    unittest.main()
