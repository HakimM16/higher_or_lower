# Unit Tests for Higher or Lower Card Game

This directory contains comprehensive unit tests for the Higher or Lower card game.

## Test Files

- **test_card.py** - Tests for the Card class
- **test_deck.py** - Tests for the Deck class
- **test_player.py** - Tests for the Player class
- **test_cpu.py** - Tests for the CPU class
- **test_dealer.py** - Tests for the Dealer class
- **test_game.py** - Tests for the Game class and utility functions
- **test_all.py** - Master test suite that runs all tests

## Running Tests

### Run All Tests
```powershell
python test_all.py
```

### Run Individual Test Files
```powershell
python test_card.py
python test_deck.py
python test_player.py
python test_cpu.py
python test_dealer.py
python test_game.py
```

### Run with Verbose Output
```powershell
python -m unittest discover -v
```

### Run Specific Test Class
```powershell
python -m unittest test_card.TestCard
```

### Run Specific Test Method
```powershell
python -m unittest test_card.TestCard.test_card_initialization
```

## Test Coverage

### Card Tests (test_card.py)
- Card initialization
- Suit symbol mapping (Hearts, Diamonds, Clubs, Spades)
- Rank value mapping (2-10, J, Q, K, A)
- Invalid suit/rank handling

### Deck Tests (test_deck.py)
- Deck initialization with 52 cards
- All unique cards present
- Card dealing and deck size reduction
- Empty deck error handling
- Shuffle functionality
- Deck integrity after shuffle

### Player Tests (test_player.py)
- Player initialization
- Making valid guesses (higher/lower)
- Case-insensitive input handling
- Invalid guess error handling
- Score increment and retrieval
- Score reset (Joker penalty)

### CPU Tests (test_cpu.py)
- CPU initialization
- Random guess generation
- Randomness verification
- Score increment and retrieval
- Score reset (Joker penalty)

### Dealer Tests (test_dealer.py)
- Dealer initialization with deck
- Custom max_rounds setting
- Current card display formatting
- Drawing and updating cards
- Guess evaluation (higher/lower)
- Ace special behavior (high/low after face cards)
- Same value card handling

### Game Tests (test_game.py)
- Game initialization with all components
- Joker penalty trigger detection
- Winner determination (player/CPU/tie)
- Round playing and counter increment
- Max rounds enforcement
- Player guess prompt with retry logic
- Score updates for correct/incorrect guesses
- Joker penalty application
- Input validation for round selection
- Rules display functionality

## Test Statistics

Total test cases: **80+**

Coverage includes:
- Edge cases (empty deck, invalid input, boundary values)
- Normal operations (gameplay flow, scoring)
- Special rules (Ace behavior, Joker penalty)
- Error handling (ValueError, FileNotFoundError)
- Input validation and retry logic
- Randomness verification

## Requirements

- Python 3.x
- unittest (built-in)
- unittest.mock (built-in)

## Notes

- Tests use mocking for user input and print statements
- Randomness is verified statistically (100 iterations)
- All tests are independent and can run in any order
- Setup and teardown methods ensure clean test state
