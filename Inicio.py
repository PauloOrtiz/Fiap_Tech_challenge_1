#Libs
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Main Page", page_icon=":house:")

#Titulo de Página
image = Image.open("./src/img/download.jpg")
st.image(image)

st.markdown("""
<h1 style = "text-align: center; color: #8A2BE2;">Análise das Exportações de Vinhos Brasileiros</h1>

<p style="text-indent: 40px;">Bem-vindos à análise de exportação de vinhos brasileiros. O Brasil tem uma rica tradição na produção de vinhos finos e, ao longo dos anos, tem exportado seus produtos para todo o mundo. Esta plataforma foi projetada para fornecer uma visão abrangente do volume e valor de nossas exportações, assim como as forças externas que as influenciam.</p>

<h2 style="color: #8A2BE2;">O que abordaremos :</h2>

<p style="text-indent: 20px;"><b>1. Volumetria da Exportação por Ano:</b> Uma análise da quantidade de vinhos exportados por ano para diferentes países, abrangendo o período de 2007 a 2021.</p>

<p style="text-indent: 20px;"><b>2. Preço Médio de Venda na Exportação:</b> Uma análise do preço médio de venda de nossos vinhos no mercado internacional.</p>

<p style="text-indent: 20px;"><b>3. Faturamento da Exportação por Ano:</b> Uma análise do faturamento anual de nossas exportações.</p>

<p style="text-indent: 20px;"><b>4. Evolução do Dólar:</b> Uma visão sobre como a flutuação da moeda influenciou nossas exportações durante o período em questão.</p>

<p style="text-indent: 20px;"><b>5. Principais Destinos de Exportação:</b> Uma análise de Pareto que mostra os principais países para os quais exportamos nossos vinhos.</p>

<p style="text-indent: 20px;"><b>6. Produção e Comercialização de Vinho:</b> Uma análise do volume de produção e comercialização de vinho no Brasil durante o período de 2007 a 2021.</p>

<p style="text-indent: 20px;"><b>7. Importação vs Exportação:</b> Uma análise comparativa entre os volumes de importação e exportação de vinho no Brasil.</p>

<h2 style="color: #8A2BE2;">Nosso público-alvo</h2>

<p style="text-indent: 40px;"> Estas análises são voltadas para investidores e outras partes interessadas que desejam compreender melhor a indústria de exportação de vinhos do Brasil e identificar oportunidades de investimento.

""",unsafe_allow_html=True )
