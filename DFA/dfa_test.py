import unittest
from DFA.dfa import DFA


class TestAutomataInitialization(unittest.TestCase):

    def test_empty_states(self):
        self.assertRaisesRegex(ValueError, 'states', DFA,
                               states=[],
                               alphabet=['1'],
                               initial_state='a',
                               end_states=['a'],
                               transition_table={'a': {'1': 'a'}})

    def test_empty_alphabet(self):
        self.assertRaisesRegex(ValueError, 'alphabet', DFA,
                               states=['a'],
                               alphabet=[],
                               initial_state='',
                               end_states=[],
                               transition_table={'a': {'1': 'a'}})

    def test_empty_initial_state(self):
        self.assertRaisesRegex(ValueError, 'initial_state', DFA,
                               states=['a'],
                               alphabet=['1'],
                               initial_state='',
                               end_states=['a'],
                               transition_table={'a': {'1': 'a'}})

    def test_empty_transition_table(self):
        self.assertRaisesRegex(ValueError, 'transition_table', DFA,
                               states=['a'],
                               alphabet=['1'],
                               initial_state='a',
                               end_states=['a'],
                               transition_table={})

    def test_initial_states_not_in_states(self):
        self.assertRaises(ValueError, DFA,
                          states=['a'],
                          alphabet=['1'],
                          initial_state='b',
                          end_states=['a'],
                          transition_table={'a': {'1': 'a'}})

    def test_end_state_not_in_states(self):
        self.assertRaises(ValueError, DFA,
                          states=['a'],
                          alphabet=['1'],
                          initial_state='a',
                          end_states=['b'],
                          transition_table={'a': {'1': 'a'}})

    def test_transition_table_key_not_in_states(self):
        self.assertRaises(ValueError, DFA,
                          states=['a'],
                          alphabet=['1'],
                          initial_state='a',
                          end_states=['a'],
                          transition_table={'b': {'1': 'a'}})

    def test_transition_table_not_containing_all_states(self):
        self.assertRaises(ValueError, DFA,
                          states=['a', 'b'],
                          alphabet=['1'],
                          initial_state='a',
                          end_states=['a'],
                          transition_table={'a': {'1': 'a'}})


class TestAutomataExamples(unittest.TestCase):

    def test_accepts_string_ending_in_0(self):
        dfa = DFA(states=['a', 'b'],
                  alphabet=['0', '1'],
                  initial_state='a',
                  end_states=['b'],
                  transition_table={
                      'a': {
                          '0': 'b',
                          '1': 'a'
                      },
                      'b': {
                          '0': 'b',
                          '1': 'a'
                      }
                  })

        self.assertTrue(dfa.run('0'))
        self.assertTrue(dfa.run('10'))
        self.assertTrue(dfa.run('10100110'))
        self.assertTrue(dfa.run('0000'))
        self.assertTrue(dfa.run('11110'))
        self.assertFalse(dfa.run('1'))
        self.assertFalse(dfa.run('11'))
        self.assertFalse(dfa.run('10100111'))
        self.assertFalse(dfa.run('0001'))
        self.assertFalse(dfa.run('11111'))

    def test_accepts_string_containing_01_as_a_subword(self):
        dfa = DFA(states=['a', 'b', 'c', 'd'],
                  alphabet=['0', '1'],
                  initial_state='a',
                  end_states=['d'],
                  transition_table={
                      'a': {
                          '0': 'c',
                          '1': 'b'
                      },
                      'b': {
                          '0': 'c',
                          '1': 'b'
                      },
                      'c': {
                          '0': 'c',
                          '1': 'd'
                      },
                      'd': {
                          '0': 'd',
                          '1': 'd'
                      }
                  })

        self.assertTrue(dfa.run('01'))
        self.assertTrue(dfa.run('101'))
        self.assertTrue(dfa.run('1100111'))
        self.assertTrue(dfa.run('100001'))
        self.assertTrue(dfa.run('011111'))
        self.assertFalse(dfa.run('0'))
        self.assertFalse(dfa.run('1'))
        self.assertFalse(dfa.run('11'))
        self.assertFalse(dfa.run('1111111'))
        self.assertFalse(dfa.run('10000'))
        self.assertFalse(dfa.run('00000'))


if __name__ == '__main__':
    unittest.main()
