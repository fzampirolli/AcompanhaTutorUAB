#!/bin/bash
# =====================================================================
# Copyright (C) 2024-2025 Francisco de Assis Zampirolli
# da Universidade Federal do ABC e colaboradores individuais.
# Todos os direitos reservados.

# Este arquivo faz parte do Acompanh@TutorUAB v.0.1

# Linguagens: Python, PHP, Bash e diversas bibliotecas descritas em
# github.com/fzampirolli/AcompanhaTutorUAB

# Referências relevantes estão disponíveis em vision.ufabc.edu.br.
# Favor citá-las em qualquer publicação relacionada.

# Acompanh@TutorUAB é um software livre: você pode redistribuí-lo e/ou
# modificá-lo sob os termos da Licença Pública Geral Affero GNU,
# como publicada pela Free Software Foundation, versão 3 da Licença
# ou (a seu critério) qualquer versão posterior.

# Este sistema é distribuído na esperança de que seja útil,
# mas SEM NENHUMA GARANTIA; sem sequer a garantia implícita de
# COMERCIALIZAÇÃO ou ADEQUAÇÃO A UM DETERMINADO PROPÓSITO. Veja a
# Licença Pública Geral GNU para mais detalhes:
# gnu.org/licenses/agpl-3.0.txt
# =====================================================================

# Recebe os argumentos
#jsonFile=$1
#odsFile=$2
#csvFile=$3
#sendEmails=$4
#emailMessage=$5
#emailCc=$6

# Exibe os argumentos (apenas para depuração)
#echo "Arquivo JSON: $jsonFile"
#echo "Arquivo ODS: $odsFile"
#echo "Arquivo CSV: $csvFile"
#echo "Enviar e-mails: $sendEmails"
#echo "Mensagem: $emailMessage"
#echo "Cc: $emailCc"

# Executa o script Python com os argumentos fornecidos
if [ "$#" -eq 6 ]; then
    python3 ./script.py "$1" "$2" "$3" "$4" "$5" "$6"
elif [ "$#" -eq 5 ]; then
    python3 ./script.py "$1" "$2" "$3" "$4" "$5"
else
    echo "Erro: Número incorreto de argumentos para execução do script Python."
    exit 1
fi

