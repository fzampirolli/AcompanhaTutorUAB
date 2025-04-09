#!/bin/bash
# =====================================================================
# Copyright (C) 2024-2025 Francisco de Assis Zampirolli
# from Federal University of ABC and individual contributors.
# All rights reserved.
#
# This file is part of Acompanh@TutorUAB v.0.1
#
# Languages: Python, PHP, Bash and many libraries described at
# github.com/fzampirolli/Acompanh@TutorUAB
#
# You should cite some references included in vision.ufabc.edu.br
# in any publication about it.
#
# Acompanh@TutorUAB is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License
# (gnu.org/licenses/agpl-3.0.txt) as published by the Free Software
# Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# Acompanh@TutorUAB is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
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

