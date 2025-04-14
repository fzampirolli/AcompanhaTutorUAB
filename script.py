# -*- coding: utf-8 -*-
'''
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
'''

import sys, os, pandas as pd
import matplotlib.pyplot as plt

def verificar_argumentos(args):
    """
    Verifica se os argumentos fornecidos são válidos.
    Espera 2 ou 3 arquivos na ordem: .json, .ods, [opcional: .csv].
    Opcionalmente, aceita informações sobre envio de e-mails: 'yes' ou 'no', mensagem e e-mail Cc.
    """
    if len(args) < 2 or len(args) > 6:
        print("Erro: Número incorreto de argumentos.")
        print("Uso: python3 script.py <arquivo_json> <arquivo_ods> [<arquivo_csv>] [yes|no] [<mensagem>] [<cc_email>]")
        return False

    # Verifica a extensão dos arquivos obrigatórios
    extensoes = ['.json', '.ods']
    for i, ext in enumerate(extensoes):
        if not args[i].endswith(ext):
            print(f"Erro: O argumento {i + 1} deve ser um arquivo {ext}.")
            return False
        if not os.path.isfile(args[i]):
            print(f"Erro: Arquivo '{args[i]}' não encontrado.")
            return False

    # Verifica o arquivo CSV (opcional)
    if len(args) > 2 and args[2] != "yes" and args[2] != "no":
        if not args[2].endswith('.csv'):
            print("Erro: O terceiro argumento deve ser um arquivo .csv ou 'yes'/'no'.")
            return False
        if not os.path.isfile(args[2]):
            print(f"Erro: Arquivo '{args[2]}' não encontrado.")
            return False

    # Verifica o argumento 'yes' ou 'no' sobre o envio de e-mail
    if len(args) > 3:
        if args[2] == "yes" or args[3] == "yes":
            if len(args) < 5:
                print("Erro: Mensagem de e-mail é obrigatória quando 'yes' é especificado.")
                return False

    return True


if __name__ == "__main__":
    args = sys.argv[1:]  # Exclui o nome do script e mantém apenas os argumentos

    if not verificar_argumentos(args):
        exit(1)

    # Mapeia os argumentos obrigatórios
    file_tutores = args[0]
    file_notas = args[1]
    file_logs = None

    # Verifica se o terceiro argumento é um arquivo .csv ou uma opção 'yes'/'no'
    if len(args) > 2 and args[2].endswith('.csv'):
        file_logs = args[2]
        enviar_email = args[3] if len(args) > 3 else "no"
        if enviar_email == 'yes':
            mensagemForm = args[4] if enviar_email == "yes" and len(args) > 4 else None
            cc_email = args[5] if enviar_email == "yes" and len(args) > 5 else None
    else:
        enviar_email = args[2] if len(args) > 2 else "no"
        if enviar_email == 'yes':
            mensagemForm = args[3] if enviar_email == "yes" and len(args) > 3 else None
            cc_email = args[4] if enviar_email == "yes" and len(args) > 4 else None

    # # Exibe os argumentos recebidos (apenas para debug)
    # print("Arquivos recebidos:")
    # print(f"Tutores JSON: {file_tutores}")
    # print(f"Notas ODS: {file_notas}")
    # print(f"Logs CSV: {file_logs if file_logs else 'Nenhum'}")
    # print(f"Enviar e-mail: {enviar_email}")
    # print(f"Mensagem de e-mail: {mensagemForm if mensagemForm else 'Nenhuma'}")
    # print(f"Cc: {cc_email if cc_email else 'Nenhum'}")

    # Aqui você pode chamar a lógica para processar os arquivos e enviar e-mails.

pasta = "./tmp/" + file_tutores.split('/')[2] + "/report/"

if not os.path.exists(pasta):
    os.makedirs(pasta)

import re, csv, json

print("<p>Arquivos gerados...</p>")

#####################################################################################
### Entrada: tutores.json
### Saída: tutores_dados.csv
#####################################################################################

print("<h2>1) Grupos de Tutores e seus Alunos (arquivo JSON)</h2>")

with open(file_tutores, "r") as f:
    dic = json.load(f)

#####
import json
import re

# Carregar o arquivo JSON
with open(file_tutores, "r") as f:
    dic = json.load(f)

