import click

from src.controller import Controller


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    '--rounds', '-r',
    prompt=True,
    required=True,
    type=click.IntRange(1, 7),
    default=1,
    help='Number of rounds',
)
@click.option(
    '--name', '-n',
    prompt=True,
    required=True,
    type=str,
    help='Player`s name',
)
def rps_game(rounds, name):
    player_a = Controller().set_player(name)
    player_b = Controller().set_computer_player()
    game = Controller().set_game(rounds, player_a, player_b)

    Controller().play_game(game)



if __name__ == '__main__':
    cli()
