#!/bin/bash
printf "Questao 03"
read ARQUIVO
echo "Saida: $ARQUIVO.jff" 
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff 101
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff  0010
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff  0010011001
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff  0001
java -jar ../../../jflaplib-cli-1.3-bundle.jar run $ARQUIVO.jff  00100
