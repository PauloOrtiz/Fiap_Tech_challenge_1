import pandas as pd
import plotly.graph_objects as go 
import plotly.express as px
from plotly.subplots import make_subplots
import streamlit as st
from PIL import Image
import statsmodels.api as sm
from prophet import Prophet

st.set_page_config(page_title="Evolução", page_icon="🌎")

df_porpo = pd.read_csv('./src/data/porpo.csv')
df_valores = pd.read_csv('./src/data/valores.csv')
df_volume = pd.read_csv('./src/data/volume.csv')
df_cotacao = pd.read_csv('./src/data/cotacao.csv')
df_sigla= pd.read_csv('./src/data/sigla_venda_total.csv')
df_boxplot_proj = pd.read_csv('./src/data/boxplot_projecao.csv')
df_agg_boxplot_prophet = pd.read_csv('./src/data/previsao.csv')
distribution = pd.read_csv('./src/data/base100_continente.csv')
df_agg_grupo = pd.read_csv('./src/data/valorlitro_dolr.csv')
df_final = pd.read_csv('./src/data/ticket_medio_continente.csv')
df_agg2_max_ticket = pd.read_csv('./src/data/hist_ticket_medio_2021.csv', sep=";", encoding='latin-1')

distribution = distribution.set_index("Ano")

image = Image.open("./src/img/download.jpg")
st.image(image)



# Layout do aplicativo
tab0, tab1, tab2 = st.tabs(["Percentual","Paises","Dados Econômicos"])

with tab0:

    st.markdown('''

    # <div style="text-align: center; color: #8A2BE2;"> Análise das Exportações </div>

    <p style="text-indent: 40px;"> O presente relatório fornece uma avaliação pormenorizada de nossas exportações ao longo dos últimos 15 anos. A análise é focada na contribuição percentual cumulativa de cada país para nossas exportações totais. Nossos insights são derivados de dados consolidados e apresentados em uma visualização gráfica que combina um gráfico de barras, indicando o valor total de exportações para cada país, com uma linha de percentual cumulativo que ressalta a contribuição progressiva para o total das exportações.

    ''', unsafe_allow_html=True)

    st.markdown('''
    # <div style="text-align: center; color: #8A2BE2;"> Nossas exportações de vinho pelo mundo!!! </div>

    <p style="text-indent: 40px;">            Mapa de calor do valor das exportações somadas nos últimos 15 por país

    ''', unsafe_allow_html=True)
    
    lista = df_sigla.values.tolist()
    
    fig = go.Figure(
        data=go.Choropleth(
            locations=[item[0] for item in lista],
            z=[item[1] for item in lista],
            colorscale='Viridis',
            autocolorscale=False,
            text=[f'{item[0]}: {item[1]}' for item in lista],
            marker_line_color='white',
            colorbar_title='Valor',
            
        )
    )

    #fig.update_layout(
    #    title_text='Mapa de calor do Valor exportados por País'

    #)

    st.plotly_chart(fig)

    st.write('''

    Este relatório apresenta uma análise de nossas exportações nos últimos 15 anos, especificamente, destacando a participação percentual acumulada de cada país em nossas exportações. Nossa análise é baseada em dados que foram agregados e apresentados em uma visualização gráfica, combinando um gráfico de barras que mostra o valor total das exportações para cada país e uma linha de percentual acumulado que indica a contribuição progressiva para o total de exportações.
    
    ''')


    color1 = 'purple'
    color2 = 'red'
    color3 = '#8A2BE2'
    line_size = 4

    df_porpo['perc_acum'] = df_porpo['perc_acum'] / 100
    df_porpo = df_porpo.sort_values('perc_acum', ascending=True)

    bar = go.Bar(
        x=df_porpo['group'],
        y=df_porpo['Total'],
        marker_color=[color3 if x <= 0.80 else color1 for x in df_porpo['perc_acum']],
        name='Valor em Milhões',
        
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
        title="Analise de Pareto da participação nas exportações por país (ultimos 15 anos)",
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

    <p style="text-indent: 41px;"> O gráfico demonstra claramente que nossas exportações são altamente concentradas em poucos países.

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

with tab2:

    
    
    st.markdown("""
    <h1 style = "text-align: center; color: #8A2BE2;">Análise de evolução das exportações</h1>
    <p style="text-indent: 40px;">Esta analise foi construida com o objetivo de identificar os melhores paises para exportar , observado a rentabilidade como principal alavanca, identificamos que a América do Sul desde 2016 se tornou o continente mais representativo de exportação chegando a 85% do volume litro exportado porém o ticket médio do valor por litro exportado é menor do que outros cotinentês e impactado pela variação do dolár
    """,unsafe_allow_html=True )

    # Converter a distribuição em uma lista de dicionários
    data = []
    for column in distribution.columns:
        data.append(go.Bar(
        x=distribution.index,
        y=distribution[column],
        name=column
    ))

    # Criar o layout do gráfico
    layout = go.Layout(
    title='Distribuição da América do Sul nas exportações (base 100)',
    xaxis_title='Ano e Mês de exportação',
    yaxis_title='% de participação nas exportações',
    barmode='stack'
    )

    # Criar a figura do gráfico
    fig3 = go.Figure(data=data, layout=layout)

    st.plotly_chart(fig3)


    # Gerar o gráfico de barras
    fig4 = px.bar(df_final, x='anomes', y=['ticket_medio'],barmode='group',color="Continente",
        #title='Comparação ticket médio por litro por Continente',
            labels={'value': 'Valor em U$' , "anomes" : "Ano e Mês de exportação"},title='Ticket médio do valor por litro exportado em cada continente')

    # Exibir o gráfico

    st.plotly_chart(fig4)


    # Criar as linhas do gráfico
    fig5 = go.Figure()


    # Criar o gráfico de linha
    for continente2 in df_agg_grupo['Continente'].unique():
        df_continente2 = df_agg_grupo[df_agg_grupo['Continente'] == continente2]
        fig5.add_trace(go.Scatter(x=df_continente2['anomes'], y=df_continente2['ticket_medio'], mode='lines', name=continente2))

    # Personalizar o layout do gráfico
    fig5.update_layout(
    title='Variação do Ticket Médio Versus evolução da cotação do Dolar',
    xaxis_title='Mês/Ano Exportação',
    yaxis_title='Valor monetário em U$'
    )

    # Exibir o gráfico
    st.plotly_chart(fig5)


    # Criando o histograma

    fig6 = go.Figure(data=[go.Bar(x=df_agg2_max_ticket['País'], y=df_agg2_max_ticket['ticket_medio'])])

    # Personalizando o layout do gráfico
    fig6.update_layout(
    title='Histograma de ticket médio U$/Litro em 2021',
    xaxis_title='País',
    yaxis_title='Valor do ticket médio em U$'
    )

    # Exibindo o gráfico
    st.plotly_chart(fig6)
    st.markdown("""
    <h1 style = "text-align: center; color: #8A2BE2;">Análise do mercado</h1>
    <p style="text-indent: 40px;">Com o aumento da cotação do dólar e a alto participação da américa do sul nas exportações o ticket médio tem diminuido Uma opção de aumentar/potencializar a rentalibilidade é diversificar para outros mercados a exportação de vinhos, mercados interessantes seriam a Nova Zelândia, Emirados Arabes e Portugual por exemplo têm respectivamente o maior ticket médio U$/Litro de 2021.

    """,unsafe_allow_html=True )
