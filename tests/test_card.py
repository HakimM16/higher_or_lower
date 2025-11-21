import unittest
from card import Card


class TestCard(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.heart_card = Card("Hearts", "A")
        self.diamond_card = Card("Diamonds", "K")
        self.club_card = Card("Clubs", "10")
        self.spade_card = Card("Spades", "J")

    def test_card_initialization(self):
        """Test that a card is initialized with correct suit and rank."""
        self.assertEqual(self.heart_card.suit, "Hearts")
        self.assertEqual(self.heart_card.rank, "A")

    def test_suit_val_hearts(self):
        """Test that Hearts returns correct symbol."""
        self.assertEqual(self.heart_card.suit_val, "♥")

    def test_suit_val_diamonds(self):
        """Test that Diamonds returns correct symbol."""
        self.assertEqual(self.diamond_card.suit_val, "♦")

    def test_suit_val_clubs(self):
        """Test that Clubs returns correct symbol."""
        self.assertEqual(self.club_card.suit_val, "♣")

    def test_suit_val_spades(self):
        """Test that Spades returns correct symbol."""
        self.assertEqual(self.spade_card.suit_val, "♠")

    def test_suit_val_invalid(self):
        """Test that invalid suit returns empty string."""
        invalid_card = Card("Invalid", "A")
        self.assertEqual(invalid_card.suit_val, "")

    def test_rank_val_number_cards(self):
        """Test rank values for number cards."""
        card_2 = Card("Hearts", "2")
        card_5 = Card("Hearts", "5")
        card_10 = Card("Hearts", "10")
        
        self.assertEqual(card_2.rank_val, 2)
        self.assertEqual(card_5.rank_val, 5)
        self.assertEqual(card_10.rank_val, 10)

    def test_rank_val_face_cards(self):
        """Test rank values for face cards."""
        jack = Card("Hearts", "J")
        queen = Card("Hearts", "Q")
        king = Card("Hearts", "K")
        
        self.assertEqual(jack.rank_val, 11)
        self.assertEqual(queen.rank_val, 12)
        self.assertEqual(king.rank_val, 13)

    def test_rank_val_ace(self):
        """Test rank value for Ace."""
        self.assertEqual(self.heart_card.rank_val, 14)

    def test_rank_val_invalid(self):
        """Test that invalid rank returns 0."""
        invalid_card = Card("Hearts", "X")
        self.assertEqual(invalid_card.rank_val, 0)


if __name__ == '__main__':
    unittest.main()
