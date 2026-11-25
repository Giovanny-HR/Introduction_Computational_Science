# Giovanny Marchena (16641485), <student 2 name> (<student id>)
# genetic algorithm for the tournament

"""Genetic algorithm that evolves a memory-1 strategy.

chromosome = [first move, reply to CC, CD, DC, DD].
fitness = total score against the strategies in STRATEGIES.
"""

import random

from strategies import STRATEGIES
from game import play_match

C, D = "C", "D"

# the four situations a memory-1 strategy must answer, in a fixed order.
# a chromosome's genes 1..4 line up with these.
KEYS = [(C, C), (C, D), (D, C), (D, D)]


def random_chromosome():
    return [random.choice([C, D]) for _ in range(5)]


def as_function(chrom):
    """Turn a chromosome into a strategy function the tournament can play."""
    first = chrom[0]
    table = dict(zip(KEYS, chrom[1:]))

    def strat(me, opp):
        if not opp:                      # first round, no history yet
            return first
        return table[(me[-1], opp[-1])]
    return strat


def fitness(chrom, opponents, rounds=200):
    """How good a strategy is: its total score against every opponent."""
    me = as_function(chrom)
    return sum(play_match(me, opp, rounds)[0] for opp in opponents)


def crossover(parent1, parent2):
    # one-point crossover
    cut = random.randint(1, len(parent1) - 1)
    return parent1[:cut] + parent2[cut:]


def mutate(chrom, rate=0.1):
    # flip genes at random
    return [(D if g == C else C) if random.random() < rate else g for g in chrom]


def evolve(generations=30, pop_size=20, rounds=200, seed=0):
    """Run the GA. Returns the best strategy found and the best-score history."""
    random.seed(seed)
    opponents = list(STRATEGIES.values())

    population = [random_chromosome() for _ in range(pop_size)]
    history = []

    for _ in range(generations):
        ranked = sorted(population, key=lambda c: fitness(c, opponents, rounds),
                        reverse=True)
        best = ranked[0]
        history.append(fitness(best, opponents, rounds))

        parents = ranked[:pop_size // 2]

        # keep best (elitism), breed the rest
        new_population = [best]
        while len(new_population) < pop_size:
            p1, p2 = random.sample(parents, 2)
            child = mutate(crossover(p1, p2))
            new_population.append(child)
        population = new_population

    return best, history


def save_plot(history, path="figures/ga_fitness.png"):
    # best fitness per generation, saved as a figure for the report
    import os
    import matplotlib
    matplotlib.use("Agg")                   # no window, just save a file
    import matplotlib.pyplot as plt
    os.makedirs(os.path.dirname(path), exist_ok=True)
    plt.figure()
    plt.plot(range(1, len(history) + 1), history, marker="o",
             label="best strategy in the population")
    plt.xlabel("generation number")
    plt.ylabel("fitness = total payoff against the whole field")
    plt.title("Genetic algorithm: best strategy fitness per generation")
    plt.legend()                 # label the line so the plot is self-explaining
    plt.grid(True, alpha=0.3)    # light grid so values are easy to read
    plt.tight_layout()
    plt.savefig(path)
    print("saved plot to", path)


if __name__ == "__main__":
    best, history = evolve()

    first = best[0]
    table = dict(zip(KEYS, best[1:]))
    print("best evolved strategy")
    print("  first move:", first)
    for k in KEYS:
        print(f"  after {k} -> {table[k]}")
    print("fitness went:", history)

    try:
        save_plot(history)
    except Exception as e:
        print("(skipped plot:", e, ")")
