https://guides.github.com/features/mastering-markdown/# jflap-grades
Grades for FTC. The usage of JFLPLib CLI to compare results and output grades

execution:
> python3 gradesX.py

## Tests

1. Name and number of test files must be the same for referenced in students questions sufix.
e.g:

  1. tests
```
 * q01a.tst
 * q01b.tst
 * .
 * .
 * .
 * q03a.tst
```

  2. students
```
 * student1
 * studentA_L01_q01a.jff
 * studentA_L01_q01b.jff
 * .
 * .
 * .
 * studentA_L01_q02.jff
 * studentA_L01_q03a.jff
```

2. Test files must have the input tests and the expected result, as bellow:
- tests
 -- q01a.tst

Inside `q01a.tst` must be in this format of data per line:
```
question_type
question_value
input1	expected_result1
input2	expected_result2
.
.
.
inputN	expected_resultN
```
Where:
- `question_type`:
type of question
    - 0 for 'run'
    - 1 for 'equivalent'
    - 2 for 'regular'

- `question_value`: 

value of question. E.g.: `0.2`
Notice that the final score will be value divided by number of correct test cases.

- `expected_result`:

    - 1 -> accept
    - 0 -> reject

**e.g.**
```
0
0.25
001	0
110	1
```
The example define 0 in the first line to indicate type _run_ (automata), the second line means the question having 0.25 points, and third until the end of file meaning the pair input and expected result. 

