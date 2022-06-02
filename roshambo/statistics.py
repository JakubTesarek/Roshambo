from __future__ import annotations

from enum import Enum


class Move(Enum):
    """A move made by a player or an AI."""

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

    @property
    def is_dominated_by(self) -> Move:
        """A move that current move loses againts."""
        return {
            Move.scissors: Move.rock,
            Move.rock: Move.paper,
            Move.paper: Move.scissors 
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

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}:{self.name}'


class Result:
    """Result of one round of game."""

    def __init__(self, player_move: Move, ai_move: Move):
        self.player_move = player_move
        self.ai_move = ai_move

    @property
    def ai_wins(self) -> bool:
        """Returns True if AI won."""
        return self.player_move < self.ai_move

    @property
    def player_wins(self) -> bool:
        """Returns True if player won."""
        return self.player_move > self.ai_move

    @property
    def is_draw(self) -> bool:
        """Returns True round ended up as a draw."""
        return self.player_move == self.ai_move


class Stats:
    """Statistics of series of game rounds."""

    def __init__(self) -> None:
        self.results: list[Result] = []

    def add_result(self, result: Result) -> None:
        """Add a game round result."""
        self.results.append(result)

    @property
    def games_count(self) -> int:
        """Returns number of all played games."""
        return len(self.results)

    @property
    def player_wins_count(self) -> int:
        """Returns number of time player won."""
        wins = 0
        for result in self.results:
            if result.player_wins:
                wins += 1
        return wins

    @property
    def ai_wins_count(self) -> int:
        """Returns number of time AI won."""
        wins = 0
        for result in self.results:
            if result.ai_wins:
                wins += 1
        return wins

    @property
    def draws_count(self) -> int:
        """Returns number of time fame ended up as draw."""
        draws = 0
        for result in self.results:
            if result.is_draw:
                draws += 1
        return draws

    @property
    def player_wins_rate(self) -> float:
        """Returns a fraction of games player won."""
        if games := self.games_count:
            return self.player_wins_count / games
        return 0.0

    @property
    def ai_wins_rate(self) -> float:
        """Returns a fraction of games AI won."""
        if games := self.games_count:
            return self.ai_wins_count / games
        return 0.0

    @property
    def draws_rate(self) -> float:
        """Returns a fraction of games that ended up as a draw."""
        if games := self.games_count:
            return self.draws_count / games
        return 0.0
