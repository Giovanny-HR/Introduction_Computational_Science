# Giovanny Marchena (16641485), <student 2 name> (<student id>)
# pyics viewer for a single match

"""GUI for watching a single prisoner's dilemma match, built on pyics.

pyics is the same framework from the CA labs (bundled in this folder). you make
a Model, override reset / step / draw, and launch it with GUI(sim).start().

what this shows:
  pick two strategies by name and a number of rounds in the parameter boxes,
  press Reset, then Step (one round) or Run (all rounds). the picture is like
  the CA space-time diagram: each round is a column, the top row is player A and
  the bottom row is player B. a filled cell means cooperate, an empty one means
  defect. the current scores are in the title.

run it with:  python gui.py
"""

import numpy as np

from pyics.model import Model  # GUI imported later, only when launching
from strategies import STRATEGIES, C
from game import PAYOFF


class PDModel(Model):
    """One iterated prisoner's dilemma match, step by step."""

    def __init__(self):
        Model.__init__(self)
        # these three show up as editable boxes in the GUI
        self.make_param('strategy_a', 'tit_for_tat')
        self.make_param('strategy_b', 'always_defect')
        self.make_param('rounds', 50)
        self.reset()

    def reset(self):
        # look the names up in STRATEGIES, fall back to tit_for_tat if misspelled
        self.fn_a = STRATEGIES.get(self.strategy_a, STRATEGIES['tit_for_tat'])
        self.fn_b = STRATEGIES.get(self.strategy_b, STRATEGIES['tit_for_tat'])
        self.a_moves = []
        self.b_moves = []
        self.score_a = 0
        self.score_b = 0
        self.t = 0

    def step(self):
        # stop once we've played all the rounds
        if self.t >= self.rounds:
            return True
        move_a = self.fn_a(self.a_moves, self.b_moves)
        move_b = self.fn_b(self.b_moves, self.a_moves)
        self.score_a += PAYOFF[(move_a, move_b)]
        self.score_b += PAYOFF[(move_b, move_a)]
        self.a_moves.append(move_a)
        self.b_moves.append(move_b)
        self.t += 1

    def draw(self):
        # import pyplot here (pyics sets the backend first, so keep it local)
        import matplotlib.pyplot as plt

        # turn the two move lists into a 2-row grid: 1 = cooperate, 0 = defect
        row_a = [1 if m == C else 0 for m in self.a_moves]
        row_b = [1 if m == C else 0 for m in self.b_moves]
        if not row_a:            # nothing played yet, show an empty strip
            row_a, row_b = [0], [0]
        grid = np.array([row_a, row_b])

        plt.cla()
        plt.imshow(grid, aspect='auto', vmin=0, vmax=1, cmap='Greens')
        plt.yticks([0, 1], [self.strategy_a, self.strategy_b])
        plt.xlabel('round (filled = cooperate, empty = defect)')
        plt.title(f'{self.strategy_a}: {self.score_a}   vs   '
                  f'{self.strategy_b}: {self.score_b}')


if __name__ == '__main__':
    sim = PDModel()
    from pyics import GUI
    cx = GUI(sim)
    cx.start()
