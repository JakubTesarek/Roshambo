from __future__ import annotations

import random
from abc import ABC, abstractmethod
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


class AI(ABC):
    """AI that can play game rock-paper-scissors."""

    @abstractmethod
    def next_move(self) -> Move:
        """Returns next move the AI will make."""
        pass


class RandomAI(AI):
    """AI that plays game by choosing random moves in every turn."""
    def next_move(self) -> Move:
        return random.choice(list(Move))