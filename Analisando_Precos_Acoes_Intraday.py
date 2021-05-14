

!pip install yahooquery
import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from yahooquery import Ticker


# Definir uma lista de simbolos (ações) de interesse
symbols_list = ['PRIO3.SA']
# Criar um objeto Ticker (para fazer o download de dados de cotação de ações)
tc = Ticker(symbols_list)
# Fazer o download de dados de um período de 60 dias, com intervalor de 1d entre cada medição
# Lista de períodos e intervalos possíveis: https://yahooquery.dpguthrie.com/guide/ticker/historical/
df = tc.history(period='30d', interval="15m")
# Mostrar os primeiros 5 registros do dataframe df

# Converter o índice (multi-nível) em colunas
df_reset = df.reset_index()

#Criando object dia para separar o dia da hora
dia = df_reset['date']
print(dia)

#separando o dia da hora
df_reset['hora'] = dia.dt.strftime("%H:%M:%S")
df_reset['dia'] = dia.dt.strftime("%Y-%m-%d")
df_clean = df_reset.drop(columns=['volume', 'low', 'open', 'high'])
df_clean.head()


#>Gerando Primeiro Gráfico
import seaborn as sns
sns.relplot(data=df_clean, kind='line', aspect=3, x='hora', y='close', hue='symbol')

#>Gerando Segundo Gráfico

#Calculando a média dos fechamentos por hora
df_media = df_clean.groupby(['hora']).mean(['close'])

sns.relplot(data=df_media, kind='line', aspect=7, x='hora', y='close')
