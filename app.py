#Libs
import streamlit as st
from PIL import Image

#pages
from home import run as run_home
from geral import run as run_geral

#Titulo de Página
image = Image.open("./src/img/download.jpg")
st.image(image)
st.title("Análise da Exportação de Vinhos Brasileiros")


# Defina variáveis para cada botão
button1 = st.sidebar.button('Inicio')
button2 = st.sidebar.button('Informações Gerais')

if button1:
    run_home()
elif button2:
    run_geral()