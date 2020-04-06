from DFA.DFA import DFA
from NFA import NFA


def nfa_to_dfa(nfa):
    # Create new transition table for the new DFA.
    transition_table = {}

    # Create new array of states. Used to add new states that we find when creating the DFA.
    states = [(nfa.initial_state, )]

    # Iterate over known states of the new DFA. New DFA's states are tuples to account for new
    # hybrid states like (q0, q1).
    for states_tuple in states:
        # Dict that will be filled and then added to the new transition table.
        state_dict = {}

        # Check every single input from the NFA's alphabet
        for inp in nfa.alphabet:
            # Array that stores all possible destination states after an input 'inp'.
            # Will be converted to a set, to deduplicate values, and then a tuple, for structural consistency.
            state_array = []

            # Check every state in the state tuple of the new DFA. Ex. if a state of the new DFA is (q0, q1) then we
            # check each tuple item and access the NFA's transition table to find all possible destination states.
            for state in states_tuple:
                # Adds new found states from the NFA's transition table to state_array
                state_array += nfa.transition_table[state][inp]

            # Dedup and tuple
            tuple_array = tuple(set(state_array))

            # Add tuple to state_dict. State_dict holds all possible destination states and inputs for the current state
            # tuple of the new DFA
            state_dict[inp] = tuple_array

            # If the newly created tuple is not empty and it isn't part of the known states of the new DFA, then we add
            # it as a new state of the new DFA. We will then iterate over this new state after coming back to line 14.
            if tuple_array and tuple_array not in states:
                states.append(tuple_array)

        # Adds state_dict as  a value to the new transition table, with state_tuple as the key.
        transition_table[states_tuple] = state_dict

    # Creates new end_states. If an existing state of the new DFA holds an end state of the old NFA, then we must add it
    # as an end_state.
    end_states = []
    for states_tuple in states:
        for state in nfa.end_states:
            if state in states_tuple:
                end_states.append(states_tuple)

    return DFA(states=states,
               alphabet=nfa.alphabet,
               initial_state=nfa.initial_state,
               transition_table=transition_table,
               end_states=end_states)


def nfa_to_dfa_with_e(nfa):
    # Add E closure column (E*) to transition table
    _e_closure(nfa)

    # Create new transition table for the new DFA.
    transition_table = {}

    # Create new array of states. Used to add new states that we find when creating the DFA.
    initial_state = tuple(nfa.transition_table[nfa.initial_state]['E*'])
    states = [tuple(initial_state)]
    alphabet = [] + nfa.alphabet
    alphabet.remove('E')

    # Iterate over known states of the new DFA. New DFA's states are tuples to account for new
    # hybrid states like (q0, q1).
    for states_tuple in states:
        # Dict that will be filled and then added to the new transition table.
        state_dict = {}

        # Check every single input from the NFA's alphabet
        for inp in alphabet:

            # Array that stores all possible destination states after an input 'inp'.
            # Will be converted to a set, to deduplicate values, and then a tuple, for structural consistency.
            state_array = []

            # Check every state in the state tuple of the new DFA. Ex. if a state of the new DFA is (q0, q1) then we
            # check each tuple item and access the NFA's transition table to find all possible destination states.
            for state in states_tuple:
                # Adds new found states from the NFA's transition table to state_array
                state_array += nfa.transition_table[state][inp] + nfa.transition_table[state]['E']

            # Dedup and tuple
            tuple_array = tuple(sorted(set(state_array)))

            # Add tuple to state_dict. State_dict holds all possible destination states and inputs for the current state
            # tuple of the new DFA
            state_dict[inp] = tuple_array

            # If the newly created tuple is not empty and it isn't part of the known states of the new DFA, then we add
            # it as a new state of the new DFA. We will then iterate over this new state after coming back to line 14.
            if tuple_array and tuple_array not in states:
                states.append(tuple_array)

        # Adds state_dict as  a value to the new transition table, with state_tuple as the key.
        transition_table[states_tuple] = state_dict

    # Creates new end_states. If an existing state of the new DFA holds an end state of the old NFA, then we must add it
    # as an end_state.
    end_states = []
    for states_tuple in states:
        for state in nfa.end_states:
            if state in states_tuple:
                end_states.append(states_tuple)

    return DFA(states=states,
               alphabet=alphabet,
               initial_state=initial_state,
               transition_table=transition_table,
               end_states=end_states)


def _e_closure(nfa):
    for state in nfa.states:
        e_closure = [state]
        queue = nfa.transition_table[state]['E']
        for s in queue:
            e_closure += s
            e_states = nfa.transition_table[s]['E']

            for e_s in e_states:
                if e_s not in e_closure:
                    queue += e_s

        nfa.transition_table[state]['E*'] = e_closure


with open('ex3.json', 'r') as f:
    nfa = NFA.from_json(f.read())

dfa = nfa_to_dfa_with_e(nfa)

dfa.pretty_print()
