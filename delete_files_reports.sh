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

# *  *    * * *   root     /var/www/html/LabMoodle/delete_files_reports.sh

# Define o tempo limite em segundos (300 segundos = 5 minutos)
tempo_limite=300

# Função para excluir arquivos/pastas após o tempo limite
excluir_itens() {
    local diretorio="$1"
    local tempo_limite="$2"
    local excluir_pastas="$3"

    # Entra no diretório
    cd "$diretorio" || exit

    # Itera sobre todas as subpastas/arquivos no diretório
    for item in *; do
        if [ -d "$item" ]; then
            # Caso seja uma pasta
            if [ "$excluir_pastas" = true ]; then
                # Obtém o tempo de criação da pasta em segundos desde a época (Unix timestamp)
                tempo_criacao=$(stat -c %Y "$item")
            else
                # Ignora pastas se não for para excluí-las
                continue
            fi
        else
            # Caso seja um arquivo
            if [ "$excluir_pastas" = false ]; then
                # Obtém o tempo de modificação do arquivo em segundos desde a época (Unix timestamp)
                tempo_criacao=$(stat -c %Y "$item")
            else
                # Ignora arquivos se for para excluir apenas pastas
                continue
            fi
        fi

        # Obtém o tempo atual em segundos desde a época
        tempo_atual=$(date +%s)

        # Calcula o tempo decorrido desde a criação/modificação do item
        tempo_decorrido=$((tempo_atual - tempo_criacao))

        # Verifica se o tempo decorrido é maior que o tempo limite
        if [ "$tempo_decorrido" -gt "$tempo_limite" ]; then
            # Remove o item (arquivo ou pasta) e todos os seus conteúdos
            rm -rf "$item"
            #echo "Item $item removido em $diretorio."
        fi
    done
}

# /var/www/html/LabMoodle

# Define os diretórios onde as subpastas estão localizadas
diretorio_reports="/var/www/html/LabMoodle/reports/"
diretorio_tmp="/var/www/html/LabMoodle/tmp/"

excluir_itens "$diretorio_reports" "$tempo_limite" false
excluir_itens "$diretorio_tmp" "$tempo_limite" true

# /var/www/html/UAB

# Define os diretórios onde as subpastas estão localizadas
diretorio_reports="/var/www/html/UAB/reports/"
diretorio_tmp="/var/www/html/UAB/tmp/"

excluir_itens "$diretorio_reports" "$tempo_limite" false
excluir_itens "$diretorio_tmp" "$tempo_limite" true