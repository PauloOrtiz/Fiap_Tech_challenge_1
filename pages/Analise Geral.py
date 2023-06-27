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
## Análise Geral

Este relatório visa oferecer uma visão abrangente das nossas transações, ilustrando a origem dos nossos produtos, o volume negociado e o valor total para cada país com o qual fizemos negócios.

Este conjunto de dados nos permitirá entender melhor a dinâmica do nosso comércio internacional, identificando tendências, pontos fortes e áreas de potencial crescimento. Nesta análise, focamos em fornecer informações precisas e atualizadas que podem nos ajudar a tomar decisões estratégicas e informadas para o futuro da nossa empresa.

Vale ressaltar que, para fins desta análise, adotamos a equivalência de que 1 kg é igual a 1 litro. Isso é importante para padronizar nossas métricas e proporcionar uma comparação justa entre diferentes produtos e volumes.

Vamos explorar juntos essas informações valiosas e discutir como elas podem ser utilizadas para potencializar nosso crescimento e rentabilidade futura.
""", unsafe_allow_html=True)
# Definindo o widget no sidebar
anos_selecionados = st.sidebar.multiselect('Selecione os anos', df_total_por_ano['Anos'].unique(), default=df_total_por_ano['Anos'].unique())

# Filtrando os dados baseado nos anos selecionados
df_filtrado_total = df_total_por_ano[df_total_por_ano['Anos'].isin(anos_selecionados)]
df_filtrado_volume = df_volume_por_ano[df_volume_por_ano['Anos'].isin(anos_selecionados)]
df_filtrado_medio = df_resultado[df_resultado['Anos'].isin(anos_selecionados)]  # corrigido aqui

# Criação das 3 colunas
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
                <div style="border:2px solid black; padding:10px;text-align: center;">
                    <h2>Faturamento</h2>
                    <h4 style ="text-decoration: underline;">U$ {df_filtrado_total['Total'].sum():,.2f}</h4>
                </div>
                """, unsafe_allow_html=True)
    
with col2:
    st.markdown(f"""
                <div style="border:2px solid black; padding:10px;text-align: center;">
                    <h2>Volume</h2>
                    <h4 style ="text-decoration: underline;">{df_filtrado_volume['Total'].sum():,.0f}</h4>
                </div>
                """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
                <div style="border:2px solid black; padding:10px; text-align: center;">
                    <h2>Preço Médio</h2>
                    <h4 style ="text-decoration: underline;">U$ {df_filtrado_medio['Total'].mean():,.2f}</h4>
                </div>""", unsafe_allow_html=True)
    
st.markdown("""



""")

st.dataframe(df_total,hide_index=True,use_container_width=True) 