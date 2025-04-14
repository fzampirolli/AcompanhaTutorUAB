<!--
=====================================================================
Copyright (C) 2024-2025 Francisco de Assis Zampirolli
da Universidade Federal do ABC e colaboradores individuais.
Todos os direitos reservados.

Este arquivo faz parte do Acompanh@TutorUAB v.0.1

Linguagens: Python, PHP, Bash e diversas bibliotecas descritas em
github.com/fzampirolli/AcompanhaTutorUAB

Referências relevantes estão disponíveis em vision.ufabc.edu.br.
Favor citá-las em qualquer publicação relacionada.

Acompanh@TutorUAB é um software livre: você pode redistribuí-lo e/ou
modificá-lo sob os termos da Licença Pública Geral Affero GNU,
como publicada pela Free Software Foundation, versão 3 da Licença
ou (a seu critério) qualquer versão posterior.

Este sistema é distribuído na esperança de que seja útil,
mas SEM NENHUMA GARANTIA; sem sequer a garantia implícita de
COMERCIALIZAÇÃO ou ADEQUAÇÃO A UM DETERMINADO PROPÓSITO. Veja a
Licença Pública Geral GNU para mais detalhes:
gnu.org/licenses/agpl-3.0.txt
=====================================================================
-->

<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guia para Acompanhamento das Atividades dos Tutores no Moodle</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f9f3e3;
            /* Fundo em tom de bege */
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }

        .container {
            background-color: #fffff5;
            /* Cor de fundo bonita */
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            padding: 40px;
            max-width: 800px;
            width: 100%;
        }

        h1 {
            color: #007bff;
            /* Letras em tom de azul */
            margin-bottom: 20px;
        }

        p {
            color: #444;
            /* Letras em tom de cinza */
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
            color: #007bff;
            /* Links em tom de azul */
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
            0% {
                transform: rotate(0deg);
            }

            100% {
                transform: rotate(360deg);
            }
        }
    </style>
</head>

<body>

    <div class="container">
        <h1>Guia para Acompanhamento das Atividades dos Tutores no Moodle</h1>

        <hr />

        <h4>
            Consulte os modelos de arquivos disponíveis na pasta
            <a href="modelos/uploads/" target="_blank" rel="noopener noreferrer">uploads</a>.
            <!-- Os arquivos gerados a partir desses modelos estão na pasta
        <a href="modelos/report/" target="_blank" rel="noopener noreferrer">report</a>. -->
            A seguir, resumem-se os passos necessários para obter ou alterar esses arquivos no Moodle.
            <a href="https://youtu.be/HLIRELvEKcs" target="_blank" rel="noopener noreferrer">Assista ao vídeo
                explicativo</a>.
        </h4>

        <hr />

<h2>1) Atualizar a lista de tutores e seus alunos</h2>

<h3>Arquivo: <code>tutores.JSON</code> (criar apenas uma vez por disciplina)</h3>

<p>Copie os dados de <b>Participantes</b> &rarr; <b>Grupos (Visão Geral)</b> e cole no dicionário, seguindo exatamente o formato do arquivo modelo
<code><a href="modelos/uploads/tutores.json" target="_blank">tutores.json</a></code>.</p>

<h2>2) Analisar feedbacks dos tutores na área de Notas</h2>

<h3>Arquivo: <code>notas.ODS</code></h3>

<ol>
    <li>Acesse <b>Notas</b> &rarr; <b>Relatório de Notas</b> &rarr; <b>Exportar</b>.</li>
    <li>Desmarque todas as opções e selecione apenas a(s) atividade(s) que deseja analisar.</li>
    <li>Em <b>Opções de formato de exportação</b>, marque <b>Incluir avaliação na exportação</b>.</li>
    <li>Escolha a opção <b>Download</b>.</li>
    <li>Renomeie o arquivo, removendo espaços do nome para evitar erros.</li>
</ol>


<h2>3) Analisar alunos por tutor(a) por meio do log da atividade no Moodle</h2>

<h3>Arquivo: <code>logs.CSV</code> (opcional)</h3>

<p>Faça o download do log da atividade correspondente na disciplina do Moodle.</p>

<ol>
    <li>Acesse <b>Relatórios</b> &rarr; <b>Logs</b>.</li>
    <li>Selecione a atividade desejada.</li>
    <li>Clique em <b>Obter estes logs</b>.</li>
    <li>Desça até o final da página e clique em <b>Download do CSV</b>.</li>
