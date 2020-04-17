# Automatas

## Getting started

### Prerequisites

Only Python 3 is required. No additional packages needed.

### Project Contents

##### DFA
Contains the main dfa.py file and its corresponding tests. It also contains some example JSON files to correctly
initialize the DFA.

Finally, it contains the operations.py file where various DFA operations are implemented.

It is the most complete folder as the DFA is the simplest automata to implement. 


##### NFA
Contains the main nfa.py file and its corresponding tests. It also contains some example JSON files to correctly
initialize the NFA.

Finally, it contains the operations.py file where a NFA to DFA operation is implemented.

*Missing features*

- Functional tests are implemented but NFA initialization tests are missing.
- The NFA needs to reject strings when there aren't available transitions.
- The NFA to DFA operation uses tuples in a way that wasn't expected when thinking about the Automata JSON format. As a
result, the JSON format might not be consistent or functional across automatas. Revisions need to be made.

##### PDA
Contains the main dpda.py file and its corresponding tests. It only implements a deterministic pushdown automata.

It also contains an example JSON file to correctly initialize the PDA.


*Missing features*

- Functional tests are implemented but PDA initialization tests are missing.
- A non-deterministic pushdown automata. Implementation of the non-deterministic PDA was becoming too complex with the
current structure of the classes. Either a restructuring of the implemented automatas or a complex implementation are
needed. If the implementation is too complex then it might not be appropriate to be used in a class setting.
This decision is left to the person taking over this project.

 