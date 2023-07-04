
import pandas as pd
import plotly.graph_objects as go 
import plotly.express as px
from plotly.subplots import make_subplots
import streamlit as st
from PIL import Image
from prophet import Prophet



st.set_page_config(page_title="Evolução", page_icon="📊")


df_resultado = pd.read_csv('./src/data/resultado.csv')
df_total_por_ano = pd.read_csv('./src/data/total_por_ano.csv')
df_volume_por_ano = pd.read_csv('./src/data/volume_por_ano.csv')
df_cotacao = pd.read_csv('./src/data/cotacao.csv', sep=";" , decimal=",")
df_boxplot_proj = pd.read_csv('./src/data/boxplot_projecao.csv')
df_valor2_agg = pd.read_csv('./src/data/base_100_exportacao.csv')
df_agg_boxplot_prophet = pd.read_csv('./src/data/previsao.csv')



image = Image.open("./src/img/download.jpg")
st.image(image)


tab0, tab1, tab2, tab3= st.tabs([ "Faturamento","Volumetria", "Preço Médio","Projeção"])


with tab0:
    
    st.markdown("""
        ## <div style="text-align: center; color: #8A2BE2;">Relatório de Faturamento de Exportação</div>

        <p style='text-indent: 40px;'> Nosso histórico de faturamento ilustra uma trajetória de crescimento e solidez que poucas empresas podem igualar. A seguir, você encontrará um gráfico que conta nossa história de sucesso nos últimos quinze anos, destacando nossos marcos e triunfos.</p>

        <p style='text-indent: 40px;'> Não podemos ignorar o pico significativo de vendas em 2013 - um ano que marcou nossa trajetória. Foi neste ano que realizamos a primeira exportação de vinho a granel para a Rússia, uma jogada estratégica que revolucionou nosso posicionamento no mercado internacional de vinhos.</p>

        <p style='text-indent: 40px;'> Em 2013, ao lado de nossos colegas associados à AVIGA, exportamos impressionantes 840 mil litros de vinho tinto de mesa para a Rússia. Este empreendimento significou 35 contêineres de vinho de qualidade premium, marcando nossa presença no cenário global.</p>

        <p style='text-indent: 40px;'> Este marco não foi apenas um testemunho de nossa capacidade de inovação e expansão, mas também ilustrou a força da colaboração e parceria. Este é o espírito que guia nossa empresa - a crença de que juntos, podemos conquistar novos patamares.</p>

        <p style='text-indent: 40px;'> O sucesso recente em 2021, onde arrecadamos quase U$ 10 milhões em vendas, demonstra o poder de nossa marca e a qualidade incomparável de nossos vinhos. Nossas estratégias de mercado provaram ser eficazes, e continuamos a crescer a um ritmo impressionante.</p>

        <p style='text-indent: 40px;'> Nossas conquistas até agora são apenas o começo. Continuaremos a explorar novas oportunidades e aprimorar nossa oferta. Agradecemos a todos os nossos parceiros e investidores pelo contínuo apoio e confiança em nossa visão.</p>
        """,unsafe_allow_html=True) 

    line2 = px.line(df_total_por_ano, x='Anos', y='Total').update_traces(mode='lines', line=dict(color='#8A2BE2'))
    scatter2 = px.scatter(df_total_por_ano, x='Anos', y='Total').update_traces(mode='markers', hovertemplate='Ano: %{x} <br>Valor: U$ %{y:,.2f}', marker=dict(color='purple'))    
    fig2 = go.Figure(data=line2.data + scatter2.data)    
    fig2.update_layout(
        title="Evolução do Faturamento Total (2007-2021)",
        xaxis_title="Anos",
        yaxis_title="Faturamento (em U$)",
        xaxis = dict(
            tickangle=45
        )
    )
    st.plotly_chart(fig2)
   

