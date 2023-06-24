#Libs
import pandas as pd
import numpy as np

#libs gráficas
import plotly.graph_objects as go 
from plotly.subplots import make_subplots
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

#Streamlit
import streamlit as st
from PIL import Image


#Lendo a base de dados e tratanto a base de dados
df_resultado = pd.read_csv('./src/data/resultado.csv')
df = pd.read_csv('./src/data/ExpVinho.csv', sep=";")
df_total = pd.read_csv('./src/data/total_final.csv')


#Titulo de Página
image = Image.open("./src/img/download.jpg")
st.image(image)
st.title("Análise da Exportação de Vinhos Brasileiros")

# Layout do aplicativo
tab0, tab1, tab2, tab3= st.tabs(["Inicio","Dados Gerais", "Paises", "Sobre"])

with tab0:

    
        
    st.write("""
        ## Bem-vindos à análise de exportação de vinhos do Brasil
        Nosso país tem uma rica tradição na produção de vinhos finos e, ao longo dos anos, temos exportado nossos produtos para todo o mundo. Através desta plataforma, estamos empolgados em compartilhar uma análise abrangente da quantidade de vinhos que exportamos e os fatores externos que influenciam essa exportação.

        ### O que vamos abordar
        - **Quantidade de Vinhos Exportados**: Uma análise ano a ano da quantidade de vinhos exportados para diferentes países. Iremos analisar os padrões de exportação nos últimos 15 anos.
        - **Fatores Externos que Influenciam a Exportação**: Uma análise profunda de como os dados climáticos, demográficos e econômicos influenciam as exportações de vinho.
        - **Prospecções Futuras**: Com base nos dados históricos e fatores externos, faremos previsões informadas sobre o futuro das exportações de vinhos do Brasil.
        - **Estratégias para Melhoria das Exportações**: Com base em nossa análise, vamos sugerir ações estratégicas que podem ser tomadas para melhorar as exportações.

        ## Nossa Jornada
        Embarque conosco nesta jornada fascinante através dos dados de nossas exportações de vinhos. Descubra as histórias por trás dos números, entenda os fatores que impulsionam nossas vendas e junte-se a nós enquanto traçamos o caminho para um futuro ainda mais brilhante para a indústria vinícola do Brasil.
        """)



with tab1:
    
    st.write("""
        ## Análise de Comércio - Últimos 15 anos

        Caros Acionistas,

        É um prazer apresentar-lhes a nossa análise detalhada do comércio dos últimos 15 anos. Este relatório visa oferecer uma visão abrangente das nossas transações, ilustrando a origem dos nossos produtos, o volume negociado e o valor total para cada país com o qual fizemos negócios.

        Este conjunto de dados nos permitirá entender melhor a dinâmica do nosso comércio internacional, identificando tendências, pontos fortes e áreas de potencial crescimento. Nesta análise, focamos em fornecer informações precisas e atualizadas que podem nos ajudar a tomar decisões estratégicas e informadas para o futuro da nossa empresa.

        Vale ressaltar que, para fins desta análise, adotamos a equivalência de que 1 kg é igual a 1 litro. Isso é importante para padronizar nossas métricas e proporcionar uma comparação justa entre diferentes produtos e volumes.

        Vamos explorar juntos essas informações valiosas e discutir como elas podem ser utilizadas para potencializar nosso crescimento e rentabilidade futura.
    """)
    df_total = df_total[['Origem','País', 'Volume KG', 'Valor (US$)']]
    st.dataframe(df_total,hide_index=True,use_container_width=True)  # Mostra o dataframe no Streamlit

    

    st.write(
    """
    ## Análise do Valor Médio de Venda por Litro de Vinho ao longo de 15 Anos

    Prezados acionistas,

    É com grande satisfação que compartilhamos os resultados obtidos ao longo dos últimos 15 anos na venda de nosso vinho. Nesse período, observamos uma notável dinâmica no valor médio de venda por litro, o que demonstra o esforço contínuo em melhorar a qualidade de nossos produtos e a adaptação às demandas de mercado.

    No gráfico abaixo, você verá a evolução do valor médio de venda por litro de vinho de 2007 a 2021. Os dados representam uma média anual, o que proporciona uma visão clara das tendências ao longo do tempo. 

    Ressaltamos que a nossa unidade de medida considera 1 kg de uva igual a 1 litro de vinho. Essa é uma aproximação comum na indústria e permite uma fácil interpretação e comparação dos dados.

    Analise os dados e observe o compromisso da nossa equipe em buscar os melhores resultados e a valorização constante dos nossos produtos. 

    Para quaisquer dúvidas ou esclarecimentos adicionais, não hesitem em nos contactar.
    """
    )
    line = px.line(df_resultado, x='anos', y='total').update_traces(mode='lines')    
    scatter = px.scatter(df_resultado, x='anos', y='total').update_traces(mode='markers', hovertemplate='Ano: %{x} <br>Valor: U$ %{y}')    
    fig = go.Figure(data=line.data + scatter.data)    
    fig.update_xaxes(tickangle=45)
    st.plotly_chart(fig)

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