import unittest
from player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.player = Player()

    def test_player_initialization(self):
        """Test that a player is initialized with score 0."""
        self.assertEqual(self.player.score, 0)
        self.assertEqual(self.player.get_score(), 0)

    def test_make_guess_higher(self):
        """Test that make_guess accepts 'higher'."""
        result = self.player.make_guess("higher")
        self.assertEqual(result, "higher")

    def test_make_guess_lower(self):
        """Test that make_guess accepts 'lower'."""
        result = self.player.make_guess("lower")
        self.assertEqual(result, "lower")

    def test_make_guess_case_insensitive(self):
        """Test that make_guess is case insensitive."""
        self.assertEqual(self.player.make_guess("HIGHER"), "higher")
        self.assertEqual(self.player.make_guess("Lower"), "lower")
        self.assertEqual(self.player.make_guess("HiGhEr"), "higher")

    def test_make_guess_invalid_raises_error(self):
        """Test that make_guess raises ValueError for invalid input."""
        with self.assertRaises(ValueError) as context:
            self.player.make_guess("invalid")
        
        self.assertIn("Guess must be 'higher' or 'lower'", str(context.exception))

    def test_make_guess_empty_string_raises_error(self):
        """Test that make_guess raises ValueError for empty string."""
        with self.assertRaises(ValueError):
            self.player.make_guess("")

    def test_make_guess_number_raises_error(self):
        """Test that make_guess raises ValueError for numbers."""
        with self.assertRaises(ValueError):
            self.player.make_guess("123")

    def test_increment_score(self):
        """Test that increment_score increases score by 1."""
        self.player.increment_score()
        self.assertEqual(self.player.get_score(), 1)

    def test_increment_score_multiple_times(self):
        """Test that score increments correctly multiple times."""
        for i in range(5):
            self.player.increment_score()
        self.assertEqual(self.player.get_score(), 5)

    def test_reset_score(self):
        """Test that reset_score sets score to 0."""
        self.player.increment_score()
        self.player.increment_score()
        self.player.increment_score()
        self.assertEqual(self.player.get_score(), 3)
        
        self.player.reset_score()
        self.assertEqual(self.player.get_score(), 0)

    def test_reset_score_when_already_zero(self):
        """Test that reset_score works when score is already 0."""
        self.player.reset_score()
        self.assertEqual(self.player.get_score(), 0)

    def test_get_score_returns_correct_value(self):
        """Test that get_score returns the current score."""
        self.assertEqual(self.player.get_score(), 0)
        self.player.increment_score()
        self.assertEqual(self.player.get_score(), 1)
        self.player.increment_score()
        self.assertEqual(self.player.get_score(), 2)


if __name__ == '__main__':
    unittest.main()
