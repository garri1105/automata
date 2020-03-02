import unittest
from NFA import NFA


class TestAutomataExamples(unittest.TestCase):

    def test_accepts_contains_00_OR_11_as_substring(self):
        nfa = NFA(states=['a', 'b', 'c', 'd'],
                  alphabet=['0', '1', 'E'],
                  initial_state='a',
                  end_states=['d'],
                  transition_table={
                      'a': {
                          '0': ['a', 'b'],
                          '1': ['a', 'c'],
                          'E': []
                      },
                      'b': {
                          '0': ['d'],
                          '1': [],
                          'E': []
                      },
                      'c': {
                          '0': [],
                          '1': ['d'],
                          'E': []
                      },
                      'd': {
                          '0': ['d'],
                          '1': ['d'],
                          'E': []
                      }
                  })

        self.assertTrue(nfa.run('00'))
        self.assertTrue(nfa.run('11'))
        self.assertTrue(nfa.run('11001'))
        self.assertTrue(nfa.run('00110'))
        self.assertTrue(nfa.run('0110'))
        self.assertFalse(nfa.run(''))
        self.assertFalse(nfa.run('1'))
        self.assertFalse(nfa.run('0'))
        self.assertFalse(nfa.run('10'))
        self.assertFalse(nfa.run('101'))
        self.assertFalse(nfa.run('10101'))

    def test_accepts_even_0s_OR_even_1s(self):
        nfa = NFA(states=['a', 'b', 'c', 'd', 'e'],
                  alphabet=['0', '1', 'E'],
                  initial_state='a',
                  end_states=['b', 'd'],
                  transition_table={
                      'a': {
                          '0': [],
                          '1': [],
                          'E': ['b', 'd']
                      },
                      'b': {
                          '0': ['c'],
                          '1': ['b'],
                          'E': []
                      },
                      'c': {
                         '0': ['b'],
                         '1': ['c'],
                         'E': []
                      },
                      'd': {
                          '0': ['d'],
                          '1': ['e'],
                          'E': []
                      },
                      'e': {
                          '0': ['e'],
                          '1': ['d'],
                          'E': []
                      }
                  })

        self.assertTrue(nfa.run(''))
        self.assertTrue(nfa.run('1'))
        self.assertTrue(nfa.run('0'))
        self.assertTrue(nfa.run('11000'))
        self.assertTrue(nfa.run('00111'))
        self.assertFalse(nfa.run('10'))
        self.assertFalse(nfa.run('01'))
        self.assertFalse(nfa.run('101010'))

    def test_infinite_epsilon_loop___accepts_any_string(self):
        nfa = NFA(states=['a', 'b', 'c', 'd'],
                  alphabet=['0', '1', 'E'],
                  initial_state='a',
                  end_states=['d'],
                  transition_table={
                      'a': {
                          '0': [],
                          '1': [],
                          'E': ['b', 'd']
                      },
                      'b': {
                          '0': ['b', 'c'],
                          '1': ['b'],
                          'E': []
                      },
                      'c': {
                          '0': ['d'],
                          '1': [],
                          'E': []
                      },
                      'd': {
                          '0': ['d'],
                          '1': ['d'],
                          'E': ['a']
                      }
                  })

        self.assertTrue(nfa.run(''))
        self.assertTrue(nfa.run('0'))
        self.assertTrue(nfa.run('1'))
        self.assertTrue(nfa.run('10'))
        self.assertTrue(nfa.run('11'))
        self.assertTrue(nfa.run('0000'))
        self.assertTrue(nfa.run('11110'))
        self.assertTrue(nfa.run('10100111'))
        self.assertTrue(nfa.run('10100110'))

    def test_complicated_nfa(self):
        """This NFA only accepts strings that end with aa. The start of the string is either a single b (followed by
          anything), OR an even number of a's followed by a single b (followed by anything). The string has three parts:
          the first part ends with a single b, the first b of the string, the second part contains any string of a's and
          b's, and the third part is just the string aa."""

        nfa = NFA(states=['q0', 'q1', 'q2', 'q3', 'q4', 'q5'],
                  alphabet=['a', 'b', 'E'],
                  initial_state='q0',
                  end_states=['q5'],
                  transition_table={
                      'q0': {
                          'a': [],
                          'b': ['q2'],
                          'E': ['q1']
                      },
                      'q1': {
                          'a': ['q3'],
                          'b': ['q2'],
                          'E': []
                      },
                      'q2': {
                          'a': ['q2', 'q4'],
                          'b': ['q2'],
                          'E': []
                      },
                      'q3': {
                          'a': ['q1'],
                          'b': [],
                          'E': []
                      },
                      'q4': {
                          'a': ['q5'],
                          'b': [],
                          'E': []
                      },
                      'q5': {
                          'a': ['q2'],
                          'b': ['q2'],
                          'E': []
                      }
                  })

        self.assertTrue(nfa.run('baa'))
        self.assertTrue(nfa.run('bbbaaababaa'))
        self.assertTrue(nfa.run('aabaa'))
        self.assertTrue(nfa.run('aababbbbaaabbaa'))
        self.assertFalse(nfa.run('aba'))
        self.assertFalse(nfa.run('abaa'))
        self.assertFalse(nfa.run('aaba'))
        self.assertFalse(nfa.run(''))
        self.assertFalse(nfa.run('aababbbbaaabb'))


if __name__ == '__main__':
    unittest.main()
