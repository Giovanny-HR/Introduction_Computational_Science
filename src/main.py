# Giovanny Marchena (16641485), Mees van Tol (15822311)
# run the tournament and print the ranking

"""Run the tournament and print the ranking."""

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
