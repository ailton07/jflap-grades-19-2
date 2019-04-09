#!/bin/bash
printf "Questao-A"
read ARQUIVO
echo "Saida: $ARQUIVO.jff"
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff aababb
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff abababbabababa
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff ababbababa
printf "Questao-B"
read ARQUIVO
echo "Saida: $ARQUIVO.jff"
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff aababb
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff ababbababa
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff abababbabababa