#!/bin/bash
printf "Questao 02-A"
read ARQUIVO
echo "Saida: $ARQUIVO.jff"
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff abab
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff ababa
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff bbbaaaa
printf "Questao 02-B"
read ARQUIVO
echo "Saida: $ARQUIVO.jff"
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff abbaa
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff abbba
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff bbabba
printf "Questao 02-C"
read ARQUIVO
echo "Saida: $ARQUIVO.jff"
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff aabaa
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff baaabaab
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff ababab
printf "Questao 02-D"
read ARQUIVO
echo "Saida: $ARQUIVO.jff"
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff aaaa
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff bbaaab
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff aabaaa