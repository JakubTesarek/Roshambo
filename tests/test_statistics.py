import pytest

from roshambo.statistics import Move, Result, Stats


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


class TestStats:
    def test_games_count(self):
        stats = Stats()
        assert stats.games_count == 0
        stats.add_result(Result(Move.rock, Move.paper))
        assert stats.games_count == 1

    def test_counts(self):
        stats = Stats()
        assert stats.player_wins_count == 0
        assert stats.ai_wins_count == 0
        assert stats.draws_count == 0
        
        stats.add_result(Result(Move.paper, Move.rock))  # player wins
        assert stats.player_wins_count == 1
        assert stats.ai_wins_count == 0
        assert stats.draws_count == 0

        stats.add_result(Result(Move.rock, Move.paper))  # ai wins
        assert stats.player_wins_count == 1
        assert stats.ai_wins_count == 1
        assert stats.draws_count == 0

        stats.add_result(Result(Move.paper, Move.paper))  # draw
        assert stats.player_wins_count == 1
        assert stats.ai_wins_count == 1
        assert stats.draws_count == 1

    def test_rates(self):
        stats = Stats()
        assert stats.player_wins_rate == 0.0
        assert stats.ai_wins_rate == 0.0
        assert stats.draws_rate == 0.0
        
        stats.add_result(Result(Move.paper, Move.rock))  # player wins
        assert stats.player_wins_rate == 1.0
        assert stats.ai_wins_rate == 0
        assert stats.draws_rate == 0

        stats.add_result(Result(Move.rock, Move.paper))  # ai wins
        assert stats.player_wins_rate == 0.5
        assert stats.ai_wins_rate == 0.5
        assert stats.draws_rate == 0

        stats.add_result(Result(Move.paper, Move.paper))  # draw
        assert stats.player_wins_rate == pytest.approx(0.333, rel=1e-2)
        assert stats.ai_wins_rate == pytest.approx(0.333, rel=1e-2)
        assert stats.draws_rate == pytest.approx(0.333, rel=1e-2)
