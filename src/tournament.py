# Giovanny Marchena (16641485), <student 2 name> (<student id>)
# round-robin tournament

"""Round robin: every strategy plays every other once, scores add up."""

from game import play_match


def run_tournament(strategies, rounds=200):
    """Play all pairs and return {name: total score}."""
    totals = {name: 0 for name in strategies}   # everyone starts at zero

    names = list(strategies)
    # i and j pick each pair once (j starts after i, so no repeats, no self-play)
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            a, b = names[i], names[j]
            score_a, score_b = play_match(strategies[a], strategies[b], rounds)
            totals[a] += score_a
            totals[b] += score_b

    return totals
