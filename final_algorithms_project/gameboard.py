# gameboard.py
"""Game constants, configuration, and UI functions."""

# Constants
EMPTY = None
BLACK = "⚫"
WHITE = "⚪"
HINT = "x"
BOARD_SIZE = 8

DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1),
]


# UI Functions

def show_hints(board, player):
    """Display hint markers for all possible moves."""
    from game_logic import possible_moves
    clear_hints(board)
    moves = possible_moves(board, player)
    for row, col in moves:
        board[row][col] = HINT


def clear_hints(board):
    """Remove all hint markers from the board."""
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == HINT:
                board[row][col] = EMPTY


def update_title(board, current_player, white_wins, black_wins):
    """Update the window title with current game state."""
    from game_logic import count_pieces
    white, black = count_pieces(board)
    turn_text = 'Black ⚫' if current_player == BLACK else 'White ⚪'
    board.title = f"Othello! Turn: {turn_text} | ⚪ {white} - ⚫ {black}"


def show_game_over(board, result_msg, white_wins, black_wins):
    """Display game over message with final scores."""
    from game_logic import count_pieces
    white, black = count_pieces(board)
    board.title = (
        f"Game over! {result_msg} "
        f"Final score: ⚪ {white} - ⚫ {black} | "
        f"Match wins: ⚪ {white_wins} - ⚫ {black_wins}"
    )