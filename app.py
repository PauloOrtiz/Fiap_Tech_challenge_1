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



#Titulo de Página
image = Image.open("./src/img/download.jpg")
st.image(image)
st.title('Estudo sobre exportação de vinhos entre 2007 a 2021')

# Layout do aplicativo
tab0, tab1, tab2, tab3= st.tabs(["Inicio","Dados Gerais", "Paises", "Sobre"])

with tab0:

    # Título da apresentação
    st.title("Relatório de Exportação de Vinho")

    # Introdução
    st.markdown("Este relatório tem como objetivo fornecer informações sobre a exportação de vinho nos últimos 15 anos, \
                visando auxiliar investidores interessados no setor vitivinícola brasileiro.")

    # Breve visão geral do setor
    st.header("Visão Geral do Setor")
    st.markdown("O setor vitivinícola brasileiro tem apresentado um crescimento significativo nas exportações de vinho. \
                A seguir, apresentamos alguns destaques:")

    # Estatísticas rápidas
    st.subheader("Estatísticas Rápidas")
    st.markdown("- O Brasil é um importante exportador de vinhos, com destaque para sua produção de vinhos finos.")
    st.markdown("- Os principais destinos de exportação incluem países como Estados Unidos, Reino Unido e China.")
    st.markdown("- O setor tem experimentado um crescimento anual médio de X% nos últimos 15 anos.")

    # Gráfico de linha com tendência de exportação ao longo do tempo
    st.subheader("Tendência de Exportação de Vinho ao Longo do Tempo")
    # Insira aqui o código para criar um gráfico de linha com a tendência de exportação de vinho ao longo dos anos

    # Gráfico de barras com principais destinos de exportação
    st.subheader("Principais Destinos de Exportação de Vinho")
    # Insira aqui o código para criar um gráfico de barras com os principais destinos de exportação de vinho

    # Conclusão e chamada para ação
    st.markdown("Com base nessas informações iniciais, é possível observar o potencial de investimento no setor vitivinícola \
                brasileiro. Recomenda-se uma análise mais detalhada para identificar oportunidades específicas de investimento.")

    # Seção para análise mais detalhada e recomendações
    st.header("Análise Detalhada e Recomendações")
    # Insira aqui a análise detalhada dos dados e as recomendações específicas para os investidores

    # Nota de rodapé
    st.markdown("*Dados fornecidos pelo Vitibrasil - Embrapa Uva e Vinho")



with tab1:

    '''
    ## Pagina2
    
    
    
    '''



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