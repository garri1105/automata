import json
import pprint


class DFA:
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
        print("---------------------\nThis DFA has %s states" % len(self.states))
        print("States:", self.states)
        print("Alphabet:", self.alphabet)
        print("Starting state:", self.initial_state)
        print("Accepting states:", self.end_states)
        print("Transition table:")
        pprint.pprint(self.transition_table, indent=2)
        print()

    @property
    def states(self):
        return self._states

    @states.setter
    def states(self, states):
        if not states:
            raise ValueError(f'states can\'t be empty. A DFA\'s number of states must be equal or greater than 1.')

        self._states = set(states)

    @property
    def alphabet(self):
        return self._alphabet

    @alphabet.setter
    def alphabet(self, alphabet):
        if not alphabet:
            raise ValueError(f'alphabet can\'t be empty. A DFA\'s number of possible inputs must be equal or greater than 1.')

        self._alphabet = set(alphabet)

    @property
    def initial_state(self):
        return self._initial_state

    @initial_state.setter
    def initial_state(self, initial_state):
        if not initial_state:
            raise ValueError(f'initial_state can\'t be empty')

        if tuple(initial_state) not in self._states:
            raise ValueError(f'initial_state \'{initial_state}\' is not in list of possible states')

        self._initial_state = tuple(initial_state)

    @property
    def end_states(self):
        return self._end_states

    @end_states.setter
    def end_states(self, end_states):
        for state in end_states:
            if state not in self._states:
                raise ValueError(
                    f'end state {state} is not in list of possible states. All end_states must be in list of states'
                )

        self._end_states = end_states

    @property
    def transition_table(self):
        return self._transition_table

    @transition_table.setter
    def transition_table(self, transition_table):
        if not transition_table:
            raise ValueError('transition_table can\'t be empty')

        if not self._states:
            raise ValueError('states can\'t be empty')

        if len(self._states) != len(transition_table.keys()):
            raise ValueError('transition_table keys must contain all possible states')

        for state in self._states:
            try:
                transition_table[state]
            except KeyError as e:
                raise ValueError(f'transition_table must contain state {e}')

        self._transition_table = transition_table

    def run(self, inp):
        current_state = self.initial_state

        for letter in inp:
            current_state = self.transition_table[current_state][letter]

        return current_state in self.end_states


if __name__ == '__main__':
    with open('basic_DFA.json', 'r') as f:
        dfa = DFA.from_json(f.read())

    print(f'Final State in End states: {dfa.run("0010111")}')
