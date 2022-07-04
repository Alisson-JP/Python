# Iremos compilar informações de uma pasta com vários arquivos, extrair as informações
# desejadas, e apresetá-las como quisermos

# Lógica de Programação

# Passo 0 - Entender o desafio que eu quero resolver

# Passo 1 - Percorrer todos os arquivos da pasta base de dados (Pasta de Vendas)
  # biblioteca [ os ] tem a ferramenta necessária para percorrer pastas
import os
  # biblioteca para trabalhar com conteúdo de arquivos (base de dados)
import pandas as pd
  # foi dado um apelido para o panda [ pd ]

  # criar uma variável para receber as infos da pasta destino
  # variável [ lista_arquivo ] será criada

lista_arquivo = os.listdir("/content/drive/MyDrive/Python/Vendas")

# criar uma tabela (planilha) para receber os dados de todas as demais planilhas
# tabela no python é chama [ DataFrame ]

tabela_total = pd.DataFrame()

# Passo 2 - Importar as bases de dados de vendas
  # criar uma estrutura de repetição, usaremos [ for ]
  # for variavel in lista_itens

for arquivo in lista_arquivo:
  # criar uma formatação dinâmica para receber o caminho correto de cada arquivo
  # vamos usar o [ printf ] e
  # adicionar chaves para incluir o endereço individual
  # condicionar, extrair informações apenas se tiver "vendas" no arquivo
  if "Vendas" in arquivo:
      
  # se tivesse alguma palavra com letra maiúscula ou minúscula
  # if "vendas" in arquivo.lower():

  # importar o arquivo
  # selecionar o tipo de arquivo para o panda (pd) ler
  # colocar essa leitura numa variável
    tabela = pd.read_csv(f"/content/drive/MyDrive/Python/Vendas/{arquivo}")
    # adicionar cada planilha individualmente à tabela total
    tabela_total = tabela_total.append(tabela)

# Passo 3 - Tratar / Compilar as bases de dados
display(tabela_total)

# Passo 4 - Calcular o produto mais vendido (em quantidade)
# será necessário agrupar a coluna [ Produto ] enquanto
# soma-se a coluna [ Quantidade Vendida ]

# vamos criar uma nova tabela que agrupará os dados produtos
tabela_produtos = tabela_total.groupby("Produto").sum()

# para selecionar as tabelas específicas que queremos 
tabela_produtos = tabela_produtos[["Quantidade Vendida", "Preco Unitario"]]

# para ordenar
# sort_values(by="colunaDeReferência", parâmetro de ordenamento)
# parêmtro de ordenamento = ascending=False = crescente do menor para o maior
tabela_produtos = tabela_produtos[["Quantidade Vendida", "Preco Unitario"]].sort_values(by="Quantidade Vendida", ascending=False)

display(tabela_produtos)

# Passo 5  - Calcular o produto que mais faturou (em faturamento)

# vamos criar uma nova coluna, para calcular o faturamento de cada item, ou seja
# a quantidade vendida vezes o valor unitário

tabela_total["Faturamento"] = tabela_total["Quantidade Vendida"] * tabela_total["Preco Unitario"]

# criaremos uma nova tabela, agrupando os produtos, enquanto somamos o faturamento

tabela_faturamento = tabela_total.groupby("Produto").sum()

# selecionar apenas as colunas Quantidade, preço e Faturamento
tabela_faturamento = tabela_faturamento[["Quantidade Vendida", "Preco Unitario", "Faturamento"]]

# ordenar do maior para o menor
tabela_faturamento = tabela_faturamento[["Quantidade Vendida", "Preco Unitario", "Faturamento"]].sort_values(by="Faturamento", ascending=False)


display(tabela_faturamento)

# Passo 6 - Calcular a loja/cidade que mais vendeu (em faturamento) - criar um gráfico/dashboard

# criar nova tabela, agrupando as lojas, enquanto soma o restante

tabela_lojas = tabela_total.groupby('Loja').sum()

# selecionar apenas a coluna de Faturamento, e ordenar do menor para o maior
tabela_lojas = tabela_lojas[["Faturamento"]].sort_values(by="Faturamento", ascending=False)

display(tabela_lojas)

# vamos criar o gráfico importando uma nova biblioteca [ plotly], dando um apelido [ px ]

import plotly.express as px

# criar a variável que receberá o gráfico, e escolher qual tipo de gráfico da biblioteca px e
# informar qual a tabela base, e quais serão os eixos (x e y)

# a primeira coluna, o panda reconhece como índice, e não coluna propriamente, então
# é necessário, mudar o [ 'Loja' ] por [ tabela_lojas.index ]
# grafico = px.bar(tabela_lojas, x='Loja', y='Faturamento')

grafico = px.bar(tabela_lojas, x=tabela_lojas.index , y='Faturamento')

# executar comando para mostrar o gráfico

grafico.show()

