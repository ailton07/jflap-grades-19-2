import subprocess
from os import listdir
from os.path import isfile, join, splitext

jflapJarPath = '../jflaplib-cli-1.3-bundle.jar'

def runJFlapLibCLI(method, file, input):
    result = subprocess.run(['java', '-jar', jflapJarPath, method, file, input], stdout=subprocess.PIPE)
    return result.stdout.decode('ascii')

def readQuestions():
    files = [f for f in listdir('tests') if isfile(join('tests', f))]
    filesWext = [splitext(f)[0] for f in files]
    filesWext.sort()
    return filesWext

def main():
    file = 'alunos/anderson-pimentel/Anderson_L01_q01a.jff'
    input = '010101'
    method = 'run'
    print(runJFlapLibCLI(method,file,input))

    questions = readQuestions()
    print(questions)
if __name__== "__main__":
    main()
