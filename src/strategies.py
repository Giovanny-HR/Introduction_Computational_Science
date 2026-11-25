# Giovanny Marchena (16641485), <student 2 name> (<student id>)
# prisoner's dilemma strategies

"""All our prisoner's dilemma strategies live here.

How a strategy works in this project:
  a strategy is just a function. it gets two lists, my own past moves and the
  opponent's past moves (oldest first, each move is "C" or "D"), and it returns
  my next move, "C" or "D". the first round both lists are empty.

  example - copy whatever the opponent did last:
      def copycat(me, opp):
          if not opp:        # first round, nothing to copy yet
              return C
          return opp[-1]

at the bottom there is a STRATEGIES dict (name -> function). the tournament
loops over that dict, so a strategy only joins the game once it is listed there.

Strategies by Giovanny Marchena (16641485), one line each:
  suspicious_tft        copy the opponent, but open with defect
  cautious_reciprocator copy them, but wait one extra round before trusting again
  forgiving_tft         copy them, but offer peace after a both-defect round
  two_move_prober       watch their last two moves, punish any inconsistency
  trust_builder         cooperate while they have cooperated at least as much as defected
"""

C = "C"
D = "D"


# =====================================================================
# benchmark (the brief asks us to include tit for tat)
# =====================================================================

def tit_for_tat(me, opp):
    # cooperate first, then just copy what they did last
    if not opp:
        return C
    return opp[-1]


# =====================================================================
# reference opponents - not original, just handy to test against
# =====================================================================

def always_defect(me, opp):
    return D

def always_cooperate(me, opp):
    return C


# =====================================================================
# strategies by Giovanny Marchena (16641485)
# theme: reciprocity (how fast to forgive) plus one memory-based idea
# =====================================================================

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


# =====================================================================
# strategies by <student 2 name> (<student id>)
# add your five here, same shape as above: def name(me, opp): return C or D.
# then list each one in the STRATEGIES dict below so it joins the tournament.
# stub to copy:
#   def my_strategy(me, opp):
#       if not opp:
#           return C
#       return opp[-1]
# =====================================================================


# =====================================================================
# register every strategy here (name -> function). the tournament reads this.
# =====================================================================

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
    # --- <student 2>: add yours here, e.g. "my_strategy": my_strategy, ---
}