# Função para remover apóstrofes de strings
def remove_apostrofes(texto):
    return texto.replace("'", "") if isinstance(texto, str) else texto

# Criar um novo dicionário sem apóstrofes
dic_sem_apostrofes = {}

# Percorrer todas as chaves e valores do dicionário original
for chave, valor in dic.items():
    # Remover apóstrofes da chave
    nova_chave = remove_apostrofes(chave)

    # Remover apóstrofes do valor (se for string)
    if isinstance(valor, str):
        novo_valor = remove_apostrofes(valor)
    elif isinstance(valor, list):
        # Se for lista, aplicar a remoção de apóstrofes em cada item
        novo_valor = [remove_apostrofes(item) for item in valor]
    else:
        novo_valor = valor

    # Adicionar ao novo dicionário
    dic_sem_apostrofes[nova_chave] = novo_valor

# Substituir o dicionário original
dic = dic_sem_apostrofes
#####

# Regex para capturar o nome e o e-mail
tutores = dic['Tutores']
pattern = r"([\w\s]+)\s\(([\w\.\-]+@[\w\.\-]+)\)"
pattern = r"([\w\s']+)\s\(([\w\.\-]+@[\w\.\-]+)\)"
matches = re.findall(pattern, tutores)

# Criar um dicionário com nomes como chave e e-mails como valor
tutores_dict = {nome.strip(): email for nome, email in matches}

# Criar uma lista para armazenar todas as linhas dos dados a serem escritos no arquivo CSV
linhas = []

# Iterar sobre o dicionário
for grupo, texto_emails in dic.items():
    # Encontrar todos os pares de nome e email usando regex
    pares_nome_email = re.findall(r'([\w\s\'\-À-ÿ]+)\s*\(([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})\)', texto_emails)

    # Iterar sobre os pares de nome e email
    for nome, email in pares_nome_email:
        # Adicionar uma linha ao arquivo CSV com o nome, email e o tutor correspondente
        nome = nome.replace("'", "")
        linhas.append([nome.strip(), email, grupo])

# Escrever os dados no arquivo CSV
with open(pasta + 'tutores_dados.csv', 'w', newline='') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    # Escrever o cabeçalho
    escritor.writerow(['Nome', 'Email', 'Grupo'])
    # Escrever as linhas de dados
    escritor.writerows(linhas)

# Leia o CSV para criar o DataFrame
df = pd.read_csv(pasta + 'tutores_dados.csv')

# Filtre os tutores
tutores_df = df[df['Grupo'] == 'Tutores']

# Filtre os outros grupos
outros_grupos_df = df[df['Grupo'] != 'Tutores'].copy()  # Use .copy() para evitar o aviso

# Inicialize as colunas Tutor1, Tutor2 e Tutor3 como vazio usando .loc
outros_grupos_df.loc[:, 'Tutor1'] = ''
outros_grupos_df.loc[:, 'Tutor2'] = ''
outros_grupos_df.loc[:, 'Tutor3'] = ''

# Crie listas dos tutores
tutores = tutores_df['Nome'].tolist()

dic_tutor = {}

# Adicionar tutores às colunas Tutor1, Tutor2 e Tutor3, se existir
for tutor in tutores:
    # Identifique os grupos onde o tutor está presente
    grupos_com_tutor = outros_grupos_df[outros_grupos_df['Nome'] == tutor]['Grupo'].unique()

    dic_tutor[tutor] = grupos_com_tutor

    for grupo in grupos_com_tutor:
        # Identifique os membros do grupo
        membros_grupo = outros_grupos_df[outros_grupos_df['Grupo'] == grupo]

        # Adicione o tutor nas colunas Tutor1, Tutor2 ou Tutor3
        if membros_grupo['Tutor1'].iloc[0] == '':
            outros_grupos_df.loc[outros_grupos_df['Grupo'] == grupo, 'Tutor1'] = tutor
        elif membros_grupo['Tutor2'].iloc[0] == '':
            outros_grupos_df.loc[outros_grupos_df['Grupo'] == grupo, 'Tutor2'] = tutor
        else:
            outros_grupos_df.loc[outros_grupos_df['Grupo'] == grupo, 'Tutor3'] = tutor

