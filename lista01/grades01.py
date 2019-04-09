import subprocess
from os import listdir
from os.path import isfile, join, splitext

jflapJarPath = '../jflaplib-cli-1.3-bundle.jar'
testsFilePath = 'tests'

def runJFlapLibCLI(method, file, input):
    result = subprocess.run(['java', '-jar', jflapJarPath, method, file, input], stdout=subprocess.PIPE)
    return result.stdout.decode('ascii')

def readQuestions():
    files = [f for f in listdir(testsFilePath) if isfile(join(testsFilePath, f))]
    files.sort()
    filesWext = [splitext(f)[0] for f in files]
    return filesWext, files

def loadTestFiles(testFiles):
    tests = []
    for test in testFiles:
        questionTest = []
        with open(join(testsFilePath,test)) as fp:
            for line in fp:
                line = line.rstrip('\n').split(' ')
                if(len(line) != 2):
                    print('[ERROR] Test should have input and expect result, eg.: 001 1')
                    print('[EFILE]', join(testsFilePath,test))
                    exit(1)
                questionTest.append(line)  # rstrip -> it removes new line '\n' from string
            fp.close()
        tests.append(questionTest)
    return tests

def main():
    file = 'alunos/anderson-pimentel/Anderson_L01_q01a.jff'
    input = '010101'
    method = 'run'
    print(runJFlapLibCLI(method,file,input))

    # read questions and test files
    questions, testFiles = readQuestions()
    print(questions)
    print(testFiles)

    # Load test files
    tests = loadTestFiles(testFiles)
    print(tests)

if __name__== "__main__":
    main()
