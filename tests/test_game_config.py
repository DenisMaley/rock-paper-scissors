import unittest
from src.game_config import game_rules_matrix, game_moves_map


class TestGameConfig(unittest.TestCase):
    def test_rules_consistence(self):
        self.assertEqual(len(game_rules_matrix), len(game_moves_map))