# Combine de volta com os tutores, se necessário
df_final = pd.concat([outros_grupos_df, tutores_df], ignore_index=True)

# Salve o DataFrame atualizado de volta em um CSV
df_final.to_csv(pasta + 'tutores_dados.csv', index=False)

print("<p>Arquivo CSV com relação tutores alunos:", '<b>tutores_dados.csv</b></p>')

#####################################################################################
### Entrada: notas.ods
### Também usa tutores_dados.csv
###
### Inclui uma coluna no final informando o grupo/tutor(es)
###
### Saída: notas_filtros.csv
#####################################################################################
"""# 2) Analisar feedbacks dos tutores em Notas"""

print("<h2>2) Feedbacks dos tutores em Notas (arquivo ODS)</h2>")

# !pip install odfpy

# Leia o arquivo ODS
notas_df = pd.read_excel(file_notas)  # <<<<< MUDAR O NOME DO ARQUIVO AQUI!!!

# Junte as colunas "Nome" e "Sobrenome" em uma nova coluna "Nome Completo"
notas_df['Nome'] = notas_df['Nome'] + ' ' + notas_df['Sobrenome']

# remover apóstrofe dos nomes
notas_df['Nome'] = notas_df['Nome'].str.replace("'", "", regex=False)

# Remova as colunas especificadas
cols = ["Sobrenome", "Número de identificação", "Instituição", "Departamento", "Último download realizado neste curso."]
notas_df = notas_df.drop(columns=cols)

# Selecione apenas as linhas onde a coluna do terceiro item não seja "-"
# notas_df = notas_df[notas_df[list(notas_df.columns)[2]] != "-"]

# Função para encontrar Grupo pelo nome do aluno
def encontrar_chave(nome):
    for chave, lista_nomes in dic.items():
        pares_nome_email = re.findall(r'(\w+(?:\s+\w+)*)\s*\(([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,})\)',
                                      lista_nomes)
        for nome_email in pares_nome_email:
            if nome == nome_email[0]:
                return chave
    return None

# Adicionar a coluna Grupo/Tutur(a) ao DataFrame
notas_df['Grupo'] = notas_df['Nome'].apply(encontrar_chave)

# Remover linhas de `notas_df` onde o nome está nas chaves de `tutores_dict`
tutores_nomes = set(tutores_dict.keys())  # Conjunto dos nomes dos tutores
#tutores_nomes.add('Victor Fernandez Nascimento')

# Salve o DataFrame filtrado em um novo arquivo CSV
notas_df.to_csv(pasta + 'notas_filtros.csv', index=False)
print("<p>Arquivo CSV com notas e cometários dos tutores, por aluno:", '<b>notas_filtros.csv</b></p>')

# print(tutores_dict)
# exit(1)

#####################################################################################
### Configura Email
#####################################################################################

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import ssl
import os

def envia_email(servidor, porta, FROM, PASS, TO, CC, subject, texto, anexo=[]):
    msg = MIMEMultipart()
    msg['From'] = FROM
    msg['To'] = TO
    msg['Cc'] = ', '.join(CC) if isinstance(CC, list) else CC  # Adiciona Cc
    msg['Subject'] = subject
    msg.attach(MIMEText(texto, 'plain'))

    # Anexa os arquivos
    for f in anexo:
        if isinstance(f, list):
            f = f[0]  # Se for uma lista, pega o primeiro item
        try:
            # Certifique-se de que o caminho do arquivo esteja correto
            if not os.path.exists(f):
                print(f"Arquivo {f} não encontrado.")
                continue

            with open(f, 'rb') as file:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(file.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(f)}"')
                msg.attach(part)
            #print(f"Anexo {f} adicionado com sucesso.")
        except Exception as e:
            print(f"Erro ao anexar o arquivo {f}: {e}")

    try:
        # Preparar lista completa de destinatários
        recipients = [TO] + (CC if isinstance(CC, list) else [CC])

        # Configurar e enviar o e-mail
        context = ssl.create_default_context()
        context.set_ciphers("DEFAULT@SECLEVEL=1")  # Adiciona suporte a chaves DH menores
        with smtplib.SMTP(servidor, porta) as gm:
            gm.ehlo()
            gm.starttls(context=context)
            gm.login(FROM, PASS)
            gm.sendmail(FROM, recipients, msg.as_string())
            print(
                f"<br>E-mail enviado com sucesso para {TO} "
                f"(Cc: {msg.get('Cc', 'N/A')}; "
                f"Anexo: {anexo[0].split('/')[-1] if anexo else 'Nenhum'})"  # Trata lista vazia ou None
            )

    except Exception as e:
        print(f"Erro ao enviar o e-mail: {e}")

