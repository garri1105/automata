import json
import pprint

# FIXME Reject strings when there aren't available transitions.


class NFA:
    def __init__(self, states, alphabet, initial_state, end_states, transition_table):
        self.states = states
        self.alphabet = alphabet
        self.initial_state = initial_state
        self.end_states = end_states
        self.transition_table = transition_table

    def to_json(self):
        return json.dumps(self.__dict__, indent=2)

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)

    def pretty_print(self):
        print("---------------------\nThis NFA has %s states" % len(self.states))
        print("States:", self.states)
        print("Alphabet:", self.alphabet)
        print("Starting state:", self.initial_state)
        print("Accepting states:", self.end_states)
        print("Transition table:")
        pprint.pprint(self.transition_table, indent=2)
        print()

    def run(self, inp):
        # states_queue is composed of the states that need to be checked.
        # It is initialized with the initial_state parameter.
        states_queue = [self.initial_state]

        # Adds states to states_queue if they are an epsilon transition away from the initial state.
        states_queue += [state for state in self.transition_table[self.initial_state]["E"]]

        # states_to_check are the number of states left to check with the current input.
        # This variable is needed to know when we can finish checking the current input and move on to the next one.
        states_to_check = len(states_queue)

        for letter in inp:
            # temp stores the states_to_check current value and uses it as a flag in the next loop
            temp = states_to_check

            # Resets states_to_check to start counting the next input's states to check.
            states_to_check = 0
            i = 0

            # Array to store states already checked with the current input.
            checked = []

            while i < temp:
                # Pops first value from the state_queue.
                state = states_queue.pop(0)

                # Adds states to states_queue if they are an epsilon transition away from the current state.
                to_add_epsilon = [state for state in self.transition_table[state]["E"] if state not in checked]
                states_queue += to_add_epsilon
                temp += len(to_add_epsilon)

                # Gets possible destination states after a transition given by the current input.
                to_add = self.transition_table[state][letter]

                # If there aren't any possible destination states, check if the current state is an end state. If so,
                # return true.
                if not to_add:

                    # FIXME: is this behavior desired? Maybe if there is an extra input then the whole input string must
                    # be rejected.
                    if state in self.end_states:
                        return True
                else:
                    # If there are possible destination states, add them to states_to_check for the next input checks.
                    states_queue += to_add
                    states_to_check += len(to_add)

                # Add current state to checked array.
                checked.append(state)
                i += 1

        # If there is any states left in the states_queue, check if they are end states. If so, return True, else, False
        for state in states_queue:
            if state in self.end_states:
                return True

        return False


if __name__ == '__main__':
    with open('basic_NFA.json', 'r') as f:
        nfa = NFA.from_json(f.read())

    print(f'Final State in End states: {nfa.run("0010111")}')
