# game_state.py
"""Game state management."""

from gameboard import BLACK, WHITE

class GameState:
    """Manages the current game state."""
    
    def __init__(self):
        self.current_player = BLACK
        self.history = []  # each entry: (row, col, player, flipped_list)
        self.white_wins = 0
        self.black_wins = 0
    
    def switch_player(self):
        """Switch to the other player."""
        self.current_player = WHITE if self.current_player == BLACK else BLACK
    
    def push_move(self, row, col, player, flipped):
        """Add a move to history."""
        self.history.append((row, col, player, flipped))
    
    def pop_move(self):
        """Remove and return the last move from history."""
        if not self.history:
            return None
        return self.history.pop()
    
    def has_history(self):
        """Check if there are moves to undo."""
        return len(self.history) > 0