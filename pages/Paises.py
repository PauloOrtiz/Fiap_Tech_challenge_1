import pandas as pd
import plotly.graph_objects as go 
import plotly.express as px
from plotly.subplots import make_subplots
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Evolução", page_icon="🌎")

df_porpo = pd.read_csv('./src/data/porpo.csv')
df_valores = pd.read_csv('./src/data/valores.csv')
df_volume = pd.read_csv('./src/data/volume.csv')

image = Image.open("./src/img/download.jpg")
st.image(image)


# Layout do aplicativo
tab0, tab1 = st.tabs(["Percentual","Paises"])




with tab0:

    st.markdown('''
    # <div style="text-align: centerç; color: #8A2BE2;"> Análise das Exportações </div>

    <p style="text-indent: 40px;"> O presente relatório fornece uma avaliação pormenorizada de nossas exportações ao longo dos últimos 15 anos. A análise é focada na contribuição percentual cumulativa de cada país para nossas exportações totais. Nossos insights são derivados de dados consolidados e apresentados em uma visualização gráfica que combina um gráfico de barras, indicando o valor total de exportações para cada país, com uma linha de percentual cumulativo que ressalta a contribuição progressiva para o total das exportações.

    ''', unsafe_allow_html=True)
    
    


    color1 = 'steelblue'
    color2 = 'red'
    line_size = 4

    df_porpo['perc_acum'] = df_porpo['perc_acum'] / 100
    df_porpo = df_porpo.sort_values('perc_acum', ascending=True)

    bar = go.Bar(
        x=df_porpo['group'],
        y=df_porpo['Total'],
        marker_color=['grey' if x <= 0.80 else 'orange' for x in df_porpo['perc_acum']],
        name='Valor em Milhões'
    )

    line = go.Scatter(
        x=df_porpo['group'],
        y=df_porpo['perc_acum'],
        mode='lines+markers',
        marker=dict(color=color2, size=line_size),
        yaxis='y2',
        name='Percentual Acumulado'
    )

    # Adicione "Others" ao final dos rótulos do eixo x


    layout = go.Layout(
        title="Analise de participação nas exportações por país (ultimos 15 anos)",
        xaxis=dict(
            title='País exportação',
            tickangle=45,
            tickmode='array',  # definir o modo de exibição dos ticks como array
            tickvals=df_porpo['group'],  # definir os valores dos ticks
           # ticktext=custom_labels  # definir os rótulos personalizados dos ticks
        ),
        yaxis=dict(title='Valor em Milhões', color=color1),
        yaxis2=dict(title='Percentual', overlaying='y', side='right', color=color2, tickformat=".0%"),
        legend=dict(x=0, y=1.3),  # mover a legenda acima do título
        margin=dict(t=130),  # aumentar o espaçamento entre o título e a legenda
        showlegend=True
    )

    fig = go.Figure(data=[bar, line], layout=layout)

    st.plotly_chart(fig)

    st.markdown('''
    ## <div style="text-align: center; color: #8A2BE2;"> Análise dos Dados </div>

    <p style="text-indent: 40px;"> O gráfico demonstra claramente que nossas exportações são altamente concentradas em poucos países.

    <p style="text-indent: 40px;"> Os primeiros países na lista - Paraguai, Rússia, Estados Unidos, Reino Unido , China e Países baixos - representam a maior parte do valor total das nossas exportações. Especificamente, o Paraguai e a Rússia sozinhos representam mais 55s% do valor total das nossas exportações. Esta concentração em um pequeno número de mercados apresenta riscos e oportunidades.

    <p style="text-indent: 40px;"> Por um lado, a dependência de poucos mercados pode nos tornar vulneráveis a mudanças econômicas ou políticas nesses países. Por exemplo, uma recessão ou mudança de política comercial no Paraguai ou na Rússia poderia ter um impacto significativo em nossas exportações.

    <p style="text-indent: 40px;"> Por outro lado, a concentração de nossas exportações nesses mercados também pode representar uma oportunidade. Há claramente uma demanda forte e estabelecida por nossos produtos nesses países, o que sugere que podemos ter oportunidades para expandir ainda mais nossa participação de mercado. Além disso, nossa experiência e relacionamento nestes mercados podem nos fornecer uma vantagem competitiva.

    <p style="text-indent: 40px;"> Os dados também mostram que, após o primeiro grupo de países, o valor das nossas exportações cai drasticamente. Muitos países têm um valor de exportação muito pequeno e estão agrupados na categoria 'Others'. Isso sugere que temos um grande número de mercados nos quais nossa presença é relativamente pequena.

    ...

    ### <div style="text-align: center; color: #8A2BE2;"> Recomendações </div>

    <div style="text-align: center";>Com base em nossa análise, sugerimos as seguintes ações estratégicas:</div>

    <p style="text-indent: 40px;">1. <b>Mitigar Riscos:</b> Devemos considerar a diversificação de nossos mercados de exportação para mitigar os riscos associados à dependência de exportações para o Paraguai e a Rússia.

    <p style="text-indent: 40px;">2. <b>Explorar Oportunidades:</b> Além disso, devemos buscar oportunidades para expandir ainda mais nossas vendas nos mercados onde já temos uma presença significativa.

    <p style="text-indent: 40px;">3. <b>Desenvolver Mercados Emergentes:</b> Os países classificados como 'Outros' em nossa análise podem ser considerados mercados emergentes potenciais. Apesar do valor das exportações para cada um desses países ser pequeno no momento, eles podem representar oportunidades substanciais para crescimento a longo prazo.

    ''', unsafe_allow_html=True)

