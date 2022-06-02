from rich.prompt import Prompt
from rich.table import Table

from roshambo.ai import RandomAI, MarkovChainAI
from roshambo.ui import console
from roshambo.statistics import Move, Stats, Result

from typing import Optional


def get_player_move() -> Optional[Move]:
    choice = Prompt.ask(
        '[green]Please choose Rock [red](1)[/red], Paper [red](2)[/red], Scissors [red](3)[/red] or Quit [red](q)[/red].',
        choices=['1', '2', '3', 'q']
    )

    if choice == 'q':
        return None
    else:
        return Move(int(choice))
                

def print_result(result: Result) -> None:
    console.print(f'Player chooses [yellow]{player_move}[/yellow]. AI chooses [yellow]{ai_move}[/yellow].')
    if result.is_draw:
        console.print('[yellow bold]Game is a draw.\n')
    elif result.player_wins:
        console.print('[green bold]Player wins.[/green bold] Congratulations!\n')
    else:
        console.print('[red bold]AI wins.\n')


def print_stats(stats: Stats) -> None:
    if not stats.games_count:
        console.print(f'No games were played.\n')
    else:
        table = Table()

        table.add_column('Result', justify='left')
        table.add_column('Count', justify='right')
        table.add_column('Rate', justify='right')

        table.add_row('Player wins', str(stats.player_wins_count), f'{round(stats.player_wins_rate * 100, 2)}%')
        table.add_row('AI wins', str(stats.ai_wins_count), f'{round(stats.ai_wins_rate * 100, 2)}%')
        table.add_row('Draws', str(stats.draws_count), f'{round(stats.draws_rate * 100, 2)}%')

        console.print(table)


if __name__ == '__main__':
    ai = MarkovChainAI()
    stats = Stats()

    console.print('[yellow]Welcome to Roshambo, aka. Rock Paper Scissors.\n')

    try:
        while True:
            if player_move := get_player_move():
                ai_move = ai.next_move()
                result = Result(player_move, ai_move)
                stats.add_result(result)
                ai.add_result(result)
                print_result(result)
            else:
                break
    except KeyboardInterrupt:
        pass
    finally:
        print_stats(stats)
