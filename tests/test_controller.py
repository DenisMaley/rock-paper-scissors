import unittest

from src import Controller
from src.models import Player, Computer, Game


class TestController(unittest.TestCase):
    rounds = 7
    name = 'Test'

    def test_set_player(self):
        player = Controller.set_player(self.name)
        self.assertIsInstance(player, Player)
        self.assertEqual(self.name, player.name)

    def test_set_computer_player(self):
        computer_player = Controller.set_computer_player()
        self.assertIsInstance(computer_player, Player)
        self.assertIsInstance(computer_player, Computer)
        self.assertEqual('Computer', computer_player.name)

    def test_set_game(self):
        player_a = Controller.set_player(self.name)
        player_b = Controller.set_computer_player()
        game = Controller.set_game(self.rounds, player_a, player_b)

        self.assertIsInstance(game, Game)
        self.assertEqual(self.rounds, game.rounds)
        self.assertEqual(0, game.draws)