with tab1:

    st.markdown("""
    # <div style="text-align: center; color: #8A2BE2;"> Análise de Faturamento e Volume por País </div>
    
    <p style="text-indent: 40px;"> Este relatório apresenta a evolução do faturamento e volume de vendas de produtos por país, utilizando dados coletados entre os anos de 2007 e 2021. A análise permite visualizar o desempenho econômico de cada país e identificar tendências e variações notáveis ao longo do tempo.
    
    """, unsafe_allow_html=True)

    def filtro_paises(df, paises):
        df_melt = df.melt(id_vars=['País'], value_vars=df.columns[1:-1], var_name='Ano', value_name='Valor')
        df_filtered = df_melt[df_melt['País'].isin(paises)]
        return df_filtered

    # Cria a lista de países com base no primeiro DataFrame, que supomos conter todos os países
    todos_paises = df_valores['País'].unique()
    filtrar_paises = st.sidebar.checkbox('Filtrar países', value=False, key='chave1')

    if filtrar_paises:
        paises_selecionados = st.sidebar.multiselect('Selecione os países:', todos_paises, default=todos_paises, key='chave2')
    else:
        paises_selecionados = todos_paises

    st.markdown('''
    ## <div style="text-align: center"> Evolução do Faturamento por País </div>
    ''', unsafe_allow_html=True)

    # Gráfico de Países para Valores
    df_valores = df_valores.iloc[:-1]
    df_filtered = filtro_paises(df_valores, paises_selecionados)
    fig = px.line(df_filtered, x='Ano', y='Valor', color='País')
    st.plotly_chart(fig)

    st.markdown('''
    ## <div style="text-align: center"> Evolução do Volume de Vendas por País </div>
    ''', unsafe_allow_html=True)

    # Gráfico de Países para Volume
    df_volume = df_volume.iloc[:-1]
    df_filtered = filtro_paises(df_volume, paises_selecionados)
    fig = px.line(df_filtered, x='Ano', y='Valor', color='País')
    st.plotly_chart(fig)

    st.markdown("""
    ## <div style="text-align: center; color: #8A2BE2;"> Análise dos Dados </div>
    
    <p style="text-indent: 40px;"> A análise dos dados revela variações significativas na atividade econômica entre os diferentes países e ao longo do tempo. Alguns países, como a Alemanha e a República Democrática, apresentam um volume de negócios expressivo, ultrapassando 2.7 milhões no período analisado. Em contrapartida, outros países, como Afeganistão e África do Sul, demonstram um volume de negócios consideravelmente menor.

    <p style="text-indent: 40px;"> Nota-se também que alguns países apresentaram um crescimento substancial em determinados anos. Um exemplo notável é a China, que apresentou um salto significativo em 2009, tendência que se manteve nos anos seguintes.

    <p style="text-indent: 40px;"> Essas observações enfatizam a importância do recurso de seleção interativa disponibilizado no gráfico, que permite aos usuários isolar países e anos específicos para uma análise mais detalhada. 

    <p style="text-indent: 40px;"> É importante destacar que as tendências e variações observadas podem refletir mudanças no contexto econômico global, regional ou nacional. Portanto, é fundamental interpretar esses dados considerando-se o cenário econômico mais amplo.
    
    """, unsafe_allow_html=True)