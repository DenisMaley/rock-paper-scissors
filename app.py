import click

from src.controller import Controller


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    '--number', '-n',
    prompt=True,
    required=True,
    type=click.IntRange(1, 7),
    default=1,
    help='Number of rounds',
)
def rps_game(number):
    for i in range(number):
        click.echo(f'Round #{i+1}')
        move = click.prompt('Please enter your move', type=click.IntRange(0, 2))
        result = Controller.play_rps_game(move)
        click.echo(result)


if __name__ == '__main__':
    cli()
