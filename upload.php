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
<?php

// Diretório base para os dados do usuário
$dataDir = "./tmp/";

// Obter a data e hora atual no formato desejado (por exemplo, YYYY-MM-DD_HH-MM-SS)
$currentDateTime = date("Y-m-d_H-i-s");

// Diretório para o usuário com a data e hora atual
$dataCurrentDir = $dataDir . $currentDateTime . "/";

// Diretório de relatórios dentro do diretório do usuário
$reportDir = $dataCurrentDir . "report/";

// Diretório de uploads dentro do diretório do usuário
$uploadDir = $dataCurrentDir . "uploads/";

// Criar o diretório do usuário se ainda não existir
if (!is_dir($dataCurrentDir)) {
    mkdir($dataCurrentDir, 0777, true);
}

// Criar o diretório de relatórios dentro do diretório do usuário
if (!is_dir($reportDir)) {
    mkdir($reportDir, 0777, true);
}

// Criar o diretório de uploads dentro do diretório do usuário
if (!is_dir($uploadDir)) {
    mkdir($uploadDir, 0777, true);
}

// Verifica se o formulário foi enviado
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_FILES["jsonFile"]) && isset($_FILES["csvFile"]) && isset($_FILES["odsFile"])) {
    // Campos de arquivos
    $jsonFile = $_FILES["jsonFile"];
    $odsFile = $_FILES["odsFile"];
    $csvFile = isset($_FILES["csvFile"]) ? $_FILES["csvFile"] : null;

    // Diretório de destino para os uploads
    //$uploadDir = "tmp/uploads/";

    // Função para mover arquivo
    function moveFile($file, $uploadDir)
    {
        // Verifica se não houve erro durante o upload
        if ($file["error"] === UPLOAD_ERR_OK) {
            // Move o arquivo enviado para o diretório de destino
            $uploadPath = $uploadDir . basename($file["name"]);
            if (move_uploaded_file($file["tmp_name"], $uploadPath)) {
                return $uploadPath;
            } else {
                return false;
            }
        } else {
            return false;
        }
    }

    // Move os arquivos e verifica se foram movidos com sucesso
    $jsonPath = moveFile($jsonFile, $uploadDir);
    $odsPath = moveFile($odsFile, $uploadDir);
    $csvPath = moveFile($csvFile, $uploadDir);

    // Verifica se os arquivos foram movidos com sucesso
    if ($jsonPath && $odsPath) {
        echo "<h1>Arquivos enviados com sucesso!</h1>";
//        echo "Arquivo JSON: " . $jsonPath . "<br>";
//        echo "Arquivo ODS: " . $odsPath . "<br>";
//        echo "Arquivo CSV: " . $csvPath . "<br>";


        // Obtém o valor do checkbox para envio de e-mails
        $sendEmails = isset($_POST["sendEmails"]) ? 'yes' : 'no';

        // Obtém a mensagem de e-mail e endereços de Cc
        $emailMessage = isset($_POST["emailMessage"]) ? escapeshellarg($_POST["emailMessage"]) : '';
        $emailCc = isset($_POST["emailCc"]) ? escapeshellarg($_POST["emailCc"]) : '';

        // Constrói o comando com base nos arquivos enviados e informações adicionais
        if ($csvPath) {
            $command = "bash ./run_script.sh $jsonPath $odsPath $csvPath $sendEmails $emailMessage $emailCc";
        } else {
            $command = "bash ./run_script.sh $jsonPath $odsPath $sendEmails $emailMessage $emailCc";
        }

        // Executa o script bash após o envio bem-sucedido dos arquivos
        //echo "<h3>$command</h3>";
        $output = shell_exec($command);
        echo "$output";

        // Gera um nome único para o arquivo ZIP com base na data e hora atual
        $zipFile = "./reports/report_" . $currentDateTime . ".zip";

        // Compacta a pasta "report"
        $zipCommand = "zip -r $zipFile " . $reportDir; 
        //echo "$zipCommand";
        shell_exec($zipCommand);

        // Verifica se o arquivo ZIP foi criado com sucesso
        if (file_exists($zipFile)) {
            // Botão de Download
            echo '<div style="text-align: center; margin-bottom: 20px;">';
            echo '<a href="' . $zipFile . '" download style="background-color: #28a745; color: #fff; border: none; border-radius: 5px; padding: 10px 20px; cursor: pointer; text-decoration: none; display: inline-block; margin-right: 10px;">Download do relatório compactado</a>';
            echo '</div>';
        } else {
            echo '<p style="color: #dc3545; text-align: center;">Erro ao compactar a pasta "report".</p>';
        }

        // Remover todos os arquivos da pasta "$dataCurrentDir"
        $removePath = $dataCurrentDir;
        // echo "REMOVER $removePath";
        shell_exec("rm -rf $removePath");

        // Executa o script bash para apagar arquivos antigos
        $command = "bash ./delete_files_reports.sh";
        $output = shell_exec($command);

    } else {
        echo "<h3>Erro ao enviar os arquivos. Certifique-se de que, pelo menos, os arquivos JSON e ODS foram escolhidos corretamente.</h3>";
    }
} else {
    echo "<h3>Nenhum arquivo enviado ou faltam arquivos necessários. Por favor, verifique e tente novamente.</h3>";
}

// Botão Voltar
echo '<div style="text-align: center;">';
echo '<button onclick="history.back()" style="background-color: #007bff; color: #fff; border: none; border-radius: 5px; padding: 10px 20px; cursor: pointer; display: inline-block;">Voltar</button>';
echo '</div>';

echo "<hr>";
echo "Todos os arquivos enviados/gerados são apagados do servidor!<br>";
//echo "$output";