import unittest
from deck import Deck
from card import Card


class TestDeck(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.deck = Deck()

    def test_deck_initialization(self):
        """Test that a deck is initialized and built."""
        self.assertIsNotNone(self.deck.deck)
        self.assertIsInstance(self.deck.deck, list)

    def test_deck_size(self):
        """Test that a new deck has 52 cards."""
        self.assertEqual(len(self.deck.deck), 52)

    def test_build_deck_creates_all_cards(self):
        """Test that build_deck creates all 52 unique cards."""
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        
        # Count unique card combinations
        card_set = set()
        for card in self.deck.deck:
            card_set.add((card.suit, card.rank))
        
        self.assertEqual(len(card_set), 52)
        
        # Verify all suits and ranks are present
        suits_in_deck = {card.suit for card in self.deck.deck}
        ranks_in_deck = {card.rank for card in self.deck.deck}
        
        self.assertEqual(suits_in_deck, set(suits))
        self.assertEqual(ranks_in_deck, set(ranks))

    def test_deal_card_returns_card(self):
        """Test that deal_card returns a Card object."""
        card = self.deck.deal_card()
        self.assertIsInstance(card, Card)

    def test_deal_card_removes_from_deck(self):
        """Test that dealing a card removes it from the deck."""
        initial_size = len(self.deck.deck)
        self.deck.deal_card()
        self.assertEqual(len(self.deck.deck), initial_size - 1)

    def test_deal_all_cards(self):
        """Test that we can deal all 52 cards."""
        cards_dealt = []
        for _ in range(52):
            cards_dealt.append(self.deck.deal_card())
        
        self.assertEqual(len(cards_dealt), 52)
        self.assertEqual(len(self.deck.deck), 0)

    def test_deal_card_empty_deck_raises_error(self):
        """Test that dealing from an empty deck raises ValueError."""
        # Deal all cards
        for _ in range(52):
            self.deck.deal_card()
        
        # Try to deal from empty deck
        with self.assertRaises(ValueError) as context:
            self.deck.deal_card()
        
        self.assertIn("No more cards in the deck", str(context.exception))

    def test_shuffle_changes_order(self):
        """Test that shuffle changes the order of cards."""
        # Create two decks with same seed won't work, so we'll save original order
        original_order = [(card.suit, card.rank) for card in self.deck.deck]
        
        # Shuffle multiple times to ensure it changes
        self.deck.shuffle()
        new_order = [(card.suit, card.rank) for card in self.deck.deck]
        
        # It's extremely unlikely they'll be the same after shuffling
        # (1 in 52! chance)
        self.assertNotEqual(original_order, new_order)

    def test_shuffle_maintains_deck_size(self):
        """Test that shuffling doesn't change the number of cards."""
        self.deck.shuffle()
        self.assertEqual(len(self.deck.deck), 52)

    def test_shuffle_maintains_all_cards(self):
        """Test that shuffling doesn't lose or duplicate cards."""
        original_cards = set((card.suit, card.rank) for card in self.deck.deck)
        self.deck.shuffle()
        shuffled_cards = set((card.suit, card.rank) for card in self.deck.deck)
        
        self.assertEqual(original_cards, shuffled_cards)


if __name__ == '__main__':
    unittest.main()
