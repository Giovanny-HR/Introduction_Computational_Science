# Giovanny Marchena (16641485), Mees van Tol (15822311)
# prisoner's dilemma strategies

"""Our prisoner's dilemma strategies.

each strategy is a function (me, opp) -> "C"/"D" from the two move histories.
add one to the STRATEGIES dict at the bottom to put it in the tournament.
"""

import random

C = "C"
D = "D"


# benchmark: tit for tat (required by the brief)

def tit_for_tat(me, opp):
    # cooperate first, then just copy what they did last
    if not opp:
        return C
    return opp[-1]


# reference opponents, just for testing

def always_defect(me, opp):
    return D

def always_cooperate(me, opp):
    return C


# my strategies

def suspicious_tft(me, opp):
    # tit for tat but starts mean. tests if a distrustful opening pays off
    if not opp:
        return D
    return opp[-1]


def cautious_reciprocator(me, opp):
    # copy them, but after a betrayal wait one extra round before trusting again
    if not opp:
        return C
    # they just went back to C but i was still punishing -> hold one more round
    if opp[-1] == C and me and me[-1] == D:
        return D
    return opp[-1]


def forgiving_tft(me, opp):
    # tit for tat, but if we BOTH just defected, offer peace to break the loop
    if not opp:
        return C
    if me and me[-1] == D and opp[-1] == D:
        return C
    return opp[-1]


def two_move_prober(me, opp):
    # look at their last two moves. steady cooperator -> C, anything shaky -> D.
    # this is the harder one: it needs two rounds of history, not one.
    if len(opp) < 2:
        return C  # first two moves: give them a chance
    last_two = opp[-2:]
    if last_two == [C, C]:
        return C
    return D  # both D, or mixed -> treat as a threat


def trust_builder(me, opp):
    # trust grows with their behaviour: cooperate while they have cooperated
    # at least as often as they have defected, otherwise pull back.
    # mirror image of the prober (prober punishes, this one rewards).
    if not opp:
        return C
    if opp.count(C) >= opp.count(D):
        return C
    return D


def exploiter(me, opp):
    # exploits forgiving strategies by alternating between cooperating and defecting
    if len(opp) % 2 == 1:
        return C
    return D


def grudge(me, opp):
    # cooperates until betrayed then defects every following round
    if not opp:
        return C
    if opp[-1] == D or me[-1] == D:
        return D
    return C


def probabilistic(me, opp):
    # cooperates and defects at random
    return random.choice([C,D])


def generous(me, opp):
    # cooperates until opponent defects twice in a row
    if len(opp) < 2:
        return C
    if opp[-1] == D and opp[-2] == D:
        return D
    return C


def leg_up_tft(me, opp):
    # tit for that but it defects on random moments
    # it is more likely to defect the longer both parties cooperate
    # it detects whenever it reinstated trust and then defects more often
    if not opp:
        return C

    me_len = len(me)
    opp_len = len(opp)

    length = 0
    for i in range(me_len):
        if me[me_len - i - 1] == C:
            length += 1
        else:
            break
    num_coop = length

    length = 0
    for i in range(opp_len):
        if opp[opp_len - i - 1] == C:
            length += 1
        else:
            break

    if length < num_coop:
        num_coop = length

    if random.randint(1, me_len) <= num_coop:
        return D
    else:
        return opp[-1]



# all strategies the tournament plays

STRATEGIES = {
    "tit_for_tat": tit_for_tat,
    "always_defect": always_defect,
    "always_cooperate": always_cooperate,
    # --- Giovanny Marchena (16641485) ---
    "suspicious_tft": suspicious_tft,
    "cautious_reciprocator": cautious_reciprocator,
    "forgiving_tft": forgiving_tft,
    "two_move_prober": two_move_prober,
    "trust_builder": trust_builder,
    # --- Mees van Tol (15822311) ---
    "exploiter": exploiter,
    "grudge": grudge,
    "probabilistic": probabilistic,
    "generous": generous,
    "leg_up_tft": leg_up_tft,
}
