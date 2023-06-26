import pandas as pd
import plotly.graph_objects as go 
import plotly.express as px
from plotly.subplots import make_subplots
import streamlit as st
from PIL import Image


df_porpo = pd.read_csv('./src/data/porpo.csv')
df_valores = pd.read_csv('./src/data/valores.csv')
df_volume = pd.read_csv('./src/data/volume.csv')

image = Image.open("./src/img/download.jpg")
st.image(image)


# Layout do aplicativo
tab0, tab1 = st.tabs(["Percentual","Paises"])




with tab0:

    st.write('''
    ## Introdução

    Este relatório apresenta uma análise de nossas exportações nos últimos 15 anos, especificamente, destacando a participação percentual acumulada de cada país em nossas exportações. Nossa análise é baseada em dados que foram agregados e apresentados em uma visualização gráfica, combinando um gráfico de barras que mostra o valor total das exportações para cada país e uma linha de percentual acumulado que indica a contribuição progressiva para o total de exportações.
    
    ''')
    
    color1 = 'steelblue'
    color2 = 'red'
    line_size = 4

    df_porpo['perc_acum'] = df_porpo['perc_acum'] / 100
    bar = go.Bar(x=df_porpo['group'], 
                y=df_porpo['Total'], 
                marker_color=['grey' if x < 0.83 else 'orange' for x in df_porpo['perc_acum']],
                name='Valor em Milhões')
    line = go.Scatter(x=df_porpo['group'], 
                    y=df_porpo['perc_acum'], 
                    mode='lines+markers',
                    marker=dict(color=color2, size=line_size),
                    yaxis='y2',
                    name='Percentual Acumulado')
    layout = go.Layout(title="Analise de participação nas exportações por país (ultimos 15 anos)", 
                    xaxis=dict(title='País exportação',tickangle=45),
                    yaxis=dict(title='Valor em Milhões', color=color1),
                    yaxis2=dict(title='Percentual', overlaying='y', side='right', color=color2, tickformat=".0%"),
                    legend=dict(x=1.2, y=1),  # mover a legenda para o lado direito
                    showlegend=True)
    fig = go.Figure(data=[bar, line], layout=layout)

    st.plotly_chart(fig)

    st.write("""
    
    ## Análise dos Dados

    O gráfico demonstra claramente que nossas exportações são altamente concentradas em poucos países.

    Os primeiros países na lista - Paraguai, Rússia, Estados Unidos, Reino Unido e China - representam a maior parte do valor total das nossas exportações. Especificamente, o Paraguai e a Rússia sozinhos representam mais de 77% do valor total das nossas exportações. Esta concentração em um pequeno número de mercados apresenta riscos e oportunidades.

    Por um lado, a dependência de poucos mercados pode nos tornar vulneráveis a mudanças econômicas ou políticas nesses países. Por exemplo, uma recessão ou mudança de política comercial no Paraguai ou na Rússia poderia ter um impacto significativo em nossas exportações.

    Por outro lado, a concentração de nossas exportações nesses mercados também pode representar uma oportunidade. Há claramente uma demanda forte e estabelecida por nossos produtos nesses países, o que sugere que podemos ter oportunidades para expandir ainda mais nossa participação de mercado. Além disso, nossa experiência e relacionamento nestes mercados podem nos fornecer uma vantagem competitiva.

    Os dados também mostram que, após o primeiro grupo de países, o valor das nossas exportações cai drasticamente. Muitos países têm um valor de exportação muito pequeno e estão agrupados na categoria 'Others'. Isso sugere que temos um grande número de mercados nos quais nossa presença é relativamente pequena.

    """) 
                    
    st.write("""
    ## Análise

    ### Recomendações

    Com base na análise dos dados, eu recomendaria as seguintes ações estratégicas:

    ### Mitigar Riscos: 
    
    Devemos buscar maneiras de mitigar o risco associado à nossa dependência das exportações para o Paraguai e a Rússia. Isso pode incluir a diversificação de nossos mercados de exportação, desenvolvendo relações comerciais com um maior número de países.

    ### Explorar Oportunidades: 
    
    Também devemos explorar oportunidades de expandir ainda mais nossas vendas nos mercados onde já temos uma presença forte. Isso pode incluir a identificação de novas oportunidades de negócios, a expansão de nossas ofertas de produtos ou a formação de parcerias estratégicas.

    ### Desenvolver mercados emergentes: 
    
    Finalmente, devemos olhar para a longa lista de países em 'Others' como mercados emergentes potenciais. Embora o valor das exportações para cada um desses países possa ser pequeno no momento, eles podem representar oportunidades significativas de crescimento a longo prazo.

    """)

with tab1:

    st.title('Análise de Faturamento e Volume por País')

    st.write("""
    Este relatório mostra a evolução do faturamento e volume de vendas de produtos por país, a partir de dados coletados entre os anos de 2007 e 2021.
    """)

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

    # Gráfico de Países para Valores
    df_valores = df_valores.iloc[:-1]
    df_filtered = filtro_paises(df_valores, paises_selecionados)
    fig = px.line(df_filtered, x='Ano', y='Valor', color='País')
    st.plotly_chart(fig)

    # Gráfico de Países para Volume
    df_volume = df_volume.iloc[:-1]
    df_filtered = filtro_paises(df_volume, paises_selecionados)
    fig = px.line(df_filtered, x='Ano', y='Valor', color='País')
    st.plotly_chart(fig)

    st.write("""
    ## Análise

    Ao examinar o conjunto de dados, é possível ver que a atividade econômica varia muito de país para país e de ano para ano. Alguns países, como a Alemanha, República Democrática, por exemplo, mostram uma atividade econômica significativa, com um total de faturamento/volume de mais de 2.7 milhões no período analisado. Outros países, como Afeganistão e África do Sul, mostram um volume de negócios muito menor.

    Vale destacar também que alguns países tiveram um aumento substancial em seu volume de negócios em anos específicos. A China, por exemplo, teve um grande salto em 2009, e essa tendência continuou nos anos subsequentes.

    Essas observações ressaltam a utilidade de poder selecionar países e anos específicos no gráfico interativo. Isso permite que os usuários identifiquem tendências e padrões que podem não ser imediatamente óbvios ao examinar o conjunto de dados como um todo.

    Por último, vale ressaltar que o conjunto de dados abrange um período de tempo significativo, e portanto as tendências observadas podem refletir mudanças nas circunstâncias econômicas globais, regionais ou nacionais. Isso sublinha a importância de interpretar os dados à luz do contexto mais amplo.    
    """)
