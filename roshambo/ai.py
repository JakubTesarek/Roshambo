from __future__ import annotations

import random
from abc import ABC, abstractmethod

from rich.prompt import Prompt

from roshambo.statistics import Move, Stats, Result


class Participant(ABC):
    """Participant of a game that can make a move."""

    def __init__(self) -> None:
        self.stats = Stats()

    def add_result(self, result: Result) -> None:
        """Add result to internal statistics."""
        self.stats.add_result(result)

    @abstractmethod
    def next_move(self) -> Move:
        """Returns next move the AI will make."""
        pass


class HumanPlayer(Participant):
    def next_move(self) -> Move:
        choice = Prompt.ask(
            '[green]Please choose Rock [red](1)[/red], Paper [red](2)[/red], Scissors [red](3)[/red] or Quit [red](q)[/red].',
            choices=['1', '2', '3', 'q']
        )

        if choice == 'q':
            raise KeyboardInterrupt()
        else:
            return Move(int(choice))


class AI(Participant):
    """AI that can play game rock-paper-scissors."""

    def _get_backup_move(self) -> Move:
        """Returns a random move the AI will make in case it wasn't able to predict move properly."""
        return random.choice(list(Move))


class RandomAI(AI):
    """AI that plays game by choosing random moves in every turn."""

    def next_move(self) -> Move:
        """Returns a random move the AI will make."""
        return self._get_backup_move()


class MarkovChainAI(AI):
    """AI that uses Markov Chain of variable length to try to predict next player move."""

    def __init__(self, segment_length=1, history_length=10):
        super().__init__()
        self.segment_length = segment_length
        self.history_length = history_length

    @property
    def chain(self):
        chain = []
        for result in self.stats.results[-self.history_length:]:
            chain.append(result.player_move)
        return chain

    def _get_current_segment(self) -> tuple[Move, ...]:
        segment = tuple(self.chain[-self.segment_length:])
        if len(segment) == self.segment_length:
            return segment
        return None

    def _get_next_move_rates(self, segment: tuple[Move, ...]) -> dict[Move, float]:
        next_moves = {}
        current_segment = []
        for next_move in self.chain:
            if tuple(current_segment) == segment:
                next_moves.setdefault(next_move, 0)
                next_moves[next_move] += 1

            current_segment.append(next_move)
            current_segment = current_segment[-self.segment_length:]

        return next_moves

    def next_move(self) -> Move:
        """Returns a random move the AI will make."""
        segment = self._get_current_segment()
        move_rates = self._get_next_move_rates(segment)

        if move_rates:
            population = []
            weights = []
            for player_move, count in move_rates.items():
                population.append(player_move)
                weights.append(count)    

            expected = random.choices(
                population=population,
                weights=weights,
                k=1
            )[0]

            return expected.is_dominated_by
        else:
            return self._get_backup_move()