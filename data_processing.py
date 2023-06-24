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
df_valor= df_valor.rename(columns=lambda c: c.replace('.1',''))
df_volume = df[columns_qtd]

#Adicionando a coluna e linha de Totais no dataframe de valores e volumes:

df_valor.loc[:, 'Total'] = df_valor.sum(axis=1)
df_valor.loc['total', :] = df_valor.sum()
df_volume.loc[:, 'Total'] = df_volume.sum(axis=1)
df_volume.loc['total', :]= df_volume.sum() 


#criando um dataframe que traz a media preço por litro vendido por ano.

linha1 = df_valor.loc['total']
linha2 = df_volume.loc['total']
resultado = linha1/linha2
df_resultado = pd.DataFrame(resultado)
df_resultado = df_resultado.T

#criando um dataframe dos volume e valores de vendas dos ultimos 15 anos
df_valor_total = df_valor[['Total']]
df_valor_total = df_valor_total.rename(columns={'Total':'Valor (US$)'})
df_valor_total['Valor (US$)'] = df_valor_total['Valor (US$)'].apply(lambda x: '{:,.2f}'.format(x))
df_volume_total = df_volume[['Total']]
df_volume_total = df_volume_total.rename(columns={'Total':'Volume'})

df_total_final = df_valor_total.merge(df_volume_total,how='left',on='País')
df_total_final['Origem'] = 'Brasil'
df_total_final = df_total_final[['Origem', 'Volume', 'Valor (US$)']]





#exportanto os dataframes tratados:

df_valor.to_csv('./src/data/valores.csv', index=True)
df_volume.to_csv('./src/data/volume.csv', index=True)
df_resultado.to_csv('./src/data/resultado.csv', index=False)
df_total_final.to_csv('./src/data/total_final.csv', index=True)