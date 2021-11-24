# Game rules
# Scissors cuts Paper
# Paper covers Rock
# Rock crushes Scissors

game_rules_matrix = [
    [-1, 1, 0],
    [1, -1, 2],
    [0, 2, -1]
]

game_moves_map = {0: 'rock', 1: 'paper', 2: 'scissors'}

# Game rules
# Scissors cuts Paper
# Paper covers Rock
# Rock crushes Lizard
# Lizard poisons Spock
# Spock smashes Scissors
# Scissors decapitates Lizard
# Lizard eats Paper
# Paper disproves Spock
# Spock vaporizes Rock
# Rock crushes Scissors

# game_rules_matrix = [
#     [-1, 1, 0, 0, 4],
#     [1, -1, 2, 3, 1],
#     [0, 2, -1, 2, 4],
#     [0, 3, 2, -1, 3],
#     [4, 1, 4, 3, -1]
# ]
# game_moves_map = {0: "rock", 1: "paper", 2: "scissors", 3: "lizard", 4: "spock"}

reversed_game_moves_map = {v: k for k, v in game_moves_map.items()}
moves = reversed_game_moves_map.keys()

MOVES_NUM = len(game_rules_matrix)
MIN_ROUNDS = 1
MAX_ROUNDS = 10
