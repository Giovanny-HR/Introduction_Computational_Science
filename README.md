# Game Theory

Iterated Prisoner's Dilemma tournament: strategies play repeated rounds against each other and accumulate payoffs.

## Structure

- Root - cloned reference implementation from [Introduction_Computational_Science](https://github.com/Giovanny-HR/Introduction_Computational_Science)
  - `game.py` - payoff rules for a single round
  - `strategies.py` - strategy definitions (rule-based and random)
  - `tournament.py` - round-robin tournament runner
  - `main.py` - entry point, defines the strategy pool and runs the tournament
- `src/` - own implementation
  - `game.py`, `strategies.py`, `gm_strategies.py`, `tournament.py`, `main.py`, `gui.py`
  - `pyics/` - cellular automata/model utilities used by `gui.py`
  - `requirements.txt` - dependencies (numpy, matplotlib)
- `docs/` - notes and write-up

## Run

Reference implementation:
```
python main.py
```

Own implementation:
```
cd src
pip install -r requirements.txt
python main.py
```
