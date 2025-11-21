import unittest
from unittest.mock import Mock, patch
from dealer import Dealer
from card import Card
from deck import Deck


class TestDealer(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.dealer = Dealer(max_rounds=10)

    def test_dealer_initialization(self):
        """Test that dealer is initialized correctly."""
        self.assertEqual(self.dealer.rounds_played, 0)
        self.assertEqual(self.dealer.max_rounds, 10)
        self.assertIsInstance(self.dealer.deck, Deck)
        self.assertIsInstance(self.dealer.current_card, Card)

    def test_dealer_custom_max_rounds(self):
        """Test that dealer can be initialized with custom max_rounds."""
        dealer = Dealer(max_rounds=5)
        self.assertEqual(dealer.max_rounds, 5)

    def test_display_current_card(self):
        """Test that display_current_card returns formatted string."""
        result = self.dealer.display_current_card()
        self.assertIsInstance(result, str)
        self.assertIn("of", result)

    def test_display_current_card_contains_suit_and_rank(self):
        """Test that display includes both suit and rank."""
        # Set a known card
        self.dealer.current_card = Card("Hearts", "A")
        result = self.dealer.display_current_card()
        
        self.assertIn("A", result)
        self.assertIn("Hearts", result)

    def test_draw_next_card_returns_card(self):
        """Test that draw_next_card returns a Card object."""
        card = self.dealer.draw_next_card()
        self.assertIsInstance(card, Card)

    def test_update_current_card(self):
        """Test that update_current_card changes the current card."""
        new_card = Card("Spades", "K")
        self.dealer.update_current_card(new_card)
        self.assertEqual(self.dealer.current_card, new_card)

    def test_evaluate_guess_higher_correct(self):
        """Test evaluate_guess returns True for correct 'higher' guess."""
        self.dealer.current_card = Card("Hearts", "5")
        next_card = Card("Diamonds", "10")
        
        result = self.dealer.evaluate_guess("higher", next_card)
        self.assertTrue(result)

    def test_evaluate_guess_higher_incorrect(self):
        """Test evaluate_guess returns False for incorrect 'higher' guess."""
        self.dealer.current_card = Card("Hearts", "10")
        next_card = Card("Diamonds", "5")
        
        result = self.dealer.evaluate_guess("higher", next_card)
        self.assertFalse(result)

    def test_evaluate_guess_lower_correct(self):
        """Test evaluate_guess returns True for correct 'lower' guess."""
        self.dealer.current_card = Card("Hearts", "10")
        next_card = Card("Diamonds", "5")
        
        result = self.dealer.evaluate_guess("lower", next_card)
        self.assertTrue(result)

    def test_evaluate_guess_lower_incorrect(self):
        """Test evaluate_guess returns False for incorrect 'lower' guess."""
        self.dealer.current_card = Card("Hearts", "5")
        next_card = Card("Diamonds", "10")
        
        result = self.dealer.evaluate_guess("lower", next_card)
        self.assertFalse(result)

    def test_evaluate_guess_same_value_returns_false(self):
        """Test evaluate_guess returns False when cards have same value."""
        self.dealer.current_card = Card("Hearts", "7")
        next_card = Card("Diamonds", "7")
        
        result_higher = self.dealer.evaluate_guess("higher", next_card)
        result_lower = self.dealer.evaluate_guess("lower", next_card)
        
        self.assertFalse(result_higher)
        self.assertFalse(result_lower)

    def test_effective_rank_regular_cards(self):
        """Test _effective_rank for regular number cards."""
        card_5 = Card("Hearts", "5")
        card_10 = Card("Diamonds", "10")
        
        self.assertEqual(self.dealer._effective_rank(card_5), 5)
        self.assertEqual(self.dealer._effective_rank(card_10), 10)

    def test_effective_rank_face_cards(self):
        """Test _effective_rank for face cards."""
        jack = Card("Hearts", "J")
        queen = Card("Diamonds", "Q")
        king = Card("Clubs", "K")
        
        self.assertEqual(self.dealer._effective_rank(jack), 11)
        self.assertEqual(self.dealer._effective_rank(queen), 12)
        self.assertEqual(self.dealer._effective_rank(king), 13)

    def test_effective_rank_ace_high(self):
        """Test _effective_rank for Ace when it should be high."""
        ace = Card("Hearts", "A")
        reference_card = Card("Diamonds", "5")
        
        result = self.dealer._effective_rank(ace, reference_card=reference_card)
        self.assertEqual(result, 14)

    def test_effective_rank_ace_low_after_face_cards(self):
        """Test _effective_rank for Ace when it should be low (after face cards)."""
        ace = Card("Hearts", "A")
        
        # Test after Jack
        jack = Card("Diamonds", "J")
        result_jack = self.dealer._effective_rank(ace, reference_card=jack)
        self.assertEqual(result_jack, 1)
        
        # Test after Queen
        queen = Card("Diamonds", "Q")
        result_queen = self.dealer._effective_rank(ace, reference_card=queen)
        self.assertEqual(result_queen, 1)
        
        # Test after King
        king = Card("Diamonds", "K")
        result_king = self.dealer._effective_rank(ace, reference_card=king)
        self.assertEqual(result_king, 1)

    def test_evaluate_guess_ace_after_face_card(self):
        """Test that Ace is treated as low (1) after face cards."""
        self.dealer.current_card = Card("Hearts", "K")  # King = 13
        next_card = Card("Diamonds", "A")  # Ace should be 1 after King
        
        # Guessing lower should be correct (Ace=1 < King=13)
        result = self.dealer.evaluate_guess("lower", next_card)
        self.assertTrue(result)

    def test_evaluate_guess_ace_after_number_card(self):
        """Test that Ace is treated as high (14) after number cards."""
        self.dealer.current_card = Card("Hearts", "7")  # 7
        next_card = Card("Diamonds", "A")  # Ace should be 14 after 7
        
        # Guessing higher should be correct (Ace=14 > 7)
        result = self.dealer.evaluate_guess("higher", next_card)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
