#Libs
import pandas as pd
import numpy as np

#libs gráficas
import plotly.graph_objects as go 
from plotly.subplots import make_subplots
import seaborn as sns
import matplotlib.pyplot as plt

#Streamlit
import streamlit as st
from PIL import Image


#Lendo a base de dados e tratanto a base de dados
df_resultado = pd.read_csv('./src/data/resultado.csv')
df = pd.read_csv('./src/data/ExpVinho.csv', sep=";")


#Titulo de Página
image = Image.open("./src/img/download.jpg")
st.image(image)

# Layout do aplicativo
tab0, tab1, tab2, tab3= st.tabs(["Inicio","Dados Gerais", "Paises", "Sobre"])

with tab0:

    st.title("Análise da Exportação de Vinhos Brasileiros")
        
    st.write("""
        # Bem-vindos à análise de exportação de vinhos do Brasil
        Nosso país tem uma rica tradição na produção de vinhos finos e, ao longo dos anos, temos exportado nossos produtos para todo o mundo. Através desta plataforma, estamos empolgados em compartilhar uma análise abrangente da quantidade de vinhos que exportamos e os fatores externos que influenciam essa exportação.

        ## O que vamos abordar
        - **Quantidade de Vinhos Exportados**: Uma análise ano a ano da quantidade de vinhos exportados para diferentes países. Iremos analisar os padrões de exportação nos últimos 15 anos.
        - **Fatores Externos que Influenciam a Exportação**: Uma análise profunda de como os dados climáticos, demográficos e econômicos influenciam as exportações de vinho.
        - **Prospecções Futuras**: Com base nos dados históricos e fatores externos, faremos previsões informadas sobre o futuro das exportações de vinhos do Brasil.
        - **Estratégias para Melhoria das Exportações**: Com base em nossa análise, vamos sugerir ações estratégicas que podem ser tomadas para melhorar as exportações.

        ## Nossa Jornada
        Embarque conosco nesta jornada fascinante através dos dados de nossas exportações de vinhos. Descubra as histórias por trás dos números, entenda os fatores que impulsionam nossas vendas e junte-se a nós enquanto traçamos o caminho para um futuro ainda mais brilhante para a indústria vinícola do Brasil.
        """)



with tab1:
    

    # Removendo a coluna 'Id'
    df.drop('Id', axis=1, inplace=True)

    # Tratando o dataset
    anos = list(range(1970, 2022))
    dados = []
    for ano in anos:
        df_ano = df.copy()
        df_ano['Ano'] = ano
        df_ano['Quantidade'] = df[str(ano)].astype(float)  # convertendo kg em litros (considerando 1kg=1L)
        df_ano['Valor'] = df[str(ano)].astype(float)
        dados.append(df_ano[['País', 'Ano', 'Quantidade', 'Valor']])

    df_final = pd.concat(dados)

    # Adicionando a coluna 'Origem'
    df_final['Origem'] = 'Brasil'

    # Reordenando as colunas
    df_final = df_final[['Origem', 'País', 'Ano', 'Quantidade', 'Valor']]

    
    st.dataframe(df_final)  # Mostra o dataframe no Streamlit


with tab2:

    '''
    ## Pagina 3
    
    
    
    '''


with tab3:
    
    '''
    Projeto desenvolvido para o 1º tech challenge da Fiap da turma Dados

    Participantes:

    Luiz Antonio Simette de Mello Campos
    
    Leonardo Fernandes de Moraes Alves

    Paulo Henrique Barbosa Ortiz



    Professor:

    Edgard

    Matheus    

    Info:

    Base dados:

    
    
    '''