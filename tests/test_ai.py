import pytest

from roshambo.ai import Move, RandomAI

class TestMove:
    @pytest.mark.parametrize('move1,move2', [
        (Move.rock, Move.scissors),
        (Move.paper, Move.rock),
        (Move.scissors, Move.paper)
    ])
    def test_dominates(self, move1, move2):
        assert move1.dominates is move2

    @pytest.mark.parametrize('move1,move2', [
        (Move.rock, Move.scissors),
        (Move.paper, Move.rock),
        (Move.scissors, Move.paper)
    ])
    def test_gt(self, move1, move2):
        assert move1 > move2

    @pytest.mark.parametrize('move1,move2', [
        (Move.scissors, Move.rock),
        (Move.rock, Move.paper),
        (Move.paper, Move.scissors)
    ])
    def test_not_gt(self, move1, move2):
        assert not move1 > move1
        assert not move1 > move2

    @pytest.mark.parametrize('move1,move2', [
        (Move.rock, Move.scissors),
        (Move.paper, Move.rock),
        (Move.scissors, Move.paper)
    ])
    def test_ge(self, move1, move2):
        assert move1 >= move1
        assert move1 >= move2

    @pytest.mark.parametrize('move1,move2', [
        (Move.scissors, Move.rock),
        (Move.rock, Move.paper),
        (Move.paper, Move.scissors)
    ])
    def test_not_ge(self, move1, move2):
        assert not move1 >= move2

    def test_ne(self):
        for move1 in Move:
            for move2 in Move:
                if move1 is not move2:
                    assert move1 != move2

    def test_eq(self):
        for move in Move:
            assert move == move

    @pytest.mark.parametrize('move1,move2', [
        (Move.scissors, Move.rock),
        (Move.rock, Move.paper),
        (Move.paper, Move.scissors)
        
    ])
    def test_lt(self, move1, move2):
        assert move1 < move2

    @pytest.mark.parametrize('move1,move2', [
        (Move.rock, Move.scissors),
        (Move.paper, Move.rock),
        (Move.scissors, Move.paper)
    ])
    def test_not_lt(self, move1, move2):
        assert not move1 < move1
        assert not move1 < move2

    @pytest.mark.parametrize('move1,move2', [
        (Move.scissors, Move.rock),
        (Move.rock, Move.paper),
        (Move.paper, Move.scissors)
    ])
    def test_le(self, move1, move2):
        assert move1 <= move1
        assert move1 <= move2

    @pytest.mark.parametrize('move1,move2', [
        (Move.rock, Move.scissors),
        (Move.paper, Move.rock),
        (Move.scissors, Move.paper)
    ])
    def test_not_le(self, move1, move2):
        assert not move1 <= move2


class TestRandomAi:
    def test_moves_are_random(self):
        stats = {move:0 for move in Move}

        ai = RandomAI()
        for i in range(100_000):
            stats[ai.next_move()] += 1

        for stat in stats.values():
            assert stat == pytest.approx(100_000/3, rel=1e-2)