</ol>


        <hr />

        <div
            style="background-color: #f9f9f9; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); max-width: 700px; margin: 0 auto;">
            <h2 style="color: #007bff; margin-bottom: 20px;">Upload de arquivos para gerar os relatórios</h2>

            <p style="color: #444; line-height: 1.6; margin-bottom: 20px;">Selecione os arquivos nos formatos JSON, ODS
                e CSV obtidos nos três passos anteriores:</p>

            <form action="upload.php" method="post" enctype="multipart/form-data" onsubmit="showLoader()">
                <!-- Arquivos obrigatórios -->
                <label for="jsonFile" style="color: #444;">Arquivo <b><code>tutores.JSON</code></b>:</label><br>
                <input type="file" name="jsonFile" id="jsonFile" accept=".json" style="margin-bottom: 10px;"><br>

                <label for="odsFile" style="color: #444;">Arquivo <b><code>notas.ODS</code></b>:</label><br>
                <input type="file" name="odsFile" id="odsFile" accept=".ods" style="margin-bottom: 20px;"><br>

                <!-- Arquivo opcional -->
                <label for="csvFile" style="color: #444;">Arquivo <b><code>logs.CSV</code></b> (opcional):</label><br>
                <input type="file" name="csvFile" id="csvFile" accept=".csv" style="margin-bottom: 20px;"><br>

                <hr style="border-color: #ccc;">

                <!-- Opção de envio de e-mails -->
                <label for="sendEmails" style="color: #444;">
                    <input type="checkbox" name="sendEmails" id="sendEmails" onchange="toggleEmailOptions()">
                    <label for="sendEmails" style="color: #444;">Enviar e-mails aos tutores (recomenda-se validar os
                        dados gerados antes do envio)</label>
                </label><br>

                <!-- Campos para e-mails (visíveis apenas se a opção estiver selecionada) -->
                <div id="emailOptions" style="display: none; margin-top: 10px;">
                    <label for="emailMessage" style="color: #444;">Mensagem:</label><br>
                    <textarea name="emailMessage" id="emailMessage" rows="6" style="width: 100%; margin-bottom: 10px;"
                        placeholder="Insira a mensagem para os tutores aqui...">
Prezado(a) Tutor(a),

Encaminho, em anexo, o gráfico de barras com o status das atividades corrigidas da disciplina YY, atualizado até xx/xx/2025.

Informações importantes:

  1. Alunos destacados em rosa no gráfico ainda aguardam correção das atividades. Caso não tenham enviado a atividade, é necessário realizar busca ativa.

  2. Alunos destacados em cinza não constam com entrega registrada no Moodle, mas estão vinculados ao grupo/polo. Esses casos requerem contato para verificar a situação de ausência no curso.

Lembro que todas as atividades entregues devem ser corrigidas em até 72 horas, garantindo retorno pedagógico adequado aos estudantes.

Atenciosamente,
Prof. [Seu Nome]
</textarea>

                    <label for="emailCc" style="color: #444;">Endereços de Cc separados por vírgula
                        (opcional):</label><br>
                    <input type="text" name="emailCc" id="emailCc" style="width: 100%; margin-bottom: 20px;"
                        placeholder="Insira os e-mails separados por vírgula"><br>
                </div>

                <hr style="border-color: #ccc;">

                <!-- Botão de envio -->
                <button type="submit" name="submit"
                    style="background-color: #007bff; color: #fff; border: none; border-radius: 5px; padding: 10px 20px; cursor: pointer;">
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

        <hr />
        <footer style="text-align: center; padding: 20px; font-size: 14px; border-top: 1px solid #dee2e6;">
            <p>
                Projeto em desenvolvimento e disponível em <a
                    href="http://educapes.capes.gov.br/handle/capes/972423 ">eduCAPES</a> e <a
                    href="http://educapes.capes.gov.br/handle/capes/972423">GitHub</a>.
                Enviar sugestões de melhoria para <a href="mailto:fzampirolli@ufabc.edu.br"
                    style="color: #007bff; text-decoration: none;">fzampirolli@ufabc.edu.br</a>.
            </p>

            <a href="https://www.gnu.org/licenses/agpl-3.0.html" target="_blank"
                style="display: inline-block; margin: 10px;">
                <img src="http://mctest.ufabc.edu.br:8000/static/agplv3.png" alt="Licença AGPL v3" width="50"
                    style="border: none;">
            </a>

            <p style="margin: 10px 0;">
                Copyright © 2024-2025 por
                <a href="https://sites.google.com/site/fzampirolli/" target="_blank"
                    style="color: #007bff; text-decoration: none;">Francisco de Assis Zampirolli</a> da
                <a href="http://www.ufabc.edu.br" target="_blank"
                    style="color: #007bff; text-decoration: none;">UFABC</a> e colaboradores.
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