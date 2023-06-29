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
<h1 style="text-align: center; color: #8A2BE2;">Análise Geral das Exportações</h1>

<p style="text-indent: 40px; font-size:18px;">Esta análise oferece uma visão abrangente das nossas exportações de vinho, detalhando a origem dos nossos produtos, o volume exportado e o faturamento gerado por cada país com o qual negociamos.</p>

<p style="text-indent: 40px; font-size:18px;">O objetivo deste conjunto de dados é permitir uma melhor compreensão da dinâmica do nosso comércio internacional, ajudando-nos a identificar tendências, pontos fortes e oportunidades de crescimento. Neste relatório, nosso foco é fornecer informações precisas e atualizadas que possam fundamentar decisões estratégicas para o futuro de nossa empresa.</p>

<p style="text-indent: 40px; font-size:18px;">Para a análise, utilizamos a equivalência de 1 kg = 1 litro para padronizar nossas métricas, permitindo uma comparação justa entre diferentes produtos e volumes.</p>

<p style="text-indent: 40px; font-size:18px;">Explore as informações valiosas a seguir e descubra como elas podem ser utilizadas para potencializar nosso crescimento e rentabilidade futura.</p>
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
                    <h2>Volume</h2>
                    <h4 style ="text-decoration: underline;">{total_volume_em_milhares:,.0f} Milhares</h4>
                </div>
                """, unsafe_allow_html=True)
    
with col3:
        st.markdown(f"""
                    <div style="border:2px solid #8A2BE2; padding:10px; text-align: center;">
                        <h2>Preço Médio</h2>
                        <h4 style ="text-decoration: underline;">U$ {df_filtrado_medio['Total'].mean():,.2f}</h4>
                    </div>
                    """, unsafe_allow_html=True)

st.markdown("""
<h2 style="text-align: center; color: #8A2BE2;">Detalhamento da Exportação por País</h2>

<p style="text-indent: 40px; font-size:18px;">A tabela a seguir fornece uma visão detalhada da exportação de vinho para cada país com o qual fizemos negócios. Nela, apresentamos o volume de venda no período de  15 anos e o faturamento correspondente a essas vendas.</p>
""", unsafe_allow_html=True)

df_total = df_total[['Origem','País','Volume KG', 'Valor (US$)']]
    
st.dataframe(df_total,hide_index=True,use_container_width=True) 