from __future__ import annotations
from typing import List, Tuple, Optional, Dict

B, W, E = "B", "W", None

DIRS = [(-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)]


class Board:
    def __init__(self) -> None:
        self.board: List[List[Optional[str]]] = [[E] * 8 for _ in range(8)]
        self.board[3][3] = W; self.board[3][4] = B
        self.board[4][3] = B; self.board[4][4] = W
        self.history: List[Dict] = []
        self.seen: set = set()
        self._remember()

    @staticmethod
    def inside(r: int, c: int) -> bool:
        return 0 <= r < 8 and 0 <= c < 8

    def _dfs_ray(self, r: int, c: int, dr: int, dc: int, color: str) -> List[Tuple[int, int]]:
        opp = B if color == W else W
        path: List[Tuple[int, int]] = []
        r += dr; c += dc
        while self.inside(r, c) and self.board[r][c] == opp:
            path.append((r, c))
            r += dr; c += dc
        if self.inside(r, c) and self.board[r][c] == color and path:
            return path
        return []

    def legal_moves(self, color: str) -> List[Tuple[int, int]]:
        moves: List[Tuple[int, int]] = []
        opp = B if color == W else W
        for r in range(8):
            for c in range(8):
                if self.board[r][c] is not E:
                    continue
                if not any(self.inside(r+dr, c+dc) and self.board[r+dr][c+dc] == opp for dr, dc in DIRS):
                    continue
                flips: List[Tuple[int, int]] = []
                for dr, dc in DIRS:
                    flips.extend(self._dfs_ray(r, c, dr, dc, color))
                if flips:
                    moves.append((r, c))
        return moves

    def must_pass(self, color: str) -> bool:
        return len(self.legal_moves(color)) == 0

    def is_game_over(self) -> bool:
        return self.must_pass(B) and self.must_pass(W)

    def score(self) -> Dict[str, int]:
        b = sum(cell == B for row in self.board for cell in row)
        w = sum(cell == W for row in self.board for cell in row)
        return {B: b, W: w}

    def apply(self, move: Optional[Tuple[int, int]], color: str) -> int:
        if move is None:
            self.history.append({"move": None, "color": color, "flipped": []})
            self._remember()
            return 0
        r, c = move
        if self.board[r][c] is not E:
            raise ValueError("Cell not empty")
        flips: List[Tuple[int, int]] = []
        for dr, dc in DIRS:
            flips.extend(self._dfs_ray(r, c, dr, dc, color))
        if not flips:
            raise ValueError("Illegal move: no flips")
        self.board[r][c] = color
        for fr, fc in flips:
            self.board[fr][fc] = color
        self.history.append({"move": (r, c), "color": color, "flipped": flips})
        self._remember()
        return len(flips)

    def undo(self) -> None:
        if not self.history:
            return
        rec = self.history.pop()
        color = rec["color"]
        opp = B if color == W else W
        if rec["move"] is None:
            self._remember()
            return
        r, c = rec["move"]
        for fr, fc in rec["flipped"]:
            self.board[fr][fc] = opp
        self.board[r][c] = E
        self._remember()

    def board_key(self) -> Tuple[int, ...]:
        mapping = {E: 0, B: 1, W: 2}
        return tuple(mapping[self.board[r][c]] for r in range(8) for c in range(8))

    def _remember(self) -> None:
        self.seen.add(self.board_key())

    def seen_before(self) -> bool:
        return self.board_key() in self.seen


__all__ = ["Board", "B", "W", "E", "DIRS"]
