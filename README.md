
# JFLAP Grades 2019-2

A Python script to compare JFLAP files with prefined results and generate a CSV summary.  Used in FTC discipline (UFAM) in the second half of 2019.

Original project: [https://github.com/andbrain/jflap-grades](https://github.com/andbrain/jflap-grades)


## Prerequisites
- Python >= Python 3.6.5

## Running

execution:
> python3 grades.py

## Setting up

The directory tree structure looks like this:
```

└───jflap-grades
    ├───students
       ├───studentA
	       ├───studentA_L01_q01a.jff
  	       └─────studentA_L01_q01b.jff
    ├───tests
	    ├───q01a.tst
	    └─────q01b.tst
    └─────grades.py
```
The .jff files are the JFLAP questions to be verified. The .tst files are the Test Files described below.

Name and number of test files must match with referenced in students questions sufix (**q01a**.tst and into the student folder studentA_L01_**q01a**.jff or  studentA_L01_**q01_a**.jff)

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

### Test Files
Test files must have the input tests and the expected result, as bellow:

```
├───tests
    ├───q01a.tst
```

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
    - 1 for 'equivalent'  (**TODO**)
    - 2 for 'regular' (**TODO**)

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

