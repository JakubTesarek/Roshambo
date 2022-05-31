import pytest

from roshambo.ai import RandomAI
from roshambo.statistics import Move


class TestRandomAi:
    def test_moves_are_random(self):
        stats = {move:0 for move in Move}

        ai = RandomAI()
        for i in range(100_000):
            stats[ai.next_move()] += 1

        for stat in stats.values():
            assert stat == pytest.approx(100_000/3, rel=1e-2)
