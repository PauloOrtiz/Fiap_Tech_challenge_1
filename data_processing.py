#Libs
import pandas as pd
import numpy as np


#importação dos dados
df = pd.read_csv("./src/data/ExpVinho.csv", sep=";")

#Alteração do indice
df=df.set_index(['País'])
df.drop(columns='Id', inplace=True)


#removendo do Brasil dos dados
df.drop('Brasil', inplace=True)


#buscando os ultimos 15 anos para analise
ano_analise = df.columns[74:]
df = df[ano_analise]


# Separando e criando os dataset de valores e quantidade
columns_valor = [col for col in df.columns if '.1' in col]
columns_qtd = [col for col in df.columns if '.1' not in  col]
df_valor = df[columns_valor]
df_valor= df_valor.rename(columns=lambda c: c.replace('.1',''))
df_volume = df[columns_qtd]

#Adicionando a coluna e linha de Totais no dataframe de valores e volumes:

df_valor.loc[:, 'Total'] = df_valor.sum(axis=1)
df_valor.loc['total', :] = df_valor.sum()
df_volume.loc[:, 'Total'] = df_volume.sum(axis=1)
df_volume.loc['total', :]= df_volume.sum() 
df_volume = df_volume[df_volume['Total'] != 0]
df_valor = df_valor[df_valor['Total'] != 0]


#criando um dataframe que traz a media preço por litro vendido por ano.

linha1 = df_valor.loc['total']
linha2 = df_volume.loc['total']
resultado = linha1/linha2
df_resultado = pd.DataFrame(resultado)
#df_resultado = df_resultado.T
df_resultado = df_resultado.reset_index()
df_resultado = df_resultado.rename(columns={'index':'Anos', 'total':'Total'})
df_resultado = df_resultado.round(2)
df_resultado = df_resultado.iloc[:-1]

#criando um dataframe dos volume e valores de vendas dos ultimos 15 anos
df_valor_total = df_valor[['Total']]
df_valor_total = df_valor_total.rename(columns={'Total':'Valor (US$)'})
df_valor_total['Valor (US$)'] = df_valor_total['Valor (US$)'].astype('int64')

df_volume_total = df_volume[['Total']]
df_volume_total = df_volume_total.rename(columns={'Total':'Volume KG'})

df_total_final = df_valor_total.merge(df_volume_total,how='left',on='País')
df_total_final['Origem'] = 'Brasil'
df_total_final = df_total_final[['Origem', 'Volume KG', 'Valor (US$)']]
df_total_final = df_total_final.iloc[:-1]

#criando os valores Totais por anos:
df_valor_2 = df_valor.iloc[:-1]
df_valor_2 =df_valor_2.reset_index()
df_valor_2 = df_valor_2.drop(columns=['País', 'Total'])
total_por_ano = df_valor_2.sum()
df_total_por_ano = total_por_ano.reset_index()
df_total_por_ano.columns = ['Anos', 'Total']

#criando os Volumetria totais por anos:
df_volume_2 = df_volume.iloc[:-1]
df_volume_2 =df_volume_2.reset_index()
df_volume_2 = df_volume_2.drop(columns=['País', 'Total'])
volume_por_ano = df_volume_2.sum()
df_volume_por_ano = volume_por_ano.reset_index()
df_volume_por_ano.columns = ['Anos', 'Total']


#Criação data set de porpoção


dt=(df_valor["Total"].groupby(by=df_valor.index, sort=True ).sum())/1000000
dt= dt.sort_values(ascending=False)
dt2 = pd.DataFrame(dt)

dt2['perc_acum'] = dt2['Total'].cumsum()/dt2['Total'].sum()*100
dt2=dt2.reset_index()
dt2['group'] = np.where(dt2['perc_acum']>=95, 'Others', dt2['País'])
dt2['perc_acum'] = np.where(dt2['perc_acum']>=95, 95,dt2['perc_acum'] )
dt2 = dt2.iloc[1:]

#exportanto os dataframes tratados:

df_valor.to_csv('./src/data/valores.csv', index=True)
df_volume.to_csv('./src/data/volume.csv', index=True)
df_resultado.to_csv('./src/data/resultado.csv', index=False)
df_total_final.to_csv('./src/data/total_final.csv', index=True)
df_total_por_ano.to_csv('./src/data/total_por_ano.csv', index=False)
df_volume_por_ano.to_csv('./src/data/volume_por_ano.csv', index=False)
dt2.to_csv('./src/data/porpo.csv', index=False)