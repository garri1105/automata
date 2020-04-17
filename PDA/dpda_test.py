import unittest
from PDA.dpda import DPDA


class TestAutomataExamples(unittest.TestCase):

    def test_accepts_equal_number_of_leading_0s_followed_by_1s(self):
        dpda = DPDA(states=["q0", "q1"],
                    alphabet=["0", "1", "E"],
                    stack_symbols=["A", "Z"],
                    initial_state="q0",
                    initial_stack_symbol="Z",
                    end_states=["q1"],
                    transition_table={
                        "q0": {
                            "0": {
                                "A": ["q0", "AA"],
                                "Z": ["q0", "AZ"]
                            },
                            "1": {
                                "A": ["q1", "E"],
                                "Z": []
                            },
                            "E": {
                                "A": ["q1", "E"],
                                "Z": []
                            }
                        },
                        "q1": {
                            "0": {
                                "A": [],
                                "Z": []
                            },
                            "1": {
                                "A": ["q1", "E"],
                                "Z": []
                            },
                            "E": {
                                "A": [],
                                "Z": ["q1", "E"]
                            }
                        }
                    })

        self.assertFalse(dpda.run('00'))
        self.assertFalse(dpda.run('11'))
        self.assertTrue(dpda.run('01'))
        self.assertTrue(dpda.run('0011'))
        self.assertTrue(dpda.run('000111'))
        self.assertFalse(dpda.run(''))
        self.assertFalse(dpda.run('1'))
        self.assertFalse(dpda.run('0'))
        self.assertFalse(dpda.run('10'))
        self.assertFalse(dpda.run('101'))
        self.assertFalse(dpda.run('10101'))


if __name__ == '__main__':
    unittest.main()
