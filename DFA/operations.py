from DFA import dfa


def intersection(dfa1, dfa2):
    assert(dfa1.alphabet == dfa2.alphabet)

    states = []
    for s1 in dfa1.states:
        for s2 in dfa2.states:
            states.append((s1, s2))

    initial_state = (dfa1.initial_state, dfa2.initial_state)

    transition_table = {}
    for state_pair in states:
        state_dict = {}
        for inp in dfa1.alphabet:
            state_dict[inp] = (dfa1.transition_table[state_pair[0]][inp], dfa2.transition_table[state_pair[1]][inp])

        transition_table[state_pair] = state_dict

    end_states = []
    for (s1, s2) in states:
        if s1 in dfa1.end_states and s2 in dfa2.end_states:
            end_states.append((s1, s2))

    return dfa(states=states,
               alphabet=dfa1.alphabet,
               initial_state=initial_state,
               transition_table=transition_table,
               end_states=end_states)


def union(dfa1, dfa2):
    assert(dfa1.alphabet == dfa2.alphabet)

    states = []
    for s1 in dfa1.states:
        for s2 in dfa2.states:
            states.append((s1,s2))

    initial_state = (dfa1.initial_state, dfa2.initial_state)

    transition_table = {}
    for state_pair in states:
        state_dict = {}
        for inp in dfa1.alphabet:
            state_dict[inp] = (dfa1.transition_table[state_pair[0]][inp], dfa2.transition_table[state_pair[1]][inp])

        transition_table[state_pair] = state_dict

    end_states = []
    for (s1, s2) in states:
        if s1 in dfa1.end_states or s2 in dfa2.end_states:
            end_states.append((s1, s2))

    return dfa(states=states,
               alphabet=dfa1.alphabet,
               initial_state=initial_state,
               transition_table=transition_table,
               end_states=end_states)


def inverse(dfa):
    end_states = []
    for state in dfa.states:
        if state not in dfa.end_states:
            end_states.append(state)

    return dfa(states=dfa.states,
               alphabet=dfa.alphabet,
               initial_state=dfa.initial_state,
               end_states=end_states,
               transition_table=dfa.transition_table)


with open('dfa1.json', 'r') as f:
    dfa1 = dfa.from_json(f.read())

with open('dfa2.json', 'r') as f:
    dfa2 = dfa.from_json(f.read())

dfa3 = union(dfa1, dfa2)

dfa3.pretty_print()
print(dfa3.run("1010"))
print(dfa3.run(""))
print(dfa3.run("010"))
print(dfa3.run("101"))
print(dfa3.run("1100"))
print(dfa3.run("10101"))
print(dfa3.run("10100"))
print(dfa3.run("101010"))
print(dfa3.run("10101001"))

