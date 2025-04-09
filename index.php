<!--
=====================================================================
Copyright (C) 2024-2025 Francisco de Assis Zampirolli
from Federal University of ABC and individual contributors.
All rights reserved.

This file is part of Acompanh@TutorUAB v.0.1

Languages: Python, PHP, Bash and many libraries described at
github.com/fzampirolli/Acompanh@TutorUAB

You should cite some references included in vision.ufabc.edu.br
in any publication about it.

Acompanh@TutorUAB is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License
(gnu.org/licenses/agpl-3.0.txt) as published by the Free Software
Foundation, either version 3 of the License, or (at your option)
any later version.

Acompanh@TutorUAB is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
=====================================================================
-->

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guia para Acompanhar Atividades dos Tutores no Moodle</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f9f3e3; /* Fundo em tom de bege */
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }

.container {
    background-color: #fffff5; /* Cor de fundo bonita */
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    padding: 40px;
    max-width: 800px;
    width: 100%;
}

        h1 {
            color: #007bff; /* Letras em tom de azul */
            margin-bottom: 20px;
        }

        p {
            color: #444; /* Letras em tom de cinza */
            line-height: 1.6;
            margin-bottom: 15px;
        }

        ul {
            list-style-type: none;
            padding: 0;
        }

        li {
            margin-bottom: 10px;
        }

        a {
            color: #007bff; /* Links em tom de azul */
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }

        @media screen and (max-width: 800px) {
            .container {
                padding: 20px;
            }
        }

        /* Novos estilos para a animação da lupa */
        .loader {
            position: relative;
            display: inline-block;
            width: 10px;
            height: 10px;
            border: 2px solid #f3f3f3;
            border-top: 2px solid #3498db;
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }

        /* Animação da lupa */
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

    </style>
</head>
<body>

<div class="container">
    <h1>Guia para Acompanhar Atividades dos Tutores no Moodle</h1>

    <hr/>

    <h4>
        Consulte os modelos de arquivos disponíveis na pasta
        <a href="modelos/uploads/" target="_blank" rel="noopener noreferrer">uploads</a>.
        <!-- Os arquivos gerados a partir desses modelos estão na pasta
        <a href="modelos/report/" target="_blank" rel="noopener noreferrer">report</a>. -->
        A seguir, resume os passos necessários para obter ou alterar esses arquivos no Moodle.
        Ao final desta página, você poderá gerar relatórios automaticamente.
        <a href="https://youtu.be/HLIRELvEKcs" target="_blank" rel="noopener noreferrer">Assista ao vídeo explicativo</a>.
    </h4>

    <hr/>

<h2>1) Atualizar a lista de tutores e seus alunos</h2>


    <h3>Arquivo: tutores.JSON (criar apenas uma vez por disciplina)</h3>
    
    <p>Copiar e colar de Participantes + Grupos (Visão Geral) no dicionário (ver modelo <a href="modelos/uploads/tutores.json" target="_blank">tutores.json</a>). É importante as chaves serem exatamente iguais aos grupos no Moodle.</p>

<h2>2) Analisar feedbacks dos tutores em Notas</h2>

    <h3>Arquivo: notas.ODS</h3>

<ol>
    <li>Ir em Notas + Relatório de Notas + Exportar.</li>
    <li>Desmarcar tudo e marcar apenas a(s) atividade(s) a ser(em) analisada(s).</li>
    <li>Depois em <b>"Opções de formato de exportação"</b>, marcar <b>"Incluir avaliação na exportação"</b>.</li>
    <li>Escolher Download.    </li>
</ol>


<h2>3) Analisar alunos por tutor(a) através do log da atividade no Moodle</h2>

    <h3>Arquivo: logs.CSV (opcional)</h3>

    <p>Fazer download do log retirado da atividade da disciplina do Moodle.</p>


<ol>
    <li>Relatórios (Logs) +</li>
    <li>Escolher a atividade +</li>
    <li>Obter estes logs +</li>
    <li>Download do csv (final da página)</li>
</ol>

<hr/>

<div style="background-color: #f9f9f9; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); max-width: 700px; margin: 0 auto;">
    <h2 style="color: #007bff; margin-bottom: 20px;">Upload de arquivos para gerar os relatórios</h2>

    <p style="color: #444; line-height: 1.6; margin-bottom: 20px;">Selecione os arquivos nos formatos JSON, ODS e CSV obtidos nos três passos anteriores:</p>

