#Libs
import pandas as pd

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
df_valor=df_valor.rename(columns=lambda c: c.replace('.1',''))
df_volume = df[columns_qtd]

#Adicionando a coluna e linha de Totais no dataframe de valores e volumes:

df_valor['Total'] = df_valor.sum(axis=1)
df_valor.loc['total']= df_valor.sum() 
df_volume['Total'] = df_volume.sum(axis=1)
df_volume.loc['total']= df_volume.sum() 


#criando um dataframe que traz a media preço por litro vendido por ano.

linha1 = df_valor.loc['total']
linha2 = df_volume.loc['total']
resultado = linha1/linha2
df_resultado = pd.DataFrame(resultado)
df_resultado = df_resultado.T


#exportanto os dataframes tratados:

df_valor.to_csv('./src/data/valores.csv', index=True)
df_volume.to_csv('./src/data/volume.csv', index=True)
df_resultado.to_csv('./src/data/resultado.csv', index=False)


