Walter Bastos Jorge Filho

Universidade Estácio de Sá - Polo Duque de Caxias(Centro) - Rio de Janeiro

Trabalho de extensão de Análise de Dados em Python

Descrição do Faturamento_de_Vendas da análise de dados em python 

1= Importação de Bibliotecas: linhas do codigo abaixo importam as bibliotecas pandas é usada para manipulação de dados e plotly.express para criação de gráficos interativos.

import pandas as pd

import plotly.express as px


2= Leitura do Arquivo Excel e conversão do arquivo excel em dataframe do pandas: file_path, uma variavel que define o caminho do Arquivo_Faturamento_de_Vendas.xlsx que é formato excel. O read_excel(file_path) lê o arquivo Excel e  pd  armazena o conteúdo  e o converter em um DataFrame do pandas na variavel df. Isso permite que você manipule os dados facilmente.

file_path = '/Arquivo_Faturamento_de_Vendas.xlsx'

arquivo = pd.read_excel(file_path)

df = pd.DataFrame(arquivo)


3= Contagem de Vendedores: A variavel  contagem_linhas2 armazena a contagem  do número de entradas na segunda coluna do DataFrame e a função print imprime a quantidade de vendedores.

contagem_linhas2 = df[df.columns[1]].count()

print("Quantidade de Vendedores:", contagem_linhas2)


4= Conversão de Colunas para DateTime: pd.to_datetime  converte a décima e nona coluna do DataFrame para o tipo datetime.

df[df.columns[9]] = pd.to_datetime(df[df.columns[9]])

df[df.columns[10]] = pd.to_datetime(df[df.columns[10]])


5= Cálculo do Período entre Datas: Calcula a diferença em dias entre as datas das colunas 9 e 10 e cria uma nova coluna chamada 'Periodo entre o Mês de Janeiro-Junho' com esses valores. Em seguida, imprime o DataFrame atualizado.

df['Periodo entre o Mês de Janeiro-Junho'] = (df[df.columns[9]] - df[df.columns[10]]).dt.days

print(df)

 
6= Criação do Gráfico: cria um gráfico de barras usando Plotly Express, onde o eixo x representa a oitava coluna do DataFrame e o eixo y representa a segunda coluna. O título do gráfico é 'Faturamento Semestral dos Vendedores'. Finalmente, o gráfico é exibido.

fig = px.bar(df, x=df.columns[8], y=df.columns[1], title='Faturamento Semestral dos Vendedores')

fig.show()

