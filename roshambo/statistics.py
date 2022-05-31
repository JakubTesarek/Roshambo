from __future__ import annotations

from enum import Enum


class Move(Enum):
    rock = 1
    paper = 2
    scissors = 3

    @property
    def dominates(self) -> Move:
        """A move that current move wins againts."""
        return {
            Move.rock: Move.scissors,
            Move.paper: Move.rock,
            Move.scissors: Move.paper
        }[self]

    def __hash__(self) -> str:
        return hash(self.name)

    def __lt__(self, other) -> bool:
        return other.dominates is self

    def __le__(self, other) -> bool:
        return self in [other.dominates, other]

    def __eq__(self, other) -> bool:
        return self is other

    def __ne__(self, other) -> bool:
        return not self is other

    def __gt__(self, other) -> bool:
        return self.dominates is other

    def __ge__(self, other) -> bool:
        return other in [self.dominates, self]


class Result:
    def __init__(self, player_move: Move, ai_move: Move):
        self.player_move = player_move
        self.ai_move = ai_move

    @property
    def ai_wins(self):
        return self.player_move < self.ai_move

    @property
    def player_wins(self):
        return self.player_move > self.ai_move

    @property
    def is_draw(self):
        return self.player_move == self.ai_move
