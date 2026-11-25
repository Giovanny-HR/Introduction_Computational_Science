# Giovanny Marchena (16641485), <student 2 name> (<student id>)
# one match and the payoff table

"""One match between two strategies, scored with the brief's payoff table."""

from strategies import C, D

# payoff table from the brief. key is (my move, their move) -> my points.
PAYOFF = {
    (C, C): 3,   # both cooperate (reward)
    (C, D): 0,   # i cooperated, they defected (sucker)
    (D, C): 5,   # i defected on a cooperator (temptation)
    (D, D): 1,   # both defect (punishment)
}


def play_match(strat_a, strat_b, rounds=200):
    """Play two strategies against each other and return (score_a, score_b)."""
    a_moves, b_moves = [], []   # histories, oldest move first
    score_a, score_b = 0, 0

    for _ in range(rounds):
        # each player sees its own history first, then the opponent's
        move_a = strat_a(a_moves, b_moves)
        move_b = strat_b(b_moves, a_moves)

        score_a += PAYOFF[(move_a, move_b)]
        score_b += PAYOFF[(move_b, move_a)]

        a_moves.append(move_a)
        b_moves.append(move_b)

    return score_a, score_b


def show_match(strat_a, strat_b, name_a="A", name_b="B", rounds=10):
    """Play a match and print it round by round (for debugging)."""
    a_moves, b_moves = [], []
    score_a, score_b = 0, 0
    print(f"{name_a}  vs  {name_b}")
    print(f"{'round':>5} {name_a:>22} {name_b:>22}   running score")
    for t in range(1, rounds + 1):
        move_a = strat_a(a_moves, b_moves)
        move_b = strat_b(b_moves, a_moves)
        score_a += PAYOFF[(move_a, move_b)]
        score_b += PAYOFF[(move_b, move_a)]
        a_moves.append(move_a)
        b_moves.append(move_b)
        print(f"{t:>5} {move_a:>22} {move_b:>22}   {score_a} - {score_b}")
    print(f"final after {rounds} rounds: {name_a} {score_a}, {name_b} {score_b}")
