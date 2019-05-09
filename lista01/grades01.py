import subprocess
from os import listdir, remove
from os.path import isfile, join, splitext, exists

jflapJarPath = '../jflaplib-cli-1.3-bundle.jar'
testsFilePath = 'tests'
studentsFilePath = 'students'
csvFileName = 'grades.csv'

######################
######################
###### Aux ###########
######################
######################

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

def doJFlapLibCLI(method, file, input):
    result = subprocess.run(['java', '-jar', jflapJarPath, method, file, input], stdout=subprocess.PIPE)
    return result.stdout.decode('ascii')

def writeLine(fp, line):
    line += '\n'
    fp.write(line)

def toCSVfile(studentsGrades, testCaseNames):
    print('\n### Grades in csv file -> ' + csvFileName)

    if(exists(csvFileName)):
        remove(csvFileName)

    with open(csvFileName,'a') as f:
        line = 'student'

        # write header
        for testName in testCaseNames:
            line += ',' + testName
        line += ',questions,points'
        writeLine(f,line)

        # write students
        for student in studentsGrades:
            line = ''
            line = student[0] + ','
            grades = student[1]['grade']

            for testName in testCaseNames:
                if testName in grades:
                    line += str(grades[testName]) + ','
                else:
                    line += '0,'
            line += str(student[1]['questions']) + ','
            line += str(student[1]['points'])
            writeLine(f,line)
        f.close()

######################
######################
###### Tests #########
######################
######################

def readQuestions():
    files = [f for f in listdir(testsFilePath) if isfile(join(testsFilePath, f))]
    files.sort()
    filesWext = [splitext(f)[0] for f in files]
    return filesWext, files

# create array of files, dics of tests for questions
def loadTestFiles(testFiles):
    tests = {}
    for test in testFiles:
        questionName = test.split('.')[0]

        with open(join(testsFilePath,test)) as fp:
            questionType = fp.readline()
            questionType = questionType.rstrip('\n').split(' ')

            questionValue = fp.readline()
            questionValue = questionValue.rstrip('\n').split(' ')

            if(len(questionType) != 1 or len(questionValue) != 1):
                print('[ERROR] The type should be 0 (run), 1 (equivalent) or 2 (regular) , eg.: 001 1')
                print('[ERROR] The value should be real number, eg.: 0.25')
                print('[EFILE]', join(testsFilePath,test))
                exit(1)

            questionTest = {
                'type': questionType[0],
                'value': questionValue[0],
                'cases': []
            }

            for line in fp:
                line = line.rstrip('\n').split(' ') # rstrip -> it removes new line '\n' from string
                if(len(line) != 2):
                    print('[ERROR] Test should have input and expect result, eg.: 001 1')
                    print('[EFILE]', join(testsFilePath,test))
                    exit(1)
                questionTest['cases'].append(line)
            fp.close()
            tests[questionName] = questionTest
    return tests

def configTests():
    # read questions and test files
    questions, testFiles = readQuestions()
    # Load test files
    tests = loadTestFiles(testFiles)
    return [questions,testFiles,tests]

######################
######################
###### Students ######
######################
######################

def readStudents():
    files = listdir(studentsFilePath)
    files.sort()
    return files

def readExercises(studentDir):
    files = [f for f in listdir(studentDir) if isfile(join(studentDir, f))]
    files.sort()
    return files

def checkRunQuestion(test, fileName, studentName):
    resultCases = {'passed': [], 'nopassed': [], 'total': len(test['cases'])}
    for case in test['cases']:
        result = doJFlapLibCLI('run', join(studentsFilePath,studentName,fileName), case[0]).rstrip('\n')
        resultBin = -1
        if result != '':
            resultBin = (1 if result == 'true' else 0)
        print('Case ['+ str(case[0]) +']: expected ' + str(case[1]) + ' got ' + str(resultBin))
        # print(resultBin, case)
        if(resultBin == int(case[1])):
            resultCases['passed'].append(case[0])
        else:
            resultCases['nopassed'].append(case[0])

    return resultCases

def calculateExercises(exerciseFiles, studentName, testCase):
    grade = {}
    counter = 0.0
    for fileName in exerciseFiles:
        question = fileName[-8:-4]

        if(question.find('_') != -1):
            question = question[1:]
        print('--> [' + question + ']')
        test = testCase[2][question]
        print(test)
        if(test['type'] == '0'):
            runResults = checkRunQuestion(test, fileName, studentName)
            print(runResults)
            questionValue = float(test['value'])
            point = float(len(runResults['passed']) * questionValue) / runResults['total']
            point = truncate(point,2)
            counter += point
            print('### Score: ' + str(point) + ', Hits: (' + str(len(runResults['passed'])) + '/' + str(runResults['total']) + ')\n')
            grade[question] = point
        # TODO:: for other types of jflap lib cli
    counter = truncate(counter,2)
    return {'grade': grade, 'points': counter, 'questions': len(exerciseFiles)}

def configStudents(testCase):
    studentsGrades = []
    studentsName = readStudents()
    counter = 0
    for studentName in studentsName:
        print('\n>> #' + str(counter + 1) + ' ' + studentName + ' ..')
        exerciseFiles = readExercises(join(studentsFilePath,studentName))
        # print(studentName + ' exercises..')
        grade = calculateExercises(exerciseFiles, studentName,testCase)
        studentsGrades.append([studentName, grade])
        counter += 1
        print('### Total of questions computed: ' + str(len(exerciseFiles)) + ' ###\n')
    print('### Total of students: ' + str(counter) + ' ###')
    return studentsGrades

######################
######################
###### Main ##########
######################
######################

def main():
    # Configuration(reading and loading) of all tests
    testCase = configTests()
    # Reading and loading of all students
    studentsGrades = configStudents(testCase)
    toCSVfile(studentsGrades, testCase[0])

if __name__== "__main__":
    main()
