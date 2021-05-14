################################## ANALISANDO CURVA DE COVID EM CIDADES SELECIONADAS EM PYTHON ######################################

#base: https://covid.saude.gov.br/

import pandas as pd
#df = pd.read_csv('/content/HIST_PAINEL_COVIDBR_20fev2021.csv', sep = ";")  (DESMARCAR)
df = pd.read_csv('/content/HIST_PAINEL_COVIDBR_04mai2021.csv', sep = ";")  # (Comentar essa linha)
df.info()

import datetime

#Escolha as Cidades
city1 = 'Monte Carmelo'
city2 = 'São Paulo'
city3 = 'Uberlândia'

#Selecionar as linhas nas quais o valor da coluna está listado (no caso as cidades)
cidades = [city1, city2, city3]
indicador = df.municipio.isin(cidades)
indicador

df_municipios = df[indicador][['municipio', 'casosAcumulado','obitosAcumulado','casosNovos','Recuperadosnovos','data','populacaoTCU2019']]
df_municipios['data'] = pd.to_datetime(df_municipios['data'])
df_municipios['anomes'] = df_municipios['data'].dt.strftime("%Y-%m")
df_municipios = df_municipios.set_index('data')

#Escolha a variável a ser analisada
variavel = 'obitosAcumulado'

#Construindo o data frame com as informações ecolhidas
x  = df_municipios[df_municipios['municipio'] == city1].index
y1 = df_municipios[df_municipios['municipio'] == city1][variavel]
y2 = df_municipios[df_municipios['municipio'] == city2][variavel]
y3 = df_municipios[df_municipios['municipio'] == city3][variavel]
y4 = df_municipios[df_municipios['municipio'] == city1]['populacaoTCU2019']
y5 = df_municipios[df_municipios['municipio'] == city2]['populacaoTCU2019']
y6 = df_municipios[df_municipios['municipio'] == city3]['populacaoTCU2019']
df_conj = pd.DataFrame({'Período': x, city1: y1, city2: y2, city3:y3, 'pop1': y4, 'pop2': y5, 'pop3': y6 })

df_conj['tx_1'] = df_conj[city1]/df_conj['pop1']*10000
df_conj['tx_2'] = df_conj[city2]/df_conj['pop2']*10000
df_conj['tx_3'] = df_conj[city3]/df_conj['pop3']*10000
df_conj.head()

#Gerando o Gráfico
# libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Data

sns.set(rc={'figure.figsize':(14, 8)})

# multiple line plot
titulo = variavel + ' por 10.000 hab'
plt.title(titulo)
plt.plot( 'Período', 'tx_1', data=df_conj, marker='', markerfacecolor='red', markersize=12, color='red', linewidth=4, label=city1)
plt.plot( 'Período', 'tx_2', data=df_conj, marker='', color='blue', linewidth=2, label=city2)
plt.plot( 'Período', 'tx_3', data=df_conj, marker='', color='green', linewidth=2, linestyle='dashed', label=city3)
plt.legend()
