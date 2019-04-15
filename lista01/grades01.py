import subprocess
from os import listdir
from os.path import isfile, join, splitext

jflapJarPath = '../jflaplib-cli-1.3-bundle.jar'
testsFilePath = 'tests'
studentsFilePath = 'students'

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
    tests = []
    for test in testFiles:
        questionName = test.split('.')[0]

        with open(join(testsFilePath,test)) as fp:
            questionType = fp.readline()
            questionType = questionType.rstrip('\n').split(' ')
            if(len(questionType) != 1):
                print('[ERROR] The type should be 0 (run), 1 (equivalent) or 2 (regular) , eg.: 001 1')
                print('[EFILE]', join(testsFilePath,test))
                exit(1)

            questionTest = {
                'name': questionName,
                'type': questionType,
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
        tests.append(questionTest)
    return tests

def configTests():
    # read questions and test files
    questions, testFiles = readQuestions()
    # Load test files
    tests = loadTestFiles(testFiles)
    return questions,testFiles,tests

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

def checkExercises(exercises):
    for exercise in exercises:
        question = exercise[-8:-4]

        if(question.find('_') != -1):
            question = question[1:]
        print(question)

def configStudents():
    studentsName = readStudents()
    counter = 0
    for studentName in studentsName:
        print('\nReading #' + str(counter + 1) + ' ' + studentName + ' ..')
        exercises = readExercises(join(studentsFilePath,studentName))
        print('Checking ' + studentName + ' exercises..')
        checkExercises(exercises)
        print('Calculating ' + studentName + ' grade..')

        # input in csv file
        counter += 1
    print('\n\n### Total of students: ' + str(counter) + ' ###')

######################
######################
###### Main ##########
######################
######################


def runJFlapLibCLI(method, file, input):
    result = subprocess.run(['java', '-jar', jflapJarPath, method, file, input], stdout=subprocess.PIPE)
    return result.stdout.decode('ascii')

def main():


    # Configuration(reading and loading) of all tests
    questions,testFiles,tests = configTests()
    # Reading and loading of all students
    configStudents()


if __name__== "__main__":
    main()

# sample of how to run
# file = 'alunos/anderson-pimentel/Anderson_L01_q01a.jff'
# input = '010101'
# method = 'run'
# print(runJFlapLibCLI(method,file,input))
