import json
import pprint


class DPDA:
    def __init__(self, states, alphabet, stack_symbols, initial_state, initial_stack_symbol, end_states, transition_table):
        self.states = states
        self.alphabet = alphabet
        self.stack_symbols = stack_symbols
        self.initial_state = initial_state
        self.initial_stack_symbol = initial_stack_symbol
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
        print("Stack Symbols:", self.stack_symbols)
        print("Starting state:", self.initial_state)
        print("Stack:", [self.initial_stack_symbol])
        print("Accepting states:", self.end_states)
        print("Transition table:")
        pprint.pprint(self.transition_table, indent=2)
        print()

    def run(self, inp):
        stack = [self.initial_stack_symbol]
        current_state = self.initial_state

        for letter in inp:
            delta_tuple = self.transition_table[current_state][letter][stack.pop()]

            if delta_tuple:
                current_state = delta_tuple[0]
                to_push_into_stack = delta_tuple[1]
                if to_push_into_stack != "E":
                    for n in reversed(delta_tuple[1]):
                        stack.append(n)
            else:
                return False

        if stack:
            delta_tuple = self.transition_table[current_state]["E"][stack.pop()]

            if delta_tuple:
                current_state = delta_tuple[0]
                to_push_into_stack = delta_tuple[1]
                if to_push_into_stack != "E":
                    for n in reversed(delta_tuple[1]):
                        stack.append(n)
            else:
                return False

        return current_state in self.end_states and not stack


if __name__ == '__main__':
    with open('basic_PDA.json', 'r') as f:
        dpda = DPDA.from_json(f.read())

    print(f'Final State in End states: {dpda.run("0010111")}')
