#Libs
import pandas as pd
import numpy as np

#libs gráficas
import plotly.express as px
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

    '''
    Este é um relatorio destinado ao investidores da Vinicula Fiap,
    onde apresentaremos os resultados dos ultimos 15 anos e as progessões
    para os proximos anos.  
    
    Começaremos apresentando a valor médio do litro de vendidos em cada ano: 
    
    '''
    df = pd.DataFrame(df_resultado)
    st.dataframe(df, use_container_width=True, hide_index= True)



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