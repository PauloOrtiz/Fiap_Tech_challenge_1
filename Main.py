#Libs
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Main Page", page_icon=":house:")

#Titulo de Página
image = Image.open("./src/img/download.jpg")
st.image(image)
st.title("Análise da Exportação de Vinhos Brasileiros")

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

