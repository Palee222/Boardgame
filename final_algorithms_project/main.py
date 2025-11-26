# main.py
from game2dboard import Board
from gameboard import EMPTY, BLACK, WHITE, HINT, BOARD_SIZE
from gameboard import show_hints, clear_hints, update_title, show_game_over
from game_state import GameState
from game_logic import flip_color, check_game_over


# Global game state
game_state = GameState()


def handle_mouse_click(btn, row, col):
    """Handle mouse click events on the board."""
    global game_state
    
    if board[row][col] != HINT:
        if board[row][col] is not None:
            board.title = "That tile is already taken!"
        else:
            board.title = "Invalid move! Click on one of the possible moves (x)."
        return

    clear_hints(board)
    board[row][col] = game_state.current_player

    flipped = flip_color(board, row, col, game_state.current_player)
    if not flipped:
        board[row][col] = EMPTY
        show_hints(board, game_state.current_player)
        update_title(board, game_state.current_player, game_state.white_wins, game_state.black_wins)
        return

    # Save move to history
    game_state.push_move(row, col, game_state.current_player, flipped)

    # Switch to other player
    game_state.switch_player()

    show_hints(board, game_state.current_player)
    update_title(board, game_state.current_player, game_state.white_wins, game_state.black_wins)
    
    # Check if game is over
    is_over, result = check_game_over(board)
    if is_over:
        if result == "White wins!":
            game_state.white_wins += 1
        elif result == "Black wins!":
            game_state.black_wins += 1
        show_game_over(board, result, game_state.white_wins, game_state.black_wins)


def handle_undo():
    """Undo the last move."""
    global game_state
    
    if not game_state.has_history():
        board.title = "No moves to undo."
        return

    row, col, player, flipped = game_state.pop_move()

    clear_hints(board)
    board[row][col] = EMPTY
    
    opponent = WHITE if player == BLACK else BLACK
    for r, c in flipped:
        board[r][c] = opponent

    game_state.current_player = player

    show_hints(board, game_state.current_player)
    update_title(board, game_state.current_player, game_state.white_wins, game_state.black_wins)


def handle_key_press(key):
    """Handle keyboard events."""
    if key == "u":
        handle_undo()


def init_board():
    """Initialize the game board with starting positions."""
    board = Board(BOARD_SIZE, BOARD_SIZE)
    board[3][3] = WHITE
    board[4][3] = BLACK
    board[3][4] = BLACK
    board[4][4] = WHITE
    
    board.cell_size = 80
    board.cell_color = "green"
    board.on_mouse_click = handle_mouse_click
    board.on_key_press = handle_key_press
    
    return board


if __name__ == "__main__":
    # Initialize the board
    board = init_board()
    
    # Show initial hints and title
    show_hints(board, game_state.current_player)
    update_title(board, game_state.current_player, game_state.white_wins, game_state.black_wins)
    
    # Start the game (blocking call)
    board.show()