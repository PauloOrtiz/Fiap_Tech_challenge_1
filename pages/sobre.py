import streamlit as st
from PIL import Image

st.set_page_config(page_title="Sobre")

image = Image.open("./src/img/download.jpg")
st.image(image)

st.write(
"""
## Projeto desenvolvido para o 1º tech challenge da Fiap da turma Dados

### Participantes:

Luiz Antonio Simette de Mello Campos

Leonardo Fernandes de Moraes Alves

Paulo Henrique Barbosa Ortiz



### Professor:

Edgard Joseph Kiriyama 

Matheus Pavani    


### Base dados:

Base dados principal: http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_01

Noticias: http://www.aviga.com.br/ 

Dataset complementar: https://www.kaggle.com/search
"""
)