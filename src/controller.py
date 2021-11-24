import click

from .models import Player, Computer, Game
from .game_config import moves, reversed_game_moves_map

class Controller:

    def __init__(self):  # pragma: no cover
        pass

    @staticmethod
    def set_player(name):
        player = Player(name)
        return player

    @staticmethod
    def set_computer_player():
        computer = Computer()
        return computer

    @staticmethod
    def set_game(rounds, player_a, player_b):
        game = Game(rounds, player_a, player_b)
        return game

    @staticmethod
    def play_game(game):
        player_a = game.player_a
        player_b = game.player_b

        for i in range(game.rounds):
            click.echo('-' * 50)
            click.echo(f'Round #{i + 1}')

            # TODO Move this block to the Player model to make
            #  the game more abstract and reuse the same code for
            #  "one player" and "two players" modes
            # ===Beginning of the block===
            input = click.prompt(
                'Please enter your move',
                type=click.Choice(moves, case_sensitive=False)
            )
            move = reversed_game_moves_map[input]
            player_a.make_move(move)
            # ===End of the block===

            player_b.make_move()

            click.echo(
                f'{str(player_a)} moved with {str(player_a.get_move())}, '
                f'{str(player_b)} moved with {str(player_b.get_move())}. '
            )

            winner = game.play_round()

            if winner:
                click.echo(f'The winner is {str(winner)}')
            else:
                click.echo('A draw')

        click.echo('=' * 50)
        click.echo(game.get_stats())
