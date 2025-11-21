import unittest
from cpu import CPU


class TestCPU(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.cpu = CPU()

    def test_cpu_initialization(self):
        """Test that a CPU is initialized with score 0."""
        self.assertEqual(self.cpu.score, 0)
        self.assertEqual(self.cpu.get_score(), 0)

    def test_make_guess_returns_valid_choice(self):
        """Test that make_guess returns either 'higher' or 'lower'."""
        guess = self.cpu.make_guess()
        self.assertIn(guess, ["higher", "lower"])

    def test_make_guess_randomness(self):
        """Test that make_guess produces both values over multiple calls."""
        guesses = set()
        for _ in range(100):  # Run 100 times to ensure both values appear
            guesses.add(self.cpu.make_guess())
        
        # With 100 random calls, we should see both "higher" and "lower"
        self.assertEqual(len(guesses), 2)
        self.assertIn("higher", guesses)
        self.assertIn("lower", guesses)

    def test_increment_score(self):
        """Test that increment_score increases score by 1."""
        self.cpu.increment_score()
        self.assertEqual(self.cpu.get_score(), 1)

    def test_increment_score_multiple_times(self):
        """Test that score increments correctly multiple times."""
        for i in range(5):
            self.cpu.increment_score()
        self.assertEqual(self.cpu.get_score(), 5)

    def test_reset_score(self):
        """Test that reset_score sets score to 0."""
        self.cpu.increment_score()
        self.cpu.increment_score()
        self.cpu.increment_score()
        self.assertEqual(self.cpu.get_score(), 3)
        
        self.cpu.reset_score()
        self.assertEqual(self.cpu.get_score(), 0)

    def test_reset_score_when_already_zero(self):
        """Test that reset_score works when score is already 0."""
        self.cpu.reset_score()
        self.assertEqual(self.cpu.get_score(), 0)

    def test_get_score_returns_correct_value(self):
        """Test that get_score returns the current score."""
        self.assertEqual(self.cpu.get_score(), 0)
        self.cpu.increment_score()
        self.assertEqual(self.cpu.get_score(), 1)
        self.cpu.increment_score()
        self.assertEqual(self.cpu.get_score(), 2)


if __name__ == '__main__':
    unittest.main()