<form action="upload.php" method="post" enctype="multipart/form-data" onsubmit="showLoader()">
    <!-- Arquivos obrigatórios -->
    <label for="jsonFile" style="color: #444;">Arquivo <b>tutores.JSON</b>:</label><br>
    <input type="file" name="jsonFile" id="jsonFile" accept=".json" style="margin-bottom: 10px;"><br>

    <label for="odsFile" style="color: #444;">Arquivo <b>notas.ODS</b>:</label><br>
    <input type="file" name="odsFile" id="odsFile" accept=".ods" style="margin-bottom: 20px;"><br>

    <!-- Arquivo opcional -->
    <label for="csvFile" style="color: #444;">Arquivo <b>logs.CSV</b> (opcional):</label><br>
    <input type="file" name="csvFile" id="csvFile" accept=".csv" style="margin-bottom: 20px;"><br>

    <hr style="border-color: #ccc;">

    <!-- Opção de envio de e-mails -->
    <label for="sendEmails" style="color: #444;">
<input type="checkbox" name="sendEmails" id="sendEmails" onchange="toggleEmailOptions()">
<label for="sendEmails" style="color: #444;">Enviar e-mails aos tutores (recomenda-se validar os dados gerados antes do envio)</label>
    </label><br>

    <!-- Campos para e-mails (visíveis apenas se a opção estiver selecionada) -->
    <div id="emailOptions" style="display: none; margin-top: 10px;">
        <label for="emailMessage" style="color: #444;">Mensagem:</label><br>
	<textarea name="emailMessage" id="emailMessage" rows="6" style="width: 100%; margin-bottom: 10px;" placeholder="Insira a mensagem para os tutores aqui...">
Prezado(a) Tutor(a),

Segue o gráfico de barras com as atividades corrigidas da disciplina YY até xx/xx/25.

Informo que:
1. Os alunos destacados em rosa no gráfico devem ter suas atividades corrigidas. Caso não tenham enviado, é necessário realizar busca ativa.
2. Os alunos destacados em cinza no gráfico devem ser contatados, pois estão ausentes no curso.

É fundamental que todos os alunos que entregaram as atividades recebam suas notas em até 72 horas.

Atenciosamente,  
Prof.
</textarea>

<label for="emailCc" style="color: #444;">Endereços de Cc separados por vírgula (opcional):</label><br>
        <input type="text" name="emailCc" id="emailCc" style="width: 100%; margin-bottom: 20px;" placeholder="Insira os e-mails separados por vírgula"><br>
    </div>

    <hr style="border-color: #ccc;">

    <!-- Botão de envio -->
    <button type="submit" name="submit" style="background-color: #007bff; color: #fff; border: none; border-radius: 5px; padding: 10px 20px; cursor: pointer;">
        <span id="loader" style="display: none;" class="loader"></span> Enviar
    </button>
</form>

<script>
    function toggleEmailOptions() {
        const emailOptions = document.getElementById('emailOptions');
        const sendEmails = document.getElementById('sendEmails').checked;
        emailOptions.style.display = sendEmails ? 'block' : 'none';
    }
</script>

</div>

<hr/>
<footer style="text-align: center; padding: 20px; font-size: 14px; border-top: 1px solid #dee2e6;">
  <p>
    Enviar sugestões de melhoria para:
    <a href="mailto:fzampirolli@ufabc.edu.br" style="color: #007bff; text-decoration: none;">fzampirolli@ufabc.edu.br</a>
  </p>

  <a href="https://www.gnu.org/licenses/agpl-3.0.html" target="_blank" style="display: inline-block; margin: 10px;">
    <img src="http://mctest.ufabc.edu.br:8000/static/agplv3.png" alt="Licença AGPL v3" width="50" style="border: none;">
  </a>

  <p style="margin: 10px 0;">
    Copyright © 2024-2025 por
    <a href="https://sites.google.com/site/fzampirolli/" target="_blank" style="color: #007bff; text-decoration: none;">Francisco de Assis Zampirolli</a> da
    <a href="http://www.ufabc.edu.br" target="_blank" style="color: #007bff; text-decoration: none;">UFABC</a> e colaboradores.
  </p>
</footer>



</div>
    <script>
        function showLoader() {
            document.getElementById("loader").style.display = "inline-block";
        }
    </script>
</body>
</html>
