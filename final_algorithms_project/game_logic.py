# game_logic.py
"""Core game logic for Reversi/Othello."""

from gameboard import EMPTY, BLACK, WHITE, HINT, DIRECTIONS, BOARD_SIZE


def possible_moves(board, player):
    """Find all valid moves for the given player."""
    opponent = WHITE if player == BLACK else BLACK
    possible = []

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] is not None:
                continue

            if is_valid_move(board, row, col, player, opponent):
                possible.append((row, col))

    return possible


def is_valid_move(board, row, col, player, opponent):
    """Check if a move at (row, col) is valid for player."""
    for dr, dc in DIRECTIONS:
        new_row, new_col = row + dr, col + dc
        if not (0 <= new_row < BOARD_SIZE and 0 <= new_col < BOARD_SIZE):
            continue
        if board[new_row][new_col] != opponent:
            continue

        r, c = new_row + dr, new_col + dc
        while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == opponent:
            r += dr
            c += dc

        if 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == player:
            return True

    return False


def flip_color(board, row, col, current):
    """Flip opponent pieces in all valid directions. Returns list of flipped positions."""
    opponent = WHITE if current == BLACK else BLACK
    to_flip = []
    
    for dr, dc in DIRECTIONS:
        r, c = row + dr, col + dc
        line = []
        
        if not (0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE) or board[r][c] != opponent:
            continue
            
        while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == opponent:
            line.append((r, c))
            r += dr
            c += dc

        if line and 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == current:
            to_flip.extend(line)

    for r, c in to_flip:
        board[r][c] = current
        
    return to_flip


def count_pieces(board):
    """Count white and black pieces. Returns (white_count, black_count)."""
    white = 0
    black = 0
    
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == WHITE:
                white += 1
            elif board[i][j] == BLACK:
                black += 1

    return white, black


def board_full(board):
    """Check if the board is full (no empty or hint cells)."""
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == EMPTY or board[row][col] == HINT:
                return False
    return True


def check_game_over(board):
    """
    Check if game is over (no valid moves for either player).
    Returns tuple: (is_over, winner_or_tie_message)
    Winner message is one of: "White wins!", "Black wins!", "It's a tie!", or None
    """
    if possible_moves(board, BLACK) or possible_moves(board, WHITE):
        return False, None

    white, black = count_pieces(board)

    if white > black:
        return True, "White wins!"
    elif black > white:
        return True, "Black wins!"
    else:
        return True, "It's a tie!"