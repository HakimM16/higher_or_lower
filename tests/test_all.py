"""
Master test suite that runs all unit tests for the Higher or Lower card game.
Run this file to execute all tests at once.
"""
import unittest
import sys

# Import all test modules
from test_card import TestCard
from test_deck import TestDeck
from test_player import TestPlayer
from test_cpu import TestCPU
from test_dealer import TestDealer
from test_game import TestGame, TestChooseRounds, TestShowRules


def create_test_suite():
    """Create a test suite containing all test cases."""
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCard))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestDeck))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestPlayer))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCPU))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestDealer))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestGame))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestChooseRounds))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestShowRules))
    
    return suite


if __name__ == '__main__':
    # Run the test suite
    runner = unittest.TextTestRunner(verbosity=2)
    suite = create_test_suite()
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("="*70)
    
    # Exit with appropriate code
    sys.exit(0 if result.wasSuccessful() else 1)