# Parâmetros do servidor

import os
from dotenv import load_dotenv

# Carregue as variáveis de ambiente do arquivo .env
load_dotenv('/etc/secrets/.UAB.env')

'''
sudo mkdir -p /etc/secrets
sudo mv /caminho/para/seu/.env /etc/secrets/.env
sudo chown www-data:www-data /etc/secrets/.env
sudo chmod 600 /etc/secrets/.env
sudo chmod 710 /etc/secrets
sudo chown root:www-data /etc/secrets

# conteúdo do arquivo .UAB.env
sudo cat /etc/secrets/.UAB.env  
MY_PORTA=587
WEBMC_TEST_SERVER=smtp.ufabc.edu.br    # MUDAR!!!
WEBMC_TEST_FROM=webmctest@ufabc.edu.br # MUDAR!!!
WEBMC_TEST_PASS=ufabc12345             # MUDAR!!!
'''

my_porta = os.getenv('MY_PORTA')
webMCTest_SERVER = os.getenv('WEBMC_TEST_SERVER')
webMCTest_FROM = os.getenv('WEBMC_TEST_FROM')
webMCTest_PASS = os.getenv('WEBMC_TEST_PASS')

# print(my_porta, webMCTest_SERVER, webMCTest_FROM, webMCTest_PASS)
# exit(1)

#####################################################################################
### Entrada: notas.ods
### Também usa tutores_dados.csv
###
### Saída: notas_filtros.png
#####################################################################################

import matplotlib.pyplot as plt
import numpy as np
import re

# Conta alunos por grupo e organiza os tutores
dic_tutor_total = {grupo: len(alunos.split(', ')) - 1 for grupo, alunos in dic.items()}
notas_cols = notas_df.columns[2:-2:2]  # Seleciona colunas alternadas (tarefas)
feedback_cols = notas_df.columns[3:-1:2]  # Colunas de feedback correspondentes
grupos = [key for key in dic_tutor_total.keys() if key != 'Tutores']

# Extrair tutores e e-mails
tutores_dict = {chave.strip(): valor for chave, valor in re.findall(r"([\w\s]+)\s\(([\w\.\-]+@[\w\.\-]+)\)", dic['Tutores'])}

