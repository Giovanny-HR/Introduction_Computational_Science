# Giovanny Marchena (16641485), Mees van Tol (15822311)
# my five strategies as rule tables
#
# My five strategies written for Mees's Strategy class (strategies.py).
# The rule tables match my function versions exactly.
# Key format is Mees's: (own_previous_moves, opp_previous_moves) -> next move,
# both as tuples of length `memory`.

from strategies import Strategy

C, D = "C", "D"

# 1. Suspicious TFT: copy the opponent, but open with D.
suspicious_tft = Strategy(
    name="suspicious_tft", initial_choice=D, memory=1, strategy_type="Rule",
    rule={
        (("C",), ("C",)): C,
        (("C",), ("D",)): D,
        (("D",), ("C",)): C,
        (("D",), ("D",)): D,
    },
)

# 2. Cautious Reciprocator: copy them, but defect one extra round before trusting again.
cautious_reciprocator = Strategy(
    name="cautious_reciprocator", initial_choice=C, memory=1, strategy_type="Rule",
    rule={
        (("C",), ("C",)): C,
        (("C",), ("D",)): D,
        (("D",), ("C",)): D,
        (("D",), ("D",)): D,
    },
)

# 3. Forgiving TFT: copy them, but offer peace after a both-defect round.
forgiving_tft = Strategy(
    name="forgiving_tft", initial_choice=C, memory=1, strategy_type="Rule",
    rule={
        (("C",), ("C",)): C,
        (("C",), ("D",)): D,
        (("D",), ("C",)): C,
        (("D",), ("D",)): C,
    },
)

# 4. Two-Move Prober: watch the opponent's last two moves, punish any inconsistency.
#    NOTE: memory=2, so decide() must return initial_choice while fewer than 2
#    moves have been played otherwise the key is too short. 16 rows.
two_move_prober = Strategy(
    name="two_move_prober", initial_choice=C, memory=2, strategy_type="Rule",
    rule={
        (("C", "C"), ("C", "C")): C, (("C", "C"), ("C", "D")): D,
        (("C", "C"), ("D", "C")): D, (("C", "C"), ("D", "D")): D,
        (("C", "D"), ("C", "C")): C, (("C", "D"), ("C", "D")): D,
        (("C", "D"), ("D", "C")): D, (("C", "D"), ("D", "D")): D,
        (("D", "C"), ("C", "C")): C, (("D", "C"), ("C", "D")): D,
        (("D", "C"), ("D", "C")): D, (("D", "C"), ("D", "D")): D,
        (("D", "D"), ("C", "C")): C, (("D", "D"), ("C", "D")): D,
        (("D", "D"), ("D", "C")): D, (("D", "D"), ("D", "D")): D,
    },
)

# 5. Trust-Builder: cooperate while the opponent has cooperated at least as much
#    as they have defected. This looks at the WHOLE history (a running count),
#    not a fixed window, so it is NOT a "Rule" and NOT "Random". It needs its own
#    strategy_type, e.g. "Count", added to Strategy.decide. Until we decide that,
#    this one is left out. (Alternative: swap it for another rule-based strategy.)

my_strategies = [
    suspicious_tft,
    cautious_reciprocator,
    forgiving_tft,
    two_move_prober,
    # trust_builder: pending a new strategy_type, see note above
]
