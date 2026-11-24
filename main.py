import strategies
import game
import tournament

def main():
    all_strats = []

    rule1 = {
        (("D",), ("C",)): "D",
        (("D",), ("D",)): "D"
    }
    exploiter = strategies.Strategy("exploiter", "D", rule=rule1, memory=1, strategy_type="rule")
    all_strats.append(exploiter)

    rule2 = {
        (("C",), ("C",)): "C",
        (("C",), ("D",)): "D",
        (("D",), ("C",)): "D",
        (("D",), ("D",)): "D"
    }
    grudge = strategies.Strategy("grudge", "C", rule=rule2, memory=1, strategy_type="rule")
    all_strats.append(grudge)

    probabilistic = strategies.Strategy("probabilistic", None,
                                        rule=None, memory=None, strategy_type="random")
    all_strats.append(probabilistic)

    rule3 = {
        (("C",), ("C",)): "C",
        (("C",), ("D",)): "C",
        (("D",), ("C",)): "C",
        (("D",), ("D",)): "C",

        (("C", "C"), ("C", "C")): "C",
        (("C", "C"), ("D", "C")): "C",
        (("C", "C"), ("C", "D")): "C",
        (("C", "C"), ("D", "D")): "D",

        (("D", "C"), ("C", "C")): "C",
        (("D", "C"), ("D", "C")): "C",
        (("D", "C"), ("C", "D")): "C",
        (("D", "C"), ("D", "D")): "D",

        (("C", "D"), ("C", "C")): "D",
        (("C", "D"), ("C", "D")): "D",
        (("C", "D"), ("D", "C")): "D",
        (("C", "D"), ("D", "D")): "D",

        (("D", "D"), ("C", "C")): "D",
        (("D", "D"), ("C", "D")): "D",
        (("D", "D"), ("D", "C")): "D",
        (("D", "D"), ("D", "D")): "D",
    }
    generous = strategies.Strategy("generous", "C", rule=rule3, memory=2, strategy_type="rule")
    all_strats.append(generous)

    leg_up = strategies.Strategy("leg_up", "D", rule=None, memory=None, strategy_type="leg_up")
    all_strats.append(leg_up)

    tournament.start_tournament(all_strats, 5, 3, 1, 0, 50)

if __name__ == "__main__":
    main()