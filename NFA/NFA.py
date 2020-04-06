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
        states_queue = [self.initial_state]
        to_add_epsilon = [state for state in self.transition_table[self.initial_state]["E"]]
        states_queue += to_add_epsilon
        states_to_check = 1 + len(to_add_epsilon)

        for letter in inp:
            temp = states_to_check
            states_to_check = 0
            i = 0
            checked = []

            while i < temp:
                state = states_queue.pop(0)

                to_add_epsilon = [state for state in self.transition_table[state]["E"] if state not in checked]
                states_queue += to_add_epsilon
                temp += len(to_add_epsilon)

                to_add = self.transition_table[state][letter]
                if not to_add:
                    if state in self.end_states:
                        return True
                else:
                    states_queue += to_add
                    states_to_check += len(to_add)

                checked.append(state)
                i += 1

        for state in states_queue:
            if state in self.end_states:
                return True

        return False
