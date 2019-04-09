# jflap-grades
Grades for FTC. The usage of JFLPLib CLI to compare results and output grades

## Tests

1. Name and number of test files must be the same for referenced in students questions sufix.
e.g:
- tests
-- q01a.tst 
- students
-- student1
--- q01a.jff

2. Test files must have the input tests and the expected result, as bellow:
- tests
-- q01a.tst
input	result
001	0
110	1

where:
1 -> accept
0 -> reject
