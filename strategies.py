import random

class Strategy:
    def __init__(self, name, initial_choice, rule, memory, strategy_type):
        """
        :param name: name of the strategy
        :param initial_choice: first choice made without any history
        :param rule: choices are made based off this list. Size = 2^(memory + 1)
        :param memory: number of moves required to make a choice
        :param strategy_type: type of strategy
        """
        self.name = name
        self.initial_choice = initial_choice
        self.rule = rule
        self.memory = memory
        self.strategy_type = strategy_type

    def decide(self, own_history, opp_history):
        """
        Determines the next choice
        """
        if self.strategy_type == "random":
            # Returns a random choice
            return random.choice(["C", "D"])

        if self.strategy_type == "rule":
            # Returns a choice based on a rule table
            if len(opp_history) == 0:
                return self.initial_choice

            own_previous_moves = tuple(own_history[-self.memory:])
            opp_previous_moves = tuple(
                opp_history[-self.memory:]
            )

            key = (own_previous_moves, opp_previous_moves)
            return self.rule[key]

        if self.strategy_type == "leg_up":
            # TFT but is more likely to defect the longer both parties cooperate
            own_len = len(own_history)

            if own_len == 0:
                return self.initial_choice

            opp_len = len(opp_history)

            length = 0
            for i in range(own_len):
                if own_history[own_len - i - 1] == "C":
                    length += 1
                else:
                    break
            num_coop = length

            length = 0
            for i in range(opp_len):
                if opp_history[opp_len - i - 1] == "C":
                    length += 1
                else:
                    break

            if length < num_coop:
                num_coop = length

            if random.randint(1, 10) < num_coop:
                return "D"
            else:
                return opp_history[-1]

        return self.initial_choice
