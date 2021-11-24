import random

from .game_config import game_rules_matrix, game_moves_map, MOVES_NUM

class Player:
    def __init__(self, name):
        self.name = name
        self.move = None
        self.score = 0

    def make_move(self, move):
        self.move = move

    def get_move(self):
        return game_moves_map[self.move]

    def set_scored(self):
        self.score += 1

    def __str__(self):
        return self.name


class Computer(Player):
    def __init__(self):
        super().__init__('Computer')

    def make_move(self, move=None):
        self.move = random.randint(0, MOVES_NUM - 1)


class Game:
    def __init__(self, rounds, player_a, player_b):
        self.rounds = rounds
        self.player_a = player_a
        self.player_b = player_b
        self.draws = 0

    def play_round(self):
        winner_move = game_rules_matrix[self.player_a.move][self.player_b.move]

        if winner_move == self.player_a.move:
            self.player_a.set_scored()
            return self.player_a
        elif winner_move == self.player_b.move:
            self.player_b.set_scored()
            return self.player_b
        else:
            self.draws += 1
            return None

    def get_stats(self):
        return f'{str(self.player_a)}:{str(self.player_b)} - ' \
               f'{str(self.player_a.score)}:{str(self.player_b.score)}, ' \
               f'{str(self.draws)} draw(s)'