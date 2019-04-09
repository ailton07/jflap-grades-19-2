#!/bin/bash
printf "Questao-A"
read ARQUIVO
echo "Saida: $ARQUIVO.jff"
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff ababab
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff abba
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff aaabbb
printf "Questao-B"
read ARQUIVO
echo "Saida: $ARQUIVO.jff"
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff abababbab
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff ababababab
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff aababbab
printf "Questao-C"
read ARQUIVO
echo "Saida: $ARQUIVO.jff"
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff aaaba
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff ababaabbab
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff aabbbabbaab
printf "Questao-D"
read ARQUIVO
echo "Saida: $ARQUIVO.jff"
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff ababc
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff abc
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff cba
printf "Questao-E"
read ARQUIVO
echo "Saida: $ARQUIVO.jff"
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff abab
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff abbb
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff abbbabbab
