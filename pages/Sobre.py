import streamlit as st
from PIL import Image

st.set_page_config(page_title="Sobre",page_icon=":information_source:")

image = Image.open("./src/img/download.jpg")
st.image(image)

st.write(
"""
## Projeto desenvolvido para o 1º tech challenge da Fiap da turma Dados

### Participantes:

Leonardo Fernandes de Moraes Alves

Luiz Antonio Simette de Mello Campos

Paulo Henrique Barbosa Ortiz de Souza



### Professor:

Edgard Joseph Kiriyama 

Matheus Pavani    


### Base dados:

Base dados principal: http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_01

Noticias: http://www.aviga.com.br/ 

Dataset complementar: https://dadosabertos.bcb.gov.br/dataset/dolar-americano-usd-todos-os-boletins-diarios
"""
)