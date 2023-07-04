#Libs
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Main Page", page_icon=":house:")

#Titulo de Página
image = Image.open("./src/img/download.jpg")
st.image(image)

st.markdown("""
<h1 style = "text-align: center; color: #8A2BE2;">Desvendando o Universo das Exportações de Vinhos Brasileiros 🍇</h1>

<p style="text-indent: 40px;">Convidamos você a embarcar conosco nesta viagem de descoberta e análise do próspero setor de exportação de vinhos do Brasil. Ao longo dos anos, os vinhos finos do Brasil têm encontrado seu caminho para mesas de todo o mundo, contando uma história de dedicação, terroir e paixão em cada garrafa. Nossa plataforma traz à luz as histórias ocultas por trás dos números, fornecendo uma visão abrangente do volume e valor das nossas exportações, bem como das forças externas que as moldam.</p>

<h2 style="color: #8A2BE2;">Explorando nosso Conteúdo :</h2>

<p style="text-indent: 40px;">Construímos uma jornada de análise que atravessa várias dimensões do setor de exportação de vinhos, permitindo uma visão holística que possa informar decisões estratégicas e fornecer insights valiosos para várias partes interessadas.</p>

<p style="text-indent: 20px;">Nossa jornada começa com a página de <b>Análise Geral</b>, oferecendo uma visão contextualizada do setor de exportação de vinhos no Brasil e apresentando algumas das principais métricas a serem exploradas ao longo das demais páginas. Deste ponto, você será capaz de navegar por um conjunto de tópicos abrangentes e detalhados, tais como:</p>

<p style="text-indent: 20px;"><b>1. Volumetria da Exportação por Ano</b> - <i>Analisamos as tendências na quantidade de vinhos exportados por ano para diferentes países, cobrindo o período de 2007 a 2021.</i></p>

<p style="text-indent: 20px;"><b>2. Preço Médio de Venda na Exportação:</b> Uma análise do preço médio de venda de nossos vinhos no mercado internacional.</p>

<p style="text-indent: 20px;"><b>3. Faturamento da Exportação por Ano:</b> Uma análise do faturamento anual de nossas exportações.</p>

<p style="text-indent: 20px;"><b>4. Evolução do Dólar:</b> Uma visão sobre como a flutuação da moeda influenciou nossas exportações durante o período em questão.</p>

<p style="text-indent: 20px;"><b>5. Principais Destinos de Exportação:</b> Uma análise de Pareto que mostra os principais países para os quais exportamos nossos vinhos.</p>

<p style="text-indent: 20px;"><b>6. Importação vs Exportação:</b> Uma análise comparativa entre os volumes de importação e exportação de vinho no Brasil.</p>

<h2 style="color: #8A2BE2;">Construído para Você</h2>

<p style="text-indent: 40px;">Nosso relatório é dedicado a investidores, entusiastas do vinho, profissionais do setor e todos aqueles que desejam compreender melhor a indústria de exportação de vinhos do Brasil. Nós organizamos nossas análises de uma maneira que facilita a navegação, oferecendo uma visão intuitiva e profunda das complexidades do setor de exportação de vinhos brasileiros. Convidamos você a explorar, descobrir e desvendar os segredos que nossos dados têm para oferecer.</p>
""",unsafe_allow_html=True )
