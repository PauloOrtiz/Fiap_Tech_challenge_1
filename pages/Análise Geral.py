import pandas as pd
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Analise Geral", page_icon="📈")

df_resultado = pd.read_csv('./src/data/resultado.csv')
df_total_por_ano = pd.read_csv('./src/data/total_por_ano.csv')
df_volume_por_ano = pd.read_csv('./src/data/volume_por_ano.csv')
df_total = pd.read_csv('./src/data/total_final.csv') 

image = Image.open("./src/img/download.jpg")
st.image(image)

st.markdown("""
<h1 style="text-align: center; color: #8A2BE2;">Panorama Geral das Exportações de Vinhos Brasileiros</h1>

<p style="text-indent: 40px; font-size:18px;">Desde 2007, a indústria vitivinícola brasileira tem se transformado, evoluindo suas práticas e posicionamento no mercado global. O país, conhecido por sua diversidade de uvas e terras propícias, tem solidificado seu espaço no mercado internacional de vinhos. Esta análise é o começo de uma jornada exploratória, onde vamos desvendar o volume, a receita e a diversidade dos nossos parceiros comerciais no cenário global.</p>

<p style="text-indent: 40px; font-size:18px;">Cada número aqui apresentado representa uma história, um esforço coletivo de viticultores, vinicultores, trabalhadores e instituições brasileiras. Nosso objetivo é revelar essas histórias, identificar tendências e oportunidades, e fornecer uma base sólida para estratégias futuras. </p>

<p style="text-indent: 40px; font-size:18px;">Vamos começar nosso tour com um olhar rápido sobre três importantes indicadores de nossa exportação de vinhos: o faturamento total, o volume total e o preço médio de venda. Esses indicadores oferecem uma visão macro da nossa performance ao longo dos anos. Aprofundaremos esses e outros tópicos em análises subsequentes, então, consideramos esta uma excelente oportunidade para se familiarizar com eles.</p>
""", unsafe_allow_html=True)

# Definindo o widget no sidebar
anos_selecionados = st.sidebar.multiselect('Selecione os anos', df_total_por_ano['Anos'].unique(), default=df_total_por_ano['Anos'].unique())

# Filtrando os dados baseado nos anos selecionados
df_filtrado_total = df_total_por_ano[df_total_por_ano['Anos'].isin(anos_selecionados)]
df_filtrado_volume = df_volume_por_ano[df_volume_por_ano['Anos'].isin(anos_selecionados)]
df_filtrado_medio = df_resultado[df_resultado['Anos'].isin(anos_selecionados)] 

total_faturamento = df_filtrado_total['Total'].sum()
total_faturamento_em_milhoes = total_faturamento / 1_000_000

total_volume = df_filtrado_volume ['Total'].sum()
total_volume_em_milhares = total_volume / 1_000

# Criação das 3 colunas
col1, col2, col3 = st.columns(3)

with col1:
    
    st.markdown(f"""
                <div style="border:2px solid #8A2BE2; padding:10px;text-align: center;">
                    <h2>Faturamento</h2>
                    <h4 style ="text-decoration: underline;">U$ {total_faturamento_em_milhoes:.2f} Milhões</h4>
                </div>
                """, unsafe_allow_html=True)
    
with col2:
    st.markdown(f"""
                <div style="border:2px solid #8A2BE2; padding:10px;text-align: center;">
                    <h2>Volume Lts</h2>
                    <h4 style ="text-decoration: underline;">{total_volume_em_milhares:,.0f} Milhares</h4>
                </div>
                """, unsafe_allow_html=True)
    
with col3:
    st.markdown(f"""
                <div style="border:2px solid #8A2BE2; padding:10px; text-align: center;">
                    <h2>Preço Médio</h2>
                    <h4 style ="text-decoration: underline;">U$ {df_filtrado_medio['Total'].mean():,.2f} p/ Lt</h4>
                </div>
                """, unsafe_allow_html=True)

st.markdown("""
<h2 style="text-align: center; color: #8A2BE2;">Detalhamento da Exportação por País</h2>

<p style="text-indent: 40px; font-size:18px;">Agora que você já tem uma visão geral da nossa performance, vamos descer um nível e olhar mais de perto para cada parceiro comercial. A tabela a seguir apresenta um detalhamento das exportações de vinho para cada país com o qual fizemos negócios. Nela, você encontrará o volume e o valor das vendas realizadas ao longo do período de 15 anos. A diversidade desses dados reflete a riqueza e complexidade da indústria vitivinícola brasileira e serve como ponto de partida para análises futuras.</p>
""", unsafe_allow_html=True)

df_total = df_total[['Origem','País','Volume KG', 'Valor (US$)']]
    
st.dataframe(df_total,hide_index=True,use_container_width=True)
