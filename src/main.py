# Introduction Computational Science - GT lab (iterated prisoner's dilemma)
# Giovanny Marchena (16641485)
# <student 2 name> (<student id>)
#
# file: main.py

"""Run this file to play the tournament and print the ranking.

how the files fit together:
  strategies.py  -> defines each strategy and lists them in STRATEGIES
  game.py        -> plays one match between two strategies (the payoff table)
                    and has show_match() for round-by-round debugging
  tournament.py  -> plays every pair, adds up the scores
  main.py        -> this file, runs the tournament and prints the result

the GUI is a separate piece we have not built yet. see gui.py for the plan.
run it from inside this folder with:  python main.py
"""

from strategies import STRATEGIES
from game import show_match
from tournament import run_tournament

ROUNDS = 200  # the brief uses 200 encounters per pair

totals = run_tournament(STRATEGIES, ROUNDS)

# sort best to worst
ranking = sorted(totals.items(), key=lambda kv: kv[1], reverse=True)

print(f"tournament, {ROUNDS} rounds per match")
print("-" * 40)
for place, (name, score) in enumerate(ranking, start=1):
    print(f"{place:>2}. {name:<22} {score}")

# example match, printed round by round, so you can see a strategy actually work.
# change the two names to debug any pair you like.
print()
print("example match (first 10 rounds) for debugging:")
show_match(
    STRATEGIES["forgiving_tft"], STRATEGIES["always_defect"],
    "forgiving_tft", "always_defect",
    rounds=10,
)
