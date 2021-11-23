import unittest
import unittest.mock as mock

from click.testing import CliRunner
from app import rps_game


def mock_computer_move(cls, *args, **kwargs):
    return 0


class TestController(unittest.TestCase):
    def test_rps_game(self):
        with mock.patch('random.randint', mock_computer_move):
            runner = CliRunner()
            result = runner.invoke(rps_game, input='3\nDenis\n0\n1\n2\n')
            self.assertFalse(result.exception)
            self.assertEqual(result.exit_code, 0)
            self.assertIn('Rounds [1]: 3', result.output)
            self.assertIn('Denis moved with rock, Computer moved with rock.', result.output)
            self.assertIn('Denis moved with paper, Computer moved with rock.', result.output)
            self.assertIn('Denis moved with scissors, Computer moved with rock.', result.output)
            self.assertIn('Denis:Computer - 1:1, 1 draw(s)', result.output)