with tab1:
  
    st.markdown("""
        <h1 style = "text-align: center; color: #8A2BE2;">Relatório de Volumetria</h1>
        <p style="text-indent: 40px;">Nossos números falam por nós. O volume de nossas vendas ao longo dos anos é uma prova tangível de nossa resiliente presença de mercado e do crescente apelo de nossos produtos.</p>
        <p style="text-indent: 40px;">No gráfico a seguir, você verá uma montanha-russa de vendas. Em 2009, o trem chegou ao pico mais alto com mais de 25 milhões em vendas, uma conquista extraordinária que está gravada em nossa história. No entanto, o que vem depois desse pico é igualmente importante.</p>
        <p style="text-indent: 40px;">Os anos subsequentes testemunharam uma desaceleração, mas não diminuíram nosso espírito. Pelo contrário, nos adaptamos, persistimos e gradualmente revigoramos nossas vendas, demonstrando a robustez e adaptabilidade de nosso modelo de negócios.</p>
        <p style="text-indent: 40px;">Essa resiliência culminou em um retorno poderoso. Desde 2016, nossas vendas aumentaram consistentemente, ultrapassando 8 milhões em 2021. Esta é uma representação vívida de nossa força no mercado e do apelo duradouro de nossos produtos.</p>
        <p style="text-indent: 40px;">Estamos entusiasmados com o futuro. Cada número em nosso gráfico de vendas não é apenas um resultado, mas um testemunho do trabalho duro, da inovação contínua e da confiança inabalável que nossos clientes e parceiros depositam em nós. Estamos confiantes de que a curva ascendente continuará nos próximos anos.</p>
        <p style="text-indent: 40px;">Abaixo, você encontrará o gráfico de nossas vendas ao longo dos últimos 15 anos, um vislumbre visual de nossa jornada, nosso progresso e nosso potencial. Agradecemos seu apoio contínuo e confiança em nossa empresa.
    """,unsafe_allow_html=True )

    fig3 = go.Figure(layout=go.Layout(
            title=go.layout.Title(text="Evolução do Volume de Vendas (2007-2021)"),
            xaxis=dict(title='Anos'),
            yaxis=dict(title='Volumetria'),
            xaxis_tickangle=45
        ))    
    fig3.add_trace(go.Scatter(x=df_volume_por_ano['Anos'], 
                            y=df_volume_por_ano['Total'], 
                            mode='lines+markers',
                            name="Volume Anual",
                            hovertemplate='Ano: %{x} <br>Volume: %{y}',
                            line=dict(color='#8A2BE2')
                            ))

    st.plotly_chart(fig3)



    
with tab2:
    st.markdown("""
        <h1 style = "text-align: center; color: #8A2BE2;">Análise do Valor Médio de Venda por Litro de Vinho</h1>
        <p style="text-indent: 40px;">O valor médio de venda por litro é um indicador crucial que reflete a nossa estratégia de preços e a percepção do valor do nosso vinho pelos consumidores. É uma dança delicada entre a qualidade do vinho, as condições do mercado e a apreciação do cliente.</p>
        <p style="text-indent: 40px;">Como você verá no gráfico abaixo, o valor médio de venda por litro experimentou altos e baixos nos últimos 15 anos. Essas oscilações não são apenas um reflexo das flutuações do mercado, mas também uma narrativa da nossa jornada para balancear a qualidade do produto e a acessibilidade para os consumidores.</p>
        <p style="text-indent: 40px;">Observe, por exemplo, o pico em 2011 e 2014, quando o valor médio de venda por litro atingiu o seu ápice. Esses foram os anos em que investimos pesadamente na melhoria da qualidade e em iniciativas de branding, resultando em um aumento na percepção do valor do nosso vinho.</p>
        <p style="text-indent: 40px;">Em contraste, você também notará uma tendência de diminuição do valor médio de venda nos últimos anos. Isso não é um indicativo de uma queda na qualidade do nosso vinho. Ao contrário, é um reflexo de nossa estratégia consciente de tornar nossos vinhos mais acessíveis para um público mais amplo, ampliando assim nossa base de clientes.</p>
        <p style="text-indent: 40px;">Essa jornada de precificação reflete nosso compromisso com a melhoria contínua da qualidade do vinho e com a satisfação do cliente. Agora, convidamos você a dar uma olhada mais de perto na evolução do valor médio de venda por litro nos últimos 15 anos.
    """,unsafe_allow_html=True )
    
    fig = go.Figure(layout=go.Layout(
                title=go.layout.Title(text="Evolução do Valor Médio de Venda por Litro (2007-2021)"),
                xaxis=dict(title='Anos'),
                yaxis=dict(title='Valor Médio (em U$)'),
                xaxis_tickangle=45
            ))

    fig.add_trace(go.Scatter(x=df_resultado['Anos'], 
                            y=df_resultado['Total'], 
                            mode='lines+markers',
                            name="Valor Médio Anual",
                            hovertemplate='Ano: %{x} <br>Valor: U$ %{y}',
                            line=dict(color='#8A2BE2')
                            ))

    st.plotly_chart(fig)
    
with tab3:


    st.markdown("""
    <h1 style = "text-align: center; color: #8A2BE2;">Projeção temporal das exportação</h1>
    <p style="text-indent: 40px;">Esta analise foi contruida com objetivo de demonstrar a projeção de exportação dos países para os proximos meses, incialmente retirando os outlier para não prejudicar a séries temporal, em seguida serão demonstradas as principais variaveis que consideramos na projeção, com o objetivo de demonstrar quais são 
    """,unsafe_allow_html=True )

    fig3 = go.Figure()

    fig3.add_trace(go.Box(
        y=df_boxplot_proj['sumtOfExport'],
        x=df_boxplot_proj['País'],
        name='Boxplot',
        line=dict(color='#8A2BE2')
    ))

    fig3.update_layout(
        title='Identificação dos outlier dos top10 países exportadors',
        xaxis_title='Paises',
        yaxis_title='Valores'
    )

    st.plotly_chart(fig3)

    st.markdown("""
    <p style="text-indent: 40px;">Após retirar os registros outliers que estão fora do intervalo interquartil, identificamos uma tendência correlata entre o variação da cotação do dólar e o ticket médio do U$/Litro
    """,unsafe_allow_html=True )



    fig = px.scatter(df_cotacao, x='ticket_medio', y='cotacaoVenda', trendline='ols', labels={'ticket_medio': 'Ticket médio U$/Litro', 'cotacaoVenda': 'Cotação do Dólar'})
    # Personalize o gráfico
    fig.update_layout(
        title={
            'text': "Relação ticket médio e preço do dólar, últimos 15 anos",
            'x': 0.5,
            'y': 0.95,
            'xanchor': 'center',
            'yanchor': 'top'
        }
    )

    fig.update_xaxes(
        title_text="Ticket médio R$/Litro",
        showticklabels=True
    )

    fig.update_yaxes(
        title_text="Cotação do Dólar em Reais",
        showticklabels=True
    )

    fig.add_trace(go.Scatter(name='Dados de dispersão'))  # Adiciona um nome para o trace
    
    # Mostre o gráfico
    st.plotly_chart(fig)

    st.markdown("""
    <p style="text-indent: 40px;">Analisamos a participação no volume de litros exportados por país para proporcionalizar o volume da exportação na projeção
    """,unsafe_allow_html=True )


    # Criando o gráfico de colunas empilhadas
    fig_1 = go.Figure()


    for pais in df_valor2_agg['group'].unique():
        dados_pais = df_valor2_agg[df_valor2_agg['group'] == pais]
        fig_1.add_trace(go.Bar(x=dados_pais['anomes'], y=dados_pais['percent'], name =pais))



    # Personalizando o layout do gráfico
    fig_1.update_layout(
        title='Participação nas Vendas por País e Ano',
        xaxis_title='Ano e Mês da exportação',
        yaxis_title='Participação nas Vendas',
        barmode='stack'
    )

    # Exibindo o gráfico
    st.plotly_chart(fig_1)


        #Crie um dicionário de DataFrames, onde cada chave corresponda a um país e o valor seja um DataFrame filtrado por país:
    dfs_paises = {}
    for pais in df_agg_boxplot_prophet['country'].unique():
        dfs_paises[pais] = df_agg_boxplot_prophet[df_agg_boxplot_prophet['country'] == pais].drop('country', axis=1)
    #Crie um modelo Prophet para cada país e ajuste-o aos dados correspondentes:
    modelos = {}
    for pais, df_pais in dfs_paises.items():
        modelo = Prophet()
        modelo.fit(df_pais)
        modelos[pais] = modelo


    #Instancia e ajusta os dados ao modelo
    datas_futuras = pd.date_range(start='2022-01-01', periods=12, freq='MS')
    datas_futuras = pd.DataFrame({'ds': datas_futuras})
    #Faça a projeção das vendas para cada país usando os modelos Prophet correspondentes:
    previsoes_paises = {}
    for pais, modelo in modelos.items():
        previsao = modelo.predict(datas_futuras)
        previsoes_paises[pais] = previsao

    for pais, previsao in previsoes_paises.items():
        previsao.loc[previsao['yhat'] < 0, 'yhat'] = -previsao['yhat_lower']
        previsoes_paises[pais] = previsao

    fig4 = go.Figure()
    for pais, previsao in previsoes_paises.items():
        fig4.add_trace(go.Scatter(
            x=previsao['ds'],
            y=previsao['yhat'],
            mode='lines',
            name=pais
        ))
    fig4.update_layout(
        title='Projeção de Valor exporta por País',
        xaxis_title='Data',
        yaxis_title='Valor Exportado Previsto'
    )
    st.plotly_chart(fig4)


    st.markdown("""
    ## <div style="text-align: center; color: #8A2BE2;"> Análise dos Dados </div>
    <p style="text-indent: 40px;"> Avaliando o cenário de tendência do dólar e a evolução no volumes/litros exportados por cada país, os mercados do Haiti, Rússia e China são clientes em potêncial expansão.
    """, unsafe_allow_html=True)