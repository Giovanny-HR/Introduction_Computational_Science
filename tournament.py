import itertools
import game
import strategies

def start_tournament(strategies, payoff_win, payoff_coop, payoff_defect, payoff_loss, game_length):
    scores = {strategy: 0 for strategy in strategies}

    for strategy1, strategy2 in itertools.combinations(strategies, 2):

        points1, points2 = game.game(
            strategy1,
            strategy2,
            payoff_win,
            payoff_coop,
            payoff_defect,
            payoff_loss,
            game_length
        )

        scores[strategy1] += points1
        scores[strategy2] += points2

    print("Tournament results:")
    for strategy, score in scores.items():
        print(f"{strategy.name}: {score} points")

    return scores