# Geração do gráfico com correção
for grupo in sorted(grupos):
    # Identifica tutor do grupo
    tutor_atual = next((tutor for tutor in tutores_dict if dic_tutor[tutor] == grupo), "Tutor desconhecido")
    email = tutores_dict.get(tutor_atual, "Email não encontrado")

    grupo_df = notas_df[notas_df['Grupo'] == grupo]
    total_alunos = dic_tutor_total[grupo]

    # Lista completa de alunos no grupo (extraída do dicionário `dic` usando regex)
    pattern = r"([\w\s]+)\s\(([\w\.\-]+@[\w\.\-]+)\)"
    matches = re.findall(pattern, dic[grupo])
    todos_nomes = [match[0].strip() for match in matches]

    azul, vermelho, cinza, feedback_contagem = [], [], [], []
    nomes_sem_nota, nomes_busca_ativa = [], []

    for nota_col, feedback_col in zip(notas_cols, feedback_cols):
        # Contagem de notas
        com_nota = grupo_df[nota_col].apply(lambda x: x != "-").sum()
        sem_nota = grupo_df[nota_col].apply(lambda x: x == "-").sum()
        busca_ativa = total_alunos - com_nota - sem_nota + 1

        # Identificação de nomes
        sem_nota_nomes = grupo_df[grupo_df[nota_col] == "-"]["Nome"].tolist()
        nomes_com_ou_sem_nota = set(grupo_df[grupo_df[nota_col] != "-"]["Nome"].tolist()).union(set(sem_nota_nomes))
        busca_ativa_nomes = set(todos_nomes) - nomes_com_ou_sem_nota - {tutor_atual}

        # Contagem de feedbacks com mais de 50 caracteres
        feedback_validos = grupo_df[feedback_col].apply(lambda x: len(str(x)) > 50).sum()

        azul.append(com_nota)
        vermelho.append(sem_nota)
        cinza.append(busca_ativa)
        feedback_contagem.append(feedback_validos)

        nomes_sem_nota.append("\n".join(sorted(nome[:30] for nome in sem_nota_nomes)))
        nomes_busca_ativa.append("\n".join(sorted(nome[:30] for nome in busca_ativa_nomes)))

    # Criação do gráfico
    fig, ax = plt.subplots(figsize=(12, 8))
    bar_positions = np.arange(len(notas_cols))
    bar_width = 0.7  # Dobro da largura anterior para colunas de notas
    feedback_bar_width = bar_width / 4  # Metade da largura anterior para feedbacks

    # Barras de notas e feedbacks
    ax.bar(bar_positions, azul, width=bar_width, color='#6baed6', label='Com Nota')
    ax.bar(bar_positions, vermelho, bottom=azul, width=bar_width, color='#fc9272', label='Sem Nota')
    ax.bar(bar_positions, cinza, bottom=np.array(azul) + np.array(vermelho), width=bar_width, color='#d9d9d9', label='Busca Ativa')
    ax.bar(bar_positions, feedback_contagem, width=feedback_bar_width, color='#fec44f', label='Feedbacks\n>50 caracteres')

    # Adicionar nomes dos alunos "Sem Nota" e "Não Enviaram"
    for i, (texto_sem_nota, texto_busca_ativa) in enumerate(zip(nomes_sem_nota, nomes_busca_ativa)):
        if texto_sem_nota:
            ax.text(
                x=i,
                y=azul[i] + vermelho[i] / 2,
                s=texto_sem_nota,
                ha='center',
                va='center',
                fontsize=6,
                color='darkred',  # Cor mais forte
                alpha=1,  # Texto mais destacado
            )
        if texto_busca_ativa:
            ax.text(
                x=i,
                y=azul[i] + vermelho[i] + cinza[i] / 2,
                s=texto_busca_ativa,
                ha='center',
                va='center',
                fontsize=6,
                color="#444444",  # Cor mais forte que 'darkgray'
                alpha=0.9,  # Texto mais destacado
            )

    # Configuração do gráfico
    ax.set_xticks(bar_positions)
    ax.set_xticklabels(notas_cols, rotation=45, ha='right', fontsize=8)
    ax.set_xlabel('Atividades', fontsize=8)
    ax.set_ylabel('Número de Alunos', fontsize=8)
    ax.set_title(f'Grupo {grupo} - {tutor_atual} ({email})', fontsize=10, fontweight='bold', color='darkblue')
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=6)
    plt.tight_layout(rect=[0, 0, 0.85, 1])  # Deixa espaço à direita para a legenda
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()

    # Salvar gráfico
    nome_arquivo = pasta + f"{grupo.replace(' ', '')}.png"
    plt.savefig(nome_arquivo, dpi=300, bbox_inches="tight")
    plt.close()

    # Anexo(s)
    anexo = [nome_arquivo]  # Usar caminho absoluto
    # mensagem2 = mensagem.replace('Prezado(a) Tutor(a),', 'Prezado(a) Tutor(a) ' + tutor_atual + ',')
    assunto = 'Mensagem automática sobre as atividades dos tutores no Moodle'

    # Enviar o e-mail
    destinatario = email # ENVIA EMAIL AOS TUTORES
    #destinatario = "fzampirolli@gmail.com" # PARA TESTES
    if enviar_email == 'yes':
        mensagem2 = mensagemForm
        CC = cc_email.split(',')
        envia_email(webMCTest_SERVER, my_porta, webMCTest_FROM, webMCTest_PASS, destinatario, CC, assunto, mensagem2, anexo)
    #break

"""## Agrupar feedbacks por similaridades"""
#####################################################################################
### Entrada: notas.ods
### Também usa tutores_dados.csv
###
### Saída: notas_cluster.txt
#####################################################################################
# Importar bibliotecas necessárias
import textwrap
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Ler o arquivo CSV
notas_df = pd.read_csv(pasta + 'notas_filtros.csv', encoding='utf-8')

# Filtrar as colunas que contêm "(Feedback)"
colunas_feedback = [col for col in notas_df.columns if "(Feedback)" in col]

# Transformar os valores de todas as colunas selecionadas em uma lista de células individuais,
# removendo os valores NaN
celulas_feedback = notas_df[colunas_feedback].stack().dropna().astype(str).reset_index()

# Obter os textos limpos (removendo valores vazios)
textos_limpios = celulas_feedback[0].str.strip()
textos_limpios = textos_limpios[textos_limpios != ""]

# Usar TF-IDF para vetorizar os textos
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(textos_limpios)

# Executar o algoritmo de agrupamento K-Means
n_clusters = min(10, len(textos_limpios))  # Ensure n_clusters <= n_samples
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(tfidf_matrix)

# Adicionar os rótulos de cluster ao DataFrame de células
celulas_feedback['Cluster'] = kmeans.labels_

# Mapear os clusters de volta para o DataFrame original
def atribuir_clusters(row):
    textos_row = row.dropna().astype(str).str.strip()
    clusters = celulas_feedback.loc[
        celulas_feedback[0].isin(textos_row),
        'Cluster'
    ].tolist()
    return clusters

notas_df['Clusters'] = notas_df[colunas_feedback].apply(atribuir_clusters, axis=1)

# Salvar a saída em um arquivo TXT
with open(pasta + "notas_cluster.txt", "w", encoding="utf-8") as f:
    for cluster_id in range(kmeans.n_clusters):
        f.write(f"\n#########\nCluster {cluster_id + 1}:\n#########\n")

        # Selecionar os textos e grupos do cluster atual
        cluster_samples = celulas_feedback[celulas_feedback['Cluster'] == cluster_id]
        for _, row in cluster_samples.iterrows():
            texto = row[0]  # Texto da célula
            linha_original = row['level_0']  # Índice da linha original no DataFrame
            grupo = notas_df.loc[linha_original, 'Grupo']  # Grupo associado à linha original

            try:
                f.write(f"Grupo: {grupo} - Texto: \n{texto}")
            except Exception as e:
                f.write(f"ERRO::{e}")
            f.write("\n--\n\n")
print("<p>Arquivo TXT com agrupamentos dos comentários dos tutores(as):", "<b>notas_cluster.txt</b></p>")



#####################################################################################
### Entrada: arquivo logs.csv
### Também usa tutores_dados.csv
###
### Saída: logs_alunos.png
#####################################################################################

"""# 3) Analisar alunos por tutor(a) através do log da atividade no Moodle"""

