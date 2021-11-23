import unittest

from src.models import Player, Computer, Game, game_map


class TestPlayer(unittest.TestCase):
    name = 'Test'

    def test_make_move(self):
        player = Player(self.name)
        player.make_move(0)
        self.assertEqual(0, player.move)

    def test_get_move(self):
        player = Player(self.name)
        player.make_move(0)
        self.assertEqual(game_map[0], player.get_move())

    def test_set_scored(self):
        player = Player(self.name)
        self.assertEqual(0, player.score)
        player.set_scored()
        self.assertEqual(1, player.score)
        player.set_scored()
        self.assertEqual(2, player.score)


class TestComputer(unittest.TestCase):
    def test_init(self):
        computer = Computer()
        self.assertEqual('Computer', computer.name)

    def test_make_move(self):
        computer = Computer()
        computer.make_move()
        self.assertLessEqual(computer.move, 2)
        self.assertGreaterEqual(computer.move, 0)


class TestGame(unittest.TestCase):
    name_a = 'Test_A'
    name_b = 'Test_B'
    rounds = 4

    def test_init(self):
        player_a = Player(self.name_a)
        player_b = Player(self.name_b)
        game = Game(self.rounds, player_a, player_b)

        self.assertEqual(self.rounds, game.rounds)
        self.assertEqual(0, game.draws)

    def test_play_round(self):
        player_a = Player(self.name_a)
        player_b = Player(self.name_b)
        game = Game(self.rounds, player_a, player_b)

        # Draw case
        player_a.make_move(0)
        player_b.make_move(0)
        winner = game.play_round()
        self.assertIsNone(winner)
        self.assertEqual(0, player_a.score)
        self.assertEqual(0, player_b.score)
        self.assertEqual(1, game.draws)

        # Player A wins
        player_a.make_move(1)
        player_b.make_move(0)
        winner = game.play_round()
        self.assertIsInstance(winner, Player)
        self.assertEqual(self.name_a, winner.name)
        self.assertEqual(1, player_a.score)
        self.assertEqual(0, player_b.score)
        self.assertEqual(1, game.draws)

        # Player B wins
        player_a.make_move(1)
        player_b.make_move(2)
        winner = game.play_round()
        self.assertIsInstance(winner, Player)
        self.assertEqual(self.name_b, winner.name)
        self.assertEqual(1, player_a.score)
        self.assertEqual(1, player_b.score)
        self.assertEqual(1, game.draws)
