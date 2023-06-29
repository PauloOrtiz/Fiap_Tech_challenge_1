import streamlit as st
from PIL import Image

st.set_page_config(page_title="Sobre",page_icon=":information_source:")

image = Image.open("./src/img/download.jpg")
st.image(image)

st.markdown("""
    # <div style="text-align: center; color: #8A2BE2;"> Resumo </div>
    
    Este projeto, parte do 1º Tech Challenge da turma de Data Science da FIAP, foi uma oportunidade para melhorar nossas habilidades em análise de dados e colaboração em equipe. Agradecemos a todos que participaram deste desafio.

    # <div style="text-align: center; color: #8A2BE2;"> 1. Introdução </div>

    Este projeto foi concebido como parte do 1º Tech Challenge da turma de Data Science da FIAP, focando na análise abrangente das exportações de vinho. Através deste estudo, buscamos obter uma visão clara da origem dos nossos produtos, o volume exportado e o faturamento gerado por cada país com o qual negociamos. O objetivo é identificar tendências, pontos fortes e oportunidades de crescimento que possam informar decisões estratégicas para o futuro da nossa empresa.

    # <div style="text-align: center; color: #8A2BE2;"> 2. Metodologia </div>

    Utilizamos uma variedade de ferramentas e técnicas de ciência de dados para realizar esta análise. Os dados foram coletados a partir de várias fontes, incluindo VitiBrasil, AviGa e Banco Central do Brasil, e carregados para análise usando a biblioteca pandas do Python. A visualização dos dados foi realizada principalmente com as bibliotecas matplotlib e seaborn, e a aplicação web foi criada usando a biblioteca streamlit. Para padronizar nossas métricas, utilizamos a equivalência de 1 kg = 1 litro, permitindo uma comparação justa entre diferentes produtos e volumes.

    # <div style="text-align: center; color: #8A2BE2;"> 3. Resultados </div>

    Os resultados de nossa análise oferecem uma visão detalhada da dinâmica de nosso comércio internacional. [Incluir aqui os principais achados e insights, por exemplo, quais países são os principais compradores, quais produtos são os mais exportados, como as exportações mudaram ao longo do tempo, etc.

    # <div style="text-align: center; color: #8A2BE2;"> 4. Conclusão </div>

    Através deste projeto, fomos capazes de explorar e compreender de maneira mais profunda a dinâmica das exportações de vinho. Os insights obtidos não só nos permitem entender melhor a atual situação do nosso comércio internacional, mas também nos oferecem uma base sólida para tomar decisões estratégicas que possam impulsionar o crescimento e a rentabilidade futura da empresa. Acreditamos que a aplicação da ciência de dados na análise de negócios, como demonstrado neste projeto, é uma ferramenta valiosa para impulsionar a inovação e o sucesso em um mundo cada vez mais orientado por dados.

    # <div style="text-align: center; color: #8A2BE2;"> 5. Agradecimentos </div>

    Gostaríamos de agradecer aos nossos professores Edgard Joseph Kiriyama e Matheus Pavani por sua orientação e suporte, bem como aos nossos colegas de classe e a todos os envolvidos na organização deste desafio.

    # <div style="text-align: center; color: #8A2BE2;"> 6. Referências </div>

    A seguir, estão os recursos dos quais os dados foram coletados:

    - Base de dados principal: [VitiBrasil](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_01)
    - Notícias: [AviGa](http://www.aviga.com.br/)
    - Dataset complementar: [Banco Central do Brasil](https://dadosabertos.bcb.gov.br/dataset/dolar-americano-usd-todos-os-boletins-diarios)

    Expressamos nossa gratidão a todas estas fontes por disponibilizar esses dados publicamente.
""", unsafe_allow_html=True)