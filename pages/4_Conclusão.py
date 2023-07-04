import streamlit as st
from PIL import Image


st.set_page_config(page_title="Conclusão", page_icon="🍷")

image = Image.open("./src/img/download.jpg")
st.image(image)


st.markdown("""
    <h1 style = "text-align: center; color: #8A2BE2;">Conclusão e Orientações Futuras</h1>
    
    <p style="text-indent: 40px;">Ao longo deste relatório, exploramos em detalhes a performance de exportação da nossa empresa nos últimos 15 anos. Discutimos a evolução do faturamento, volume de vendas e o preço médio de venda por litro de vinho. Também levamos em consideração o impacto da variação cambial do dólar.</p>
    
    <p style="text-indent: 40px;">Vimos que nosso faturamento e volume de vendas têm mostrado uma tendência de crescimento constante, especialmente nos últimos anos. Isso sugere que nossos produtos estão ganhando cada vez mais aceitação no mercado global e que nossas estratégias de negócios estão funcionando bem.</p>
    
    <p style="text-indent: 40px;">No entanto, nosso valor médio de venda por litro de vinho tem mostrado uma tendência de queda recentemente. Isso pode ser um reflexo de nossa estratégia de tornar nossos vinhos mais acessíveis a um público mais amplo, mas também sugere que devemos continuar a monitorar essa tendência e a adaptar nossa estratégia de preços, se necessário.</p>
    
    <p style="text-indent: 40px;">Quanto ao cenário de exportação, sugerimos um investimento mais acentuado nos países em que tivemos maior crescimento de vendas e nos quais a aceitação do nosso vinho é alta, como Rússia e Canadá. Além disso, países com grandes populações e crescimento econômico, como China e Índia, também são mercados promissores a serem explorados.</p>
    
    <p style="text-indent: 40px;">No entanto, também devemos ter um pouco de cautela ao investir em países onde as vendas têm sido instáveis ou apresentaram declínio recente. Nessas regiões, uma abordagem mais cuidadosa e uma análise mais aprofundada do mercado podem ser necessárias antes de investir pesadamente.</p>
    
    <p style="text-indent: 40px;">Agradecemos a todos pelo seu apoio contínuo e confiança em nossa empresa. Vamos continuar a nos esforçar para melhorar nossos produtos e serviços e para expandir nossa presença no mercado global de vinhos.</p>
    
    <p style="text-indent: 40px;">Nosso futuro é brilhante e estamos entusiasmados com as oportunidades que estão por vir. Vamos continuar a compartilhar nossas atualizações e resultados com vocês. Até lá, brindemos ao sucesso contínuo e ao futuro da nossa empresa!</p>

    """,unsafe_allow_html=True )
