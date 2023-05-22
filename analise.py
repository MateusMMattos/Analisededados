import pandas as pd
import plotly.express as px

tabela = pd.read_csv('./clientes.csv', encoding='latin', sep=';')
tabela = tabela.drop('Unnamed: 8', axis=1)
tabela['Salário Anual (R$)'] = pd.to_numeric(
    tabela['Salário Anual (R$)'], errors='coerce')
tabela = tabela.dropna()

# tabela com descrição

# print(tabela.describe())

# cria o grafico
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, y='Nota (1-100)',
                           histfunc='avg', text_auto=True, nbins=10)

    # exibe o grafico
    grafico.show()
