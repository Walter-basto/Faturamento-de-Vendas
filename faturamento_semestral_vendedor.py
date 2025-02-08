import pandas as pd
import plotly.express as px

file_path = '/Arquivo_Faturamento_de_Vendas.xlsx'
arquivo=pd.read_excel(file_path)
df = pd.DataFrame(arquivo)
contagem_linhas2 = df[df.columns[1]].count()
print("Quantidade de Vendedores:", contagem_linhas2)
df[df.columns[9]]  = pd.to_datetime(df[df.columns[9]])
df[df.columns[10]] = pd.to_datetime(df[df.columns[10]])
df['Periodo entre o Mês de Janeiro-Junho'] = (df[df.columns[9]]  - df[df.columns[10]] ).dt.days
print(df)
fig = px.bar(df, x=df.columns[ 8],y=df.columns[1],title='Faturamento Semestral dos Vendedores')
fig.show()
