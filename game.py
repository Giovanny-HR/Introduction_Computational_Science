import strategies

def check_payoff(choice1, choice2, payoff_win, payoff_coop, payoff_defect, payoff_loss):
    if choice1 == "C" and choice2 == "C":
        return payoff_coop, payoff_coop

    if choice1 == "D" and choice2 == "C":
        return payoff_win, payoff_loss

    if choice1 == "C" and choice2 == "D":
        return payoff_loss, payoff_win

    if choice1 == "D" and choice2 == "D":
        return payoff_defect, payoff_defect

    return 0


def game(strategy1, strategy2, payoff_win, payoff_coop, payoff_defect, payoff_loss, length):
    strat1_history = []
    strat2_history = []
    strat1_total = 0
    strat2_total = 0

    for _ in range(length):
        choice1 = strategy1.decide(strat1_history, strat2_history)
        choice2 = strategy2.decide(strat2_history, strat1_history)

        strat1_history.append(choice1)
        strat2_history.append(choice2)

        points1, points2 = check_payoff(choice1, choice2, payoff_win, payoff_coop, payoff_defect, payoff_loss)
        strat1_total += points1
        strat2_total += points2

    return strat1_total, strat2_total