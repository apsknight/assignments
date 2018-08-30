"""
    FLAT Assignment #1: Epsilon NFA to DFA Conversion Program
    Submitted by: Aman Pratap Singh, 16CS01011
"""
import Queue
import json

print("Epsilon NFA to DFA Conversion Program")
print("Alphabets available in language are: 0, 1 and epsilon")

nfa_states_count = int(raw_input("Enter number of NFA States: "))
nfa = dict()

print("Created following NFA states:"),
for i in range(nfa_states_count):
    nfa[chr(ord('A') + i)] = dict()
    nfa[chr(ord('A') + i)]['0'] = list()
    nfa[chr(ord('A') + i)]['1'] = list()
    nfa[chr(ord('A') + i)]['eps'] = list()
    print(chr(ord('A') + i)),
print("\n")

print("Enter space seperated states corresponding to transition. For e.g. A B C etc.")
print("Leave empty if no state is present corresponding to transition.\n")
for key, value in nfa.items():
    nfa[key]['0'] = str(raw_input("%s->0: " % key)).split()
    nfa[key]['1'] = str(raw_input("%s->1: " % key)).split()
    nfa[key]['eps'] = str(raw_input("%s->eps: " % key)).split()

print("\nThe Epsilon NFA is: ")
print(json.dumps(nfa, sort_keys=True, indent=4))

# nfa = {
#     'A' : {
#         '0'  : ['B', 'C'],
#         '1'  : ['A'],
#         'eps': ['B']
#     },
#     'B' : {
#         '0'  : [],
#         '1'  : ['B'],
#         'eps': ['C']
#     },
#     'C' : {
#         '0'  : ['C'],
#         '1'  : ['C'],
#         'eps': []
#     }
# }

dfa = dict()

start = str(raw_input("Enter NFA's Start State: "))
final = str(raw_input("Enter NFA's Final State: "))

eps_closure_start = set()

q = Queue.Queue()
q.put(start)
visited = []

while not q.empty():
    current = q.get()
    visited.append(current)
    for state in nfa[current]['eps']:
        eps_closure_start.add(state)
        if state not in visited:
            q.put(state)

# Add epsilon transition in start state
final_start = start
for state in eps_closure_start:
    final_start = final_start + state
final_start = "".join(sorted(set(final_start)))


dfa = dict()
dfa_q = Queue.Queue()
dfa_q.put(final_start)
final_visited = list()
final_visited.append(final_start)

while not dfa_q.empty():
    state = dfa_q.get()
    if not state in dfa:
        dfa[state] = dict()
    this_state = ""
    for alphabet in state:
        for alphabet_state in nfa[alphabet]["0"]:
            this_state = this_state + alphabet_state
            for eps_state in nfa[alphabet_state]["eps"]:
                this_state = this_state + eps_state
    this_state = "".join(sorted(set(this_state)))

    if this_state not in final_visited and this_state != "":
        final_visited.append(this_state)
        dfa_q.put(this_state)
    dfa[state]["0"] = this_state
    this_state = ""
    for alphabet in state:
        for alphabet_state in nfa[alphabet]["1"]:
            this_state = this_state + alphabet_state
            for eps_state in nfa[alphabet_state]["eps"]:
                this_state = this_state + eps_state
    this_state = "".join(sorted(set(this_state)))
    if this_state not in final_visited and this_state != "":
        final_visited.append(this_state)
        dfa_q.put(this_state)
    dfa[state]["1"] = this_state

dfa_final_states = list()
for key in dfa:
    if final in key:
        dfa_final_states.append(key)

print("\nThe DFA is: ")
print(json.dumps(dfa, sort_keys=True, indent=4))
print("DFA Start state: %s" % final_start)
print("DFA Final states: %s" % dfa_final_states)