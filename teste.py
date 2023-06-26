import pandas as pd
import plotly.graph_objects as go 
import plotly.express as px
from plotly.subplots import make_subplots
import streamlit as st
from PIL import Image


st.set_page_config(page_title="Analise Geral", page_icon="📈")

#Lendo a base de dados e tratanto a base de dados
df_resultado = pd.read_csv('./src/data/resultado.csv')
df_total_por_ano = pd.read_csv('./src/data/total_por_ano.csv')
df_volume_por_ano = pd.read_csv('./src/data/volume_por_ano.csv')
df_total = pd.read_csv('./src/data/total_final.csv')    
df_porpo = pd.read_csv('./src/data/porpo.csv')
df_valores = pd.read_csv('./src/data/valores.csv')
df_volume = pd.read_csv('./src/data/volume.csv')

image = Image.open("./src/img/download.jpg")
st.image(image)


# Layout do aplicativo
tab0, tab1, tab2, tab3, tab4, tab5= st.tabs(["Dados Gerais", "Preço Médio", "Faturamento","Volumetria","Percentual","Paises"])



with tab0:
    st.write("""
    ## Análise de Comércio - Últimos 15 anos

    Análise detalhada do comércio dos últimos 15 anos. Este relatório visa oferecer uma visão abrangente das nossas transações, ilustrando a origem dos nossos produtos, o volume negociado e o valor total para cada país com o qual fizemos negócios.

    Este conjunto de dados nos permitirá entender melhor a dinâmica do nosso comércio internacional, identificando tendências, pontos fortes e áreas de potencial crescimento. Nesta análise, focamos em fornecer informações precisas e atualizadas que podem nos ajudar a tomar decisões estratégicas e informadas para o futuro da nossa empresa.

    Vale ressaltar que, para fins desta análise, adotamos a equivalência de que 1 kg é igual a 1 litro. Isso é importante para padronizar nossas métricas e proporcionar uma comparação justa entre diferentes produtos e volumes.

    Vamos explorar juntos essas informações valiosas e discutir como elas podem ser utilizadas para potencializar nosso crescimento e rentabilidade futura.
    """)
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
                        <h4 style ="text-decoration: underline;">U$ {df_filtrado_medio['Total'].sum():,.2f}</h4>
                    </div>""", unsafe_allow_html=True)
        
    st.markdown("""
    

    
    """)

    st.dataframe(df_total,hide_index=True,use_container_width=True) 
    
with tab1:
    st.write(
    """
    
    ## Análise do Valor Médio de Venda por Litro de Vinho ao longo de 15 Anos

    Os resultados obtidos ao longo dos últimos 15 anos na venda de nosso vinho. Nesse período, observamos uma notável dinâmica no valor médio de venda por litro, o que demonstra o esforço contínuo em melhorar a qualidade de nossos produtos e a adaptação às demandas de mercado.

    No gráfico abaixo, você verá a evolução do valor médio de venda por litro de vinho de 2007 a 2021. Os dados representam uma média anual, o que proporciona uma visão clara das tendências ao longo do tempo. 

    Ressaltamos que a nossa unidade de medida considera 1 kg de uva igual a 1 litro de vinho. Essa é uma aproximação comum na indústria e permite uma fácil interpretação e comparação dos dados.

    Analise os dados e observe o compromisso da nossa equipe em buscar os melhores resultados e a valorização constante dos nossos produtos. 

    Para quaisquer dúvidas ou esclarecimentos adicionais, não hesitem em nos contactar.
    """
    )
    line = px.line(df_resultado, x='Anos', y='Total').update_traces(mode='lines')    
    scatter = px.scatter(df_resultado, x='Anos', y='Total').update_traces(mode='markers', hovertemplate='Ano: %{x} <br>Valor: U$ %{y}')    
    fig = go.Figure(data=line.data + scatter.data)    
    fig.update_layout(
        xaxis_title="Anos",
        yaxis_title="Valor Médio (em U$)",
        xaxis = dict(
            tickangle=45
        )
    )

    st.plotly_chart(fig)

with tab2:
    st.markdown('''

    ## Relatório de Vendas dos Últimos 15 Anos

    A evolução do faturamento total de vendas da nossa empresa ao longo dos últimos quinze anos. Como verão no gráfico a seguir, nossos esforços e investimentos contínuos nos posicionaram para um crescimento sustentável, culminando em uma receita expressiva em 2021.

    No gráfico, é importante notar o pico significativo de vendas em 2013. Isso se deve ao marco histórico em nossa história de negócios - a primeira exportação de vinho a granel para a Rússia, um empreendimento liderado pela Associação dos Vinicultores de Garibaldi (AVIGA), da qual fazemos parte. Este feito não só elevou o nosso perfil no mercado internacional de vinhos, mas também abriu portas para novas oportunidades de negócios.

    Naquele ano, juntamente com outras empresas associadas à AVIGA, exportamos um total de 840 mil litros de vinho tinto de mesa para o mercado russo, equivalente a 35 contêineres. Este acontecimento histórico foi o resultado de anos de trabalho árduo, qualidade do produto e articulação estratégica.

    Esta iniciativa pioneira de exportação para a Rússia é um testemunho do nosso compromisso com a inovação e a busca de novos mercados. É também um exemplo de como a colaboração e a parceria podem gerar resultados expressivos.

    Aproveitamos também para destacar o nosso desempenho recente em 2021, onde atingimos quase U$ 10 milhões em vendas. Este crescimento robusto reflete a força contínua da nossa marca e a qualidade dos nossos vinhos, além do sucesso das nossas estratégias de mercado.

    Para o futuro, continuaremos a buscar novas oportunidades e a melhorar nossos produtos e serviços. Agradecemos a todos pelo seu apoio contínuo e confiança em nossa empresa.
    ''')

    

    line2 = px.line(df_total_por_ano, x='Anos', y='Total').update_traces(mode='lines')    
    scatter2 = px.scatter(df_total_por_ano, x='Anos', y='Total').update_traces(mode='markers', hovertemplate='Ano: %{x} <br>Valor: U$ %{y:,.2f}')    
    fig2 = go.Figure(data=line2.data + scatter2.data)    
    fig2.update_layout(
        xaxis_title="Anos",
        yaxis_title="Faturamento (em U$)",
        xaxis = dict(
            tickangle=45
        )
    )
    st.plotly_chart(fig2)

with tab3:
    st.markdown('''
    ## Relatório de Volumetria dos Últimos 15 Anos

    O relatório de vendas dos últimos 15 anos. As informações aqui fornecidas oferecem uma visão clara da evolução das nossas vendas, destacando os pontos altos e baixos deste período.

    Observe, a partir da demostração de dados, que nossas vendas passaram por períodos de pico, como em 2009, onde alcançamos a incrível marca de mais de 25 milhões, seguido por uma desaceleração nos anos seguintes. Contudo, a resiliência e capacidade de adaptação do nosso negócio permitiram uma recuperação consistente ao longo dos anos. 

    A tendência de crescimento que observamos desde 2016, culminando em mais de 8 milhões em vendas em 2021, reforça a força da nossa empresa no mercado. Esses resultados são reflexo do nosso comprometimento com a qualidade e inovação constante dos nossos produtos e serviços.

    Estamos animados com o futuro e confiantes de que continuaremos a ver essa tendência ascendente nos próximos anos. Agradecemos seu apoio contínuo e confiança em nossa empresa.

    Agora, apresentamos a vocês o gráfico de nossas vendas ao longo desses 15 anos para um olhar mais detalhado sobre a evolução do nosso desempenho.
    ''')
    line3 = px.line(df_volume_por_ano, x='Anos', y='Total').update_traces(mode='lines')    
    scatter3 = px.scatter(df_volume_por_ano, x='Anos', y='Total').update_traces(mode='markers', hovertemplate='Ano: %{x} <br>Volume %{y}')    
    fig3 = go.Figure(data=line3.data + scatter3.data)    
    fig3.update_layout(
    xaxis_title="Anos",
    yaxis_title="Volumetria",
    xaxis = dict(
        tickangle=45
        )
    )
    st.plotly_chart(fig3) 

with tab4:

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

with tab5:

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
