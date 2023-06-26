
import pandas as pd
import plotly.graph_objects as go 
import plotly.express as px
from plotly.subplots import make_subplots
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Evolução", page_icon="📊")


df_resultado = pd.read_csv('./src/data/resultado.csv')
df_total_por_ano = pd.read_csv('./src/data/total_por_ano.csv')
df_volume_por_ano = pd.read_csv('./src/data/volume_por_ano.csv')


image = Image.open("./src/img/download.jpg")
st.image(image)


tab0, tab1, tab2= st.tabs(["Preço Médio", "Faturamento","Volumetria"])


with tab0:
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

with tab1:
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

with tab2:
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