import subprocess

jflapJarPath = '../jflaplib-cli-1.3-bundle.jar'



def main():
  result = subprocess.run(['java', '-jar', jflapJarPath, 'run', 'alunos/anderson-pimentel/Anderson_L01_q01a.jff', '010101'], stdout=subprocess.PIPE)
  print(result.stdout.decode('ascii'))

if __name__== "__main__":
  main()
