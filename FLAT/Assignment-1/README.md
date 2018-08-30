# FLAT Assignment #1: Epsilon NFA to DFA Conversion Program
### Submitted by: Aman Pratap Singh, 16CS01011

## Algorithm of convesion:
1. Take ∈ closure for the beginning state of NFA as beginning state of DFA.
2. Find the states that can be traversed from the present for each input symbol (union of transition value and their closures for each states of NFA present in current state of DFA).
3. If any new state is found take it as current state and repeat step 2.
4. Do repeat Step 2 and Step 3 until no new state present in DFA transition table.
5. Mark the states of DFA which contains final state of NFA as final states of DFA.

## How to run program:
In the bash terminal, type following commands
```bash
python2 nfa_to_dfa.py
```
or open this [IPython notebook](nfa_to_dfa.ipynb) to see result with default inputs.