# Higher or Lower: Documentation Notes

## 1. Folder Layout
- `src/` contains all executable Python code, ensuring imports remain consistent and making later packaging straightforward.  
- Within `src/`, the `game_features/` package (game modules) isolates gameplay logic (`dealer.py`, `deck.py`, `card.py`, `player.py`, `cpu.py`, `game.py`). This separation allows us to extend or replace components (e.g., new AI opponents) without altering the entry point.  
- `docs/` stores supporting documentation (this file, `rules.md`). Keeping documentation within the project ensures a single source of truth.  
- `tests/` collects unit tests, mirroring the `src/` structure so test coverage can expand without cluttering runtime code.  

## 2. `main.py` Responsibilities
- `src/main.py` provides a minimal interface that simply imports `show_menu()` from the gameplay package and triggers it under `if __name__ == "__main__"`. This keeps the entry point clear for developers and tooling (debuggers, packaging entry points).  
- With the `Game` menu isolated inside `game.py`, we avoid circular imports and enable CLI utilities or tests to run without invoking interactive prompts.  

## 3. Other Supporting Choices
- `rules.md` resides in `docs/` so both players and the CLI can access the same markdown file (`Game.show_rules()` references it via `pathlib`, maintaining one canonical rule set).  
- `Game` deliberately retains all round flow (`play_round`, `_handle_result`, `_joker_triggered`) within a single class so state (current card, scores, rounds) is centralised. Commands from `main.py` instantiate `Dealer` with the chosen round count and hand control passes to `Game.start_game()`, which then loops over `play_round()` until complete.  
- `Player` and `CPU` both expose common operations (`make_guess`, `increment_score`, `reset_score`, `get_score`). This shared interface keeps `Game` agnostic to who is playing, so adding multiplayer or additional bots would require minimal integration.  
- `Dealer` encapsulates deck management and card comparison logic. By allowing `Dealer` to evaluate guesses and update the current card, we avoid duplicating card-order rules across modules and make it easier to introduce future rule variants (e.g., Ace high versus low).  