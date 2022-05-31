from __future__ import annotations

from roshambo.statistics import Move

import random
from abc import ABC, abstractmethod


class AI(ABC):
    """AI that can play game rock-paper-scissors."""

    @abstractmethod
    def next_move(self) -> Move:
        """Returns next move the AI will make."""
        pass


class RandomAI(AI):
    """AI that plays game by choosing random moves in every turn."""

    def next_move(self) -> Move:
        """Returns a random move the AI will make."""
        return random.choice(list(Move))