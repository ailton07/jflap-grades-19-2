# jflap-grades
Grades for FTC. The usage of JFLPLib CLI to compare results and output grades

## Tests

1. Name and number of test files must be the same for referenced in students questions sufix.
e.g:
- tests
-- q01a.tst
-- q01b.tst
-- .
-- .
-- .
-- q03a.tst

- students
-- student1
--- studentA_L01_q01a.jff
--- studentA_L01_q01b.jff
.
.
.
--- studentA_L01_q02.jff
--- studentA_L01_q03a.jff

2. Test files must have the input tests and the expected result, as bellow:
- tests
-- q01a.tst
question_type
question_value
input1	expected_result1
input2	expected_result2
.
.
.
inputN	expected_resultN

[question_type] -> type of question
1. 0 for 'run'
2. 1 for 'equivalent'
3. 2 for 'regular'

[question_value] -> value of question. e.g. 0.2. Notice that the final score will be value divided by number of correct test cases.

> e.g.
0
0.25
001	0
110	1

[expected_result]:
1 -> accept
0 -> reject
