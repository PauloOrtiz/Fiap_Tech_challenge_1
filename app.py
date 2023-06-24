#Libs
import streamlit as st
from PIL import Image

#pages
from home import run as run_home
from geral import run as run_geral
from sobre import run as run_sobre

#Titulo de Página
image = Image.open("./src/img/download.jpg")
st.image(image)
st.title("Análise da Exportação de Vinhos Brasileiros")

# Sidebar com opções de seleção da página
st.sidebar.title('Menu')
page = st.sidebar.radio("Escolha uma Página", ["Home", "Geral", "Sobre"])

if page == "Home":
    run_home()
elif page == "Geral":
    run_geral()
elif page == "Sobre":
    run_sobre()