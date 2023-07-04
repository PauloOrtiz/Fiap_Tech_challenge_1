import streamlit as st
from PIL import Image

st.set_page_config(page_title="Sobre",page_icon="❗")

image = Image.open("./src/img/download.jpg")
st.image(image)

st.markdown("""
    # <div style="text-align: center; color: #8A2BE2;"> Sobre o Projeto </div>
    
    Este projeto foi desenvolvido como parte do 1º Tech Challenge da turma de Data Science da FIAP. Foi uma oportunidade incrível para aprimorar nossas habilidades em análise de dados e colaboração em equipe, e gostaríamos de expressar nossa gratidão a todos que participaram deste desafio.

    ### <div style="text-align: center; color: #8A2BE2; "> Equipe do Projeto </div>
    
    - Leonardo Fernandes de Moraes Alves
    - Luiz Antonio Simette de Mello Campos
    - Paulo Henrique Barbosa Ortiz de Souza

    ### <div style="text-align: center; color: #8A2BE2;"> Orientadores </div>
    
    Este projeto não teria sido possível sem a orientação de nossos professores:

    - Edgard Joseph Kiriyama
    - Matheus Pavani

    Eles nos forneceram a estrutura necessária para concluir este desafio e estamos profundamente gratos pelo tempo e esforço que dedicaram à nossa aprendizagem.

    ### <div style="text-align: center; color: #8A2BE2;"> Agradecimentos </div>

    Também gostaríamos de agradecer aos nossos colegas de classe e a todos os envolvidos na organização deste desafio.

    ### <div style="text-align: center; color: #8A2BE2;"> Referências </div>

    Os dados utilizados neste projeto foram coletados a partir dos seguintes recursos:

    - Base de dados principal: [VitiBrasil](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_01)
    - Notícias: [AviGa](http://www.aviga.com.br/)
    - Dataset complementar: [Banco Central do Brasil](https://dadosabertos.bcb.gov.br/dataset/dolar-americano-usd-todos-os-boletins-diarios)
    
    Gostaríamos de expressar nossa gratidão a todas estas fontes por disponibilizar esses dados publicamente.
""", unsafe_allow_html=True)