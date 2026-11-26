# Giovanny Marchena (16641485), Mees van Tol (15822311)
# pyics viewer for a single match

"""Watch one match in a window, using the pyics framework from the CA labs.

pick two strategies and a round count, then Reset and Step or Run. each round is
a column: top row player A, bottom row player B, filled = cooperate. the payoff
values are editable too, so you can see how changing the game changes the match.
"""

import numpy as np

from pyics.model import Model  # GUI imported later, only when launching
from strategies import STRATEGIES, C, D


class PDModel(Model):
    """One iterated prisoner's dilemma match, step by step."""

    def __init__(self):
        Model.__init__(self)
        # the two players and how many rounds (editable in the GUI)
        self.make_param('strategy_a', 'tit_for_tat')
        self.make_param('strategy_b', 'always_defect')
        self.make_param('rounds', 50)
        # payoff values, so you can experiment with the game itself
        self.make_param('both_cooperate', 3)   # reward
        self.make_param('i_defect_alone', 5)    # temptation
        self.make_param('both_defect', 1)       # punishment
        self.make_param('i_cooperate_alone', 0)  # sucker
        self.reset()

    def reset(self):
        # look the names up, fall back to tit_for_tat if one is misspelled
        self.fn_a = STRATEGIES.get(self.strategy_a, STRATEGIES['tit_for_tat'])
        self.fn_b = STRATEGIES.get(self.strategy_b, STRATEGIES['tit_for_tat'])
        # build the payoff table from the current parameters
        self.payoff = {
            (C, C): self.both_cooperate,
            (C, D): self.i_cooperate_alone,
            (D, C): self.i_defect_alone,
            (D, D): self.both_defect,
        }
        self.a_moves = []
        self.b_moves = []
        self.score_a = 0
        self.score_b = 0
        self.t = 0

    def step(self):
        # stop once all rounds are played
        if self.t >= self.rounds:
            return True
        move_a = self.fn_a(self.a_moves, self.b_moves)
        move_b = self.fn_b(self.b_moves, self.a_moves)
        self.score_a += self.payoff[(move_a, move_b)]
        self.score_b += self.payoff[(move_b, move_a)]
        self.a_moves.append(move_a)
        self.b_moves.append(move_b)
        self.t += 1

    def draw(self):
        # pyplot imported here (pyics sets the backend first)
        import matplotlib.pyplot as plt

        # two rows, 1 = cooperate, 0 = defect
        row_a = [1 if m == C else 0 for m in self.a_moves]
        row_b = [1 if m == C else 0 for m in self.b_moves]
        if not row_a:
            row_a, row_b = [0], [0]
        grid = np.array([row_a, row_b])

        plt.cla()
        plt.imshow(grid, aspect='auto', vmin=0, vmax=1, cmap='Greens')
        plt.yticks([0, 1], ['[1]', '[2]'],
                   fontsize=12, fontweight='bold', color='black')
        plt.xlabel('round (filled = cooperate, empty = defect)')
        plt.title(f'{self.strategy_a} [1]: {self.score_a}   vs   '
                  f'{self.strategy_b} [2]: {self.score_b}')


if __name__ == '__main__':
    sim = PDModel()
    from pyics import GUI
    cx = GUI(sim)
    cx.start()
