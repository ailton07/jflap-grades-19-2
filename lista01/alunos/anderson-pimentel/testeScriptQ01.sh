#!/bin/bash
printf "Questao 01-A"
read ARQUIVO
echo "Saida: $ARQUIVO.jff"
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff 010101
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff 00001
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff 0101101
printf "Questao 01-B"
read ARQUIVO
echo "Saida: $ARQUIVO.jff"
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff 010100
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff 0010001
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff 01010000101
printf "Questao 01-C"
read ARQUIVO
echo "Saida: $ARQUIVO.jff"
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff 010111
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff 010100
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff 110010
printf "Questao 01-D"
read ARQUIVO
echo "Saida: $ARQUIVO.jff"
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff 12345
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff 12345522
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff 1353
printf "Questao 01-E"
read ARQUIVO
echo "Saida: $ARQUIVO.jff"
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff 00000
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff 000000
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff 0000