try:

    print("<h2>3) Alunos por tutor(a) através do log da atividade no Moodle (arquivo CSV)</h2>")

    # Defina o formato da data e hora
    date_format = '%d/%m/%y, %H:%M:%S'

    # Use o argumento `date_format` ao ler o CSV
    df = pd.read_csv(file_logs, parse_dates=['Hora'], date_format=date_format)

    # Remover linhas onde o "Usuário afetado" e "Nome completo" é igual a "-" ou "Nome completo" é igual a "Usuário afetado"
    df = df[(df['Usuário afetado'] != "-") & (df['Nome completo'] != "-") & (df['Nome completo'] != df['Usuário afetado'])]

    if df.shape[0]:

      # Ordenar primeiro por nome e depois por hora
      df_ordenado = df.sort_values(by=['Nome completo', 'Hora'])

      """### Incluir tutores(as) nas últimas colunas"""

      # Ler o arquivo tutores_dados.csv com "Nome", "Email" "Grupo" e "Tutores"
      concatenado_df = pd.read_csv(pasta + 'tutores_dados.csv', encoding='utf-8')

      # Remover duplicatas do DataFrame concatenado_df
      concatenado_df = concatenado_df.drop_duplicates(subset='Nome')

      # Adicionar a coluna "Tutor(a)" ao arquivo logs0_ordenado.csv com base nas informações do arquivo concatenado.csv
      df_ordenado['Grupo'] = df_ordenado['Nome completo'].map(concatenado_df.set_index('Nome')['Grupo'])
      df_ordenado['Tutor1'] = df_ordenado['Nome completo'].map(concatenado_df.set_index('Nome')['Tutor1'])
      df_ordenado['Tutor2'] = df_ordenado['Nome completo'].map(concatenado_df.set_index('Nome')['Tutor2'])
      df_ordenado['Tutor3'] = df_ordenado['Nome completo'].map(concatenado_df.set_index('Nome')['Tutor3'])

      # print('Coluna Tutor(a) adicionada e arquivo logs0_ordenado_com_tutor.csv salvo com sucesso.<br>')

      """### Filtrar alunos por tutor(a)"""

      filtro = df_ordenado['Tutor1'].notnull()
      logs_filtrados_df = df_ordenado[filtro]

      # Agrupar os dados pelo nome completo e obter a lista de alunos sem repetição
      usuarios_por_nome_completo = logs_filtrados_df.groupby('Nome completo')['Usuário afetado'].unique()


      # Contar o número de vezes que cada usuário aparece
      usuarios_afetados = logs_filtrados_df['Nome completo'].value_counts()

      # Ordenar os dados por nome do tutor em ordem alfabética
      usuarios_afetados_sorted = usuarios_afetados.sort_index()

      # Definir cores para as barras
      cores = ['skyblue', 'salmon', 'lightgreen', 'gold', 'orchid']  # Adicione mais cores conforme necessário

      # Criar o gráfico de barras
      plt.figure(figsize=(10, 6))
      # barplot = usuarios_afetados_sorted.plot(kind='bar', color=cores, zorder=2)  # Definir zorder para as barras

      # Criar o gráfico de barras
      ax = usuarios_afetados_sorted.plot(kind='bar', color=cores, zorder=2)

      # Adicionar rótulos personalizados e números de alunos em cada barra
      for i, (index, value) in enumerate(usuarios_afetados_sorted.items()):
          # Compor a string dos rótulos
          labels = '\n'.join(dic_tutor[index]) + '\n' + str(value)
          # Adicionar o texto acima da barra
          ax.text(i, value + 0.5, labels, ha='center', va='bottom')

      # Ajustar o limite superior do eixo y para criar espaço adicional
      ax.set_ylim(0, 1.2 * usuarios_afetados_sorted.max())

      # Adicionar grade apenas na horizontal
      plt.grid(axis='y', zorder=1)  # Definir zorder para a grade menor que o das barras

      # Definir título e rótulos dos eixos
      plt.title('Número de Alunos (com repetição) por Tutor(a)')
      plt.xlabel('Nome Tutor(a)')
      plt.ylabel('Número de Alunos')

      plt.xticks(rotation=45, ha='right')  # Ajustar rotação dos rótulos do eixo x

      plt.tight_layout()
      plt.savefig(pasta + "logs_alunos.png", dpi=300,
                  bbox_inches="tight")  # Ajustar nome do arquivo e dpi conforme necessário
      plt.close()
      print("<p>Arquivo PNG com relação dos alunos que tiveram interações por tutor(a):", '<b>logs_alunos.png</b></p>')
    else:
        print("<p>ERRO ao gerar logs_alunos.*. Tutores não tiveram interações com alunos</p>")

    """### Lista de alunos sem repetição para cada Tutor(a)"""
    #####################################################################################
    ### Entrada: arquivo logs.csv
    ### Também usa tutores_dados.csv
    ###
    ### Saída: logs_alunos.txt
    #####################################################################################

    arquivo = pasta + 'logs_alunos.txt'

    if df.shape[0]:
        with open(arquivo, 'w') as f:
            f.write("### Lista de Alunos sem repetição para cada Tutor(a)\n\n")

            for nome_completo, usuarios_afetados in sorted(usuarios_por_nome_completo.items()):

                f.write(f"Tutor(a): {nome_completo}  (")
                f.write(', '.join(dic_tutor[nome_completo]) + ')\n')

                for i, usuario_afetado in enumerate(sorted(usuarios_afetados)):
                    f.write(f"{i + 1:2}. {usuario_afetado}\n")

                f.write("\n")
        print("<p>Arquivo TXT com relação dos alunos que tiveram interações por tutor(a):", '<b>logs_alunos.txt</b></p>')
except:
    pass