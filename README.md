# 🎴 Higher or Lower Card Game

A Python-based card game where you compete against a CPU to guess whether the next card will be higher or lower than the current card. Test your luck and intuition in this classic guessing game!

## 📋 Table of Contents

- [Features](#features)
- [Game Rules](#game-rules)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Project Structure](#project-structure)
- [Running Tests](#running-tests)
- [Requirements](#requirements)

## ✨ Features

- 🎮 **Interactive Menu System** - Easy-to-navigate menu with options to play, view rules, or exit
- 🤖 **CPU Opponent** - Play against a computer opponent that makes random guesses
- 🃏 **Joker Penalty** - Jack cards reset your score to zero, adding strategic risk
- 🎯 **Ace Flexibility** - Aces are treated as high (14) after number cards and low (1) after face cards
- 📊 **Live Score Tracking** - Real-time score updates for both player and CPU
- 🔁 **Customizable Rounds** - Choose how many rounds you want to play
- 📖 **In-Game Rules** - View complete game rules without leaving the application
- ✅ **Comprehensive Testing** - 80+ unit tests ensuring game integrity

## 🎯 Game Rules

### Objective
Guess correctly whether the next card will be **higher** or **lower** than the current card. Compete against the CPU to achieve the highest score!

### Card Rankings
Cards rank from low to high: **2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A**

- Number cards: Value equals their number (2-10)
- Jack (J): 11
- Queen (Q): 12
- King (K): 13
- Ace (A): 14 (high) or 1 (low, when following face cards)

### Gameplay
1. A starting card is displayed face-up
2. You guess if the next card will be "higher" or "lower"
3. The CPU also makes a random guess
4. The next card is revealed
5. Correct guesses earn 1 point
6. The revealed card becomes the new current card
7. Play continues for the chosen number of rounds

### Special Rules
- **Equal Cards**: If the next card has the same value, the guess is considered incorrect
- **Joker Penalty**: Drawing a Jack (J) resets the score of players who guessed incorrectly to 0
- **Ace Behavior**: 
  - After face cards (J, Q, K): Ace = 1 (low)
  - After number cards: Ace = 14 (high)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/HakimM16/higher_or_lower.git
   cd higher_or_lower
   ```

2. **Ensure Python 3.x is installed**
   ```bash
   python --version
   ```

3. **No additional dependencies required** - The game uses only Python standard library

## 🎮 How to Play

### Running the Game

**Option 1: Run from the main entry point**
```bash
python src/main.py
```

**Option 2: Run directly from game module**
```bash
python src/game_features/game.py
```

### Menu Options

When you start the game, you'll see:

```
=== 🎴 Higher or Lower Menu ===
1. ▶️ Play Game
2. 📘 View Rules
3. 🚪 Exit
```

1. **Play Game**: Choose number of rounds and start playing
2. **View Rules**: Display complete game rules
3. **Exit**: Quit the application

### During Gameplay

- Type `higher` or `lower` when prompted for your guess
- Watch as the CPU makes its random guess
- See the next card revealed
- Track scores after each round
- View final results when all rounds complete

## 📁 Project Structure

```
higher_or_lower/
├── src/
│   ├── main.py                    # Main entry point
│   └── game_features/
│       ├── card.py                # Card class with rank and suit
│       ├── cpu.py                 # CPU player logic
│       ├── dealer.py              # Dealer and game evaluation
│       ├── deck.py                # Deck management and shuffling
│       ├── game.py                # Game loop and menu system
│       └── player.py              # Player logic and input handling
├── tests/
│   ├── test_card.py               # Card class tests
│   ├── test_cpu.py                # CPU logic tests
│   ├── test_dealer.py             # Dealer and evaluation tests
│   ├── test_deck.py               # Deck functionality tests
│   ├── test_game.py               # Game flow tests
│   ├── test_player.py             # Player logic tests
│   ├── test_all.py                # Master test suite
│   └── README_TESTS.md            # Testing documentation
├── docs/
│   ├── notes.txt                  # Development notes
│   └── rules.md                   # Complete game rules
└── README.md                      # This file
```

## 🧪 Running Tests

The project includes comprehensive unit tests covering all game components.

### Run All Tests
```bash
python tests/test_all.py
```

### Run Individual Test Modules
```bash
python tests/test_card.py
python tests/test_deck.py
python tests/test_player.py
python tests/test_cpu.py
python tests/test_dealer.py
python tests/test_game.py
```

### Run with Verbose Output
```bash
python -m unittest discover -v
```

### Test Coverage
- **Card Tests**: Initialization, suit symbols, rank values
- **Deck Tests**: Building, shuffling, dealing, empty deck handling
- **Player Tests**: Guess validation, scoring, input handling
- **CPU Tests**: Random guessing, scoring
- **Dealer Tests**: Card evaluation, Ace behavior, game state
- **Game Tests**: Round flow, winner determination, menu system

For detailed testing documentation, see `tests/README_TESTS.md`.

## 💻 Requirements

- **Python**: 3.6 or higher
- **Operating System**: Windows, macOS, or Linux
- **Dependencies**: None (uses Python standard library only)

### Python Modules Used
- `random` - For shuffling and CPU decisions
- `pathlib` - For file path handling
- `unittest` - For testing framework
- `unittest.mock` - For mocking in tests

## 🎨 Features Breakdown

### Card Class
- Represents individual playing cards
- Handles suit symbols (♠, ♥, ♦, ♣)
- Manages rank values and comparisons

### Deck Class
- Creates standard 52-card deck
- Shuffles cards randomly
- Deals cards one at a time
- Handles empty deck scenarios

### Player Class
- Accepts and validates user input
- Tracks player score
- Handles score reset on Joker penalty

### CPU Class
- Makes random guesses
- Tracks CPU score
- Mirrors player functionality

### Dealer Class
- Manages current and next cards
- Evaluates guess correctness
- Implements Ace flexibility rules
- Controls game rounds

### Game Class
- Orchestrates game flow
- Handles player and CPU turns
- Manages round progression
- Determines winner
- Provides interactive menu

## 🏆 Winning the Game

The player or CPU with the **highest score** after all rounds wins!

- **Player Wins**: Your score > CPU score 🎉
- **CPU Wins**: CPU score > Your score 🤖
- **Tie**: Both scores equal 🤝

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📝 License

This project is open source and available for educational purposes.

## 👤 Author

**HakimM16**
- GitHub: [@HakimM16](https://github.com/HakimM16)

## 🎉 Enjoy the Game!

Have fun testing your intuition and competing against the CPU. May the cards be in your favor! 🃏✨
