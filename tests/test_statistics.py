import pytest

from roshambo.statistics import Move, Result


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


class TestResult:
    @pytest.mark.parametrize('player_move,ai_move', [
        (Move.rock, Move.scissors),
        (Move.paper, Move.rock),
        (Move.scissors, Move.paper)
    ])
    def test_player_wins(self, player_move, ai_move):
        result = Result(player_move, ai_move)
        assert result.player_wins
        assert not result.ai_wins
        assert not result.is_draw

    @pytest.mark.parametrize('player_move,ai_move', [
        (Move.scissors, Move.rock),
        (Move.rock, Move.paper),
        (Move.paper, Move.scissors)
    ])
    def test_ai_wins(self, player_move, ai_move):
        result = Result(player_move, ai_move)
        assert not result.player_wins
        assert result.ai_wins
        assert not result.is_draw

    def test_draw(self):
        for move in Move:
            result = Result(move, move)
        
            assert not result.player_wins
            assert not result.ai_wins
            assert result.is_draw
