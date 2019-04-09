#!/bin/bash
printf "Questao 01-A"
read ARQUIVO
echo "Saida: $ARQUIVO.jff"
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff 010101
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff 00001
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff 0101101
