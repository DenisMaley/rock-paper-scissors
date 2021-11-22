import random

game_map = {0: 'rock', 1: 'paper', 2: 'scissors'}

# Win-lose matrix for the game
rps_matrix = [
    [-1, 1, 0],
    [1, -1, 2],
    [0, 2, -1]
]

class Controller:

    def __init__(self):  # pragma: no cover
        pass

    @staticmethod
    def play_rps_game(move):

        print('Computer making a move....')

        # Get the computer move randomly
        comp_move = random.randint(0, 2)

        # Find the winner of the match
        winner = rps_matrix[move][comp_move]

        if winner == move:
            result = 'You WIN!!!'
        elif winner == comp_move:
            result = 'COMPUTER WINS!!!'
        else:
            result = 'TIE GAME'


        return f'You have chosen {game_map[move]}, computer - {game_map[comp_move]}, {result}'
