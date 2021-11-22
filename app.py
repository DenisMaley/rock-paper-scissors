import click

from src.controller import Controller


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    '--move', '-m',
    required=True,
    type=click.IntRange(0, 2),
    default=0,
    help='Your move',
)
def rps_game(move):
    result = Controller.play_rps_game(move)
    click.echo(result)


if __name__ == '__main__':
    cli()
