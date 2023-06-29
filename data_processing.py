#Libs
import pandas as pd
import numpy as np




#importação dos dados
df = pd.read_csv("./src/data/ExpVinho.csv", sep=";")
df_dolar = pd.read_csv("./src/data/dolar.csv", sep=";", decimal=",")

#Alteração do indice
df=df.set_index(['País'])
df.drop(columns='Id', inplace=True)


#removendo do Brasil dos dados
df.drop('Brasil', inplace=True)


#buscando os ultimos 15 anos para analise
ano_analise = df.columns[74:]
df = df[ano_analise]


# Separando e criando os dataset de valores e quantidade
columns_valor = [col for col in df.columns if '.1' in col]
columns_qtd = [col for col in df.columns if '.1' not in  col]
df_valor = df[columns_valor]
df_valor= df_valor.rename(columns=lambda c: c.replace('.1',''))
df_volume = df[columns_qtd]


#Adicionando a coluna e linha de Totais no dataframe de valores e volumes:

df_valor.loc[:, 'Total'] = df_valor.sum(axis=1)
df_valor.loc['total', :] = df_valor.sum()
df_volume.loc[:, 'Total'] = df_volume.sum(axis=1)
df_volume.loc['total', :]= df_volume.sum() 
df_volume = df_volume[df_volume['Total'] != 0]
df_valor = df_valor[df_valor['Total'] != 0]


#criando um dataframe que traz a media preço por litro vendido por ano.

linha1 = df_valor.loc['total']
linha2 = df_volume.loc['total']
resultado = linha1/linha2
df_resultado = pd.DataFrame(resultado)
#df_resultado = df_resultado.T
df_resultado = df_resultado.reset_index()
df_resultado = df_resultado.rename(columns={'index':'Anos', 'total':'Total'})
df_resultado = df_resultado.round(2)
df_resultado = df_resultado.iloc[:-1]

#criando um dataframe dos volume e valores de vendas dos ultimos 15 anos
df_valor_total = df_valor[['Total']]
df_valor_total = df_valor_total.rename(columns={'Total':'Valor (US$)'})
df_valor_total['Valor (US$)'] = df_valor_total['Valor (US$)'].astype('int64')

df_volume_total = df_volume[['Total']]
df_volume_total = df_volume_total.rename(columns={'Total':'Volume KG'})

df_total_final = df_valor_total.merge(df_volume_total,how='left',on='País')
df_total_final['Origem'] = 'Brasil'
df_total_final = df_total_final[['Origem', 'Volume KG', 'Valor (US$)']]
df_total_final = df_total_final.iloc[:-1]

#criando os valores Totais por anos:
df_valor_2 = df_valor.iloc[:-1]
df_valor_2 =df_valor_2.reset_index()
df_valor_2 = df_valor_2.drop(columns=['País', 'Total'])
total_por_ano = df_valor_2.sum()
df_total_por_ano = total_por_ano.reset_index()
df_total_por_ano.columns = ['Anos', 'Total']

#criando os Volumetria totais por anos:
df_volume_2 = df_volume.iloc[:-1]
df_volume_2 =df_volume_2.reset_index()
df_volume_2 = df_volume_2.drop(columns=['País', 'Total'])
volume_por_ano = df_volume_2.sum()
df_volume_por_ano = volume_por_ano.reset_index()
df_volume_por_ano.columns = ['Anos', 'Total']


#Criação de dataSets dos dados sumarizados
meses = df_valor.columns.str.replace("$","")
meses=meses.drop("Total")
meses

meses_valor = df_valor.columns
meses_valor=meses_valor.drop("Total")
meses_valor
df_valor_ = df_valor.reset_index()
df_agg_valor = df_valor_.melt(id_vars=['País'],value_vars=meses_valor,var_name='anomes', value_name="sumtOfExport")
df_agg_valor= df_agg_valor.reset_index()

#Criação data set de porpoção


dt=((df_valor["Total"].groupby(by=df_valor.index, sort=True ).sum())/1000000).round(decimals = 2)
dt= dt.sort_values(ascending=False)
dt2 = pd.DataFrame(dt)
dt2 = dt2.iloc[1:]
dt2 = dt2.loc[dt2["Total"] > 0]
dt2['perc_acum'] = (dt2['Total'].cumsum()/dt2['Total'].sum()*100).round(decimals = 2)
dt2=dt2.reset_index()
dt2['group'] = np.where(dt2['perc_acum']>95, 'Others', dt2['País'])

dt2_agg= dt2.groupby(["group"])["Total"].sum().round(decimals = 2)
dt2_agg2 = dt2.groupby(["group"])["perc_acum"].mean().round(decimals = 2)
dt2_agg = pd.DataFrame(dt2_agg)
dt2_agg2 = pd.DataFrame(dt2_agg2)
dt2_agg_final = dt2_agg.merge(dt2_agg2, how="left", on="group")
paises_pareto = dt2_agg_final.index.unique()

#Criação da analise do dolar
df_dolar['timestamp'] = pd.to_datetime(df_dolar['dataHoraCotacao'])
df_dolar['anomes'] = df_dolar['timestamp'].dt.year
df_dolar['anomes'] = df_dolar["anomes"].astype(int)
maiores_datas_por_ano = df_dolar.groupby('anomes')['timestamp'].max().reset_index()

#analise do dolar

indee=["Alemanha, República Democrática","Austrália","Bélgica","Canadá","Espanha","Estados Unidos","Finlândia","França","Japão","Paraguai","Países Baixos","Polônia","Portugal","Reino Unido","Rússia","Suíça","Tcheca, República"]
meses = df_valor.columns.str.replace("$","")
meses=meses.drop("Total")
meses_valor = df_valor.columns
meses=meses_valor.drop("Total")
df_volume_= df_volume.reset_index()
df_valor_= df_valor.reset_index()
colunas_dolar = ['timestamp',"cotacaoVenda"]
df_dolar_final = maiores_datas_por_ano.merge(df_dolar[colunas_dolar], how='left', on='timestamp')
df_valor_vol_agg = df_volume_.melt(id_vars='País',value_vars=meses,var_name='anomes', value_name="countOfExport")
df_valor_vol_agg= df_valor_vol_agg[df_valor_vol_agg["País"].isin(indee)]

df_valor_agg = df_valor_.melt(id_vars='País',value_vars=meses_valor,var_name='anomes', value_name="sumOfExport")
df_valor_val_agg= df_valor_agg[df_valor_agg["País"].isin(indee)]
df_ = df_valor_vol_agg.merge(df_valor_val_agg, how='left' ,on=["País","anomes"])
df_["anomes"] = df_["anomes"].astype(int)
df_ = df_.merge(df_dolar_final, how='left' ,on=["anomes"])
df_ = df_.loc[df_["countOfExport"] > 0]
df_["ticket_medio"] = df_.sumOfExport/df_.countOfExport
paises = ["Paraguai","Rússia","Reino Unido","Países Baixos","China","Estados Unidos"]
df_ = df_[df_["País"].isin(paises)]
df_cotacao = df_.groupby("anomes")[["cotacaoVenda","ticket_medio"]].mean()
#Gera dicionario com a lista de paises:
dict_abr = {
    "Afeganistão": "AFG",
    "África do Sul": "ZAF",
    "Albânia": "ALB",
    "Alemanha": "DEU",
    "Andorra": "AND",
    "Angola": "AGO",
    "Antígua e Barbuda": "ATG",
    "Arábia Saudita": "SAU",
    "Argélia": "DZA",
    "Argentina": "ARG",
    "Armênia": "ARM",
    "Austrália": "AUS",
    "Áustria": "AUT",
    "Azerbaijão": "AZE",
    "Bahamas": "BHS",
    "Bahrein": "BHR",
    "Bangladesh": "BGD",
    "Barbados": "BRB",
    "Belarus": "BLR",
    "Bélgica": "BEL",
    "Belize": "BLZ",
    "Benin": "BEN",
    "Bolívia": "BOL",
    "Bósnia e Herzegovina": "BIH",
    "Botsuana": "BWA",
    "Brasil": "BRA",
    "Brunei": "BRN",
    "Bulgária": "BGR",
    "Burkina Faso": "BFA",
    "Burundi": "BDI",
    "Butão": "BTN",
    "Cabo Verde": "CPV",
    "Camarões": "CMR",
    "Camboja": "KHM",
    "Canadá": "CAN",
    "Catar": "QAT",
    "Cazaquistão": "KAZ",
    "Chade": "TCD",
    "Chile": "CHL",
    "China": "CHN",
    "Chipre": "CYP",
    "Colômbia": "COL",
    "Comores": "COM",
    "Congo": "COG",
    "Costa do Marfim": "CIV",
    "Costa Rica": "CRI",
    "Croácia": "HRV",
    "Cuba": "CUB",
    "Dinamarca": "DNK",
    "Djibouti": "DJI",
    "Dominica": "DMA",
    "Egito": "EGY",
    "El Salvador": "SLV",
    "Emirados Árabes Unidos": "ARE",
    "Equador": "ECU",
    "Eritreia": "ERI",
    "Eslováquia": "SVK",
    "Eslovênia": "SVN",
    "Espanha": "ESP",
    "Estados Unidos": "EUA",
    "Estônia": "EST",
    "Eswatini": "SWZ",
    "Etiópia": "ETH",
    "Fiji": "FJI",
    "Filipinas": "PHL",
    "Finlândia": "FIN",
    "França": "FRA",
    "Gabão": "GAB",
    "Gâmbia": "GMB",
    "Gana": "GHA",
    "Geórgia": "GEO",
    "Granada": "GRD",
    "Grécia": "GRC",
    "Guatemala": "GTM",
    "Guiné-Bissau": "GNB",
    "Guiana": "GUY",
    "Haiti": "HTI",
    "Holanda": "NLD",
    "Honduras": "HND",
    "Hungria": "HUN",
    "Iêmen": "YEM",
    "Ilhas Cayman": "CYM",
    "Ilhas Cook": "COK",
    "Ilhas Faroe": "FRO",
    "Ilhas Marshall": "MHL",
    "Ilhas Salomão": "SLB",
    "Ilhas Virgens Americanas": "VIR",
    "Ilhas Virgens Britânicas": "VGB",
    "Índia": "IND",
    "Indonésia": "IDN",
    "Irã": "IRN",
    "Iraque": "IRQ",
    "Irlanda": "IRL",
    "Islândia": "ISL",
    "Israel": "ISR",
    "Itália": "ITA",
    "Jamaica": "JAM",
    "Japão": "JPN",
    "Jersey": "JEY",
    "Jordânia": "JOR",
    "Kiribati": "KIR",
    "Kuwait": "KWT",
    "Laos": "LAO",
    "Lesoto": "LSO",
    "Letônia": "LVA",
    "Líbano": "LBN",
    "Libéria": "LBR",
    "Líbia": "LBY",
    "Liechtenstein": "LIE",
    "Lituânia": "LTU",
    "Luxemburgo": "LUX",
    "Macedônia do Norte": "MKD",
    "Madagascar": "MDG",
    "Malásia": "MYS",
    "Malawi": "MWI",
    "Maldivas": "MDV",
    "Mali": "MLI",
    "Malta": "MLT",
    "Marrocos": "MAR",
    "Martinica": "MTQ",
    "Mauritânia": "MRT",
    "Maurício": "MUS",
    "Mayotte": "MYT",
    "México": "MEX",
    "Micronésia": "FSM",
    "Moçambique": "MOZ",
    "Moldávia": "MDA",
    "Mônaco": "MCO",
    "Mongólia": "MNG",
    "Montenegro": "MNE",
    "Montserrat": "MSR",
    "Myanmar": "MMR",
    "Namíbia": "NAM",
    "Nauru": "NRU",
    "Nepal": "NPL",
    "Nicarágua": "NIC",
    "Níger": "NER",
    "Nigéria": "NGA",
    "Niue": "NIU",
    "Noruega": "NOR",
    "Nova Caledônia": "NCL",
    "Nova Zelândia": "NZL",
    "Omã": "OMN",
    "Palau": "PLW",
    "Panamá": "PAN",
        "Panamá": "PAN",
    "Papua-Nova Guiné": "PNG",
    "Paquistão": "PAK",
    "Paraguai": "PRY",
    "Países Baixos": "NLD",
    "Peru": "PER",
    "Filipinas": "PHL",
    "Polônia": "POL",
    "Portugal": "PRT",
    "Catar": "QAT",
    "Romênia": "ROU",
    "Rússia": "RUS",
    "Ruanda": "RWA",
    "São Cristóvão e Neves": "KNA",
    "Santa Lúcia": "LCA",
    "São Vicente e Granadinas": "VCT",
    "Samoa": "WSM",
    "San Marino": "SMR",
    "São Tomé e Príncipe": "STP",
    "Arábia Saudita": "SAU",
    "Senegal": "SEN",
    "Sérvia": "SRB",
    "Seychelles": "SYC",
    "Serra Leoa": "SLE",
    "Cingapura": "SGP",
    "Eslováquia": "SVK",
    "Eslovênia": "SVN",
    "Ilhas Salomão": "SLB",
    "Somália": "SOM",
    "África do Sul": "ZAF",
    "Sudão do Sul": "SSD",
    "Espanha": "ESP",
    "Sri Lanka": "LKA",
    "Sudão": "SDN",
    "Suriname": "SUR",
    "Suazilândia": "SWZ",
    "Suécia": "SWE",
    "Suíça": "CHE",
    "Síria": "SYR",
    "Taiwan": "TWN",
    "Tajiquistão": "TJK",
    "Tanzânia": "TZA",
    "Tailândia": "THA",
    "Timor-Leste": "TLS",
    "Togo": "TGO",
    "Tonga": "TON",
    "Trinidad e Tobago": "TTO",
    "Tunísia": "TUN",
    "Turquia": "TUR",
    "Turcomenistão": "TKM",
    "Tuvalu": "TUV",
    "Uganda": "UGA",
    "Ucrânia": "UKR",
    "Emirados Árabes Unidos": "ARE",
    "Reino Unido": "GBR",
    "Estados Unidos": "EUA",
    "Uruguai": "URY",
    "Uzbequistão": "UZB",
    "Vanuatu": "VUT",
    "Venezuela": "VEN",
    "Vietnã": "VNM",
    "Iêmen": "YEM",
    "Zâmbia": "ZMB",
    "Zimbábue": "ZWE"

}

#Analise mapa de calor

df_agg_valor_sigla = df_agg_valor.replace({"País": dict_abr})
df_agg_valor_sigla_total = df_agg_valor_sigla.groupby("País")["sumtOfExport"].sum()
df_agg_valor_sigla_total=df_agg_valor_sigla_total.reset_index()
agg = pd.DataFrame(df_agg_valor_sigla_total)

#Boxplot para projeção
df_agg_valor_aj = df_agg_valor.loc[df_agg_valor["sumtOfExport"] > 0]
df_agg_valor_aj = df_agg_valor_aj.loc[df_agg_valor_aj["País"] != "total"]
df_agg_valor_aj = df_agg_valor_aj.sort_values("sumtOfExport", ascending=False)
df_agg_valor_mean = df_agg_valor_aj.groupby(["País"])["sumtOfExport"].mean()/1000000
df_agg_valor_mean = df_agg_valor_mean.reset_index()
df_agg_valor_mean = df_agg_valor_mean.sort_values("sumtOfExport", ascending=False)
df_agg_valor_mean_10 = df_agg_valor_mean.iloc[:10,:]
df_agg_boxplot_10 = df_agg_valor_aj.merge(df_agg_valor_mean_10["País"], how="inner", on="País")

# Considere que 'df' é o seu DataFrame original
# Supondo que você deseje remover os outliers da coluna 'Valores'

# Calcule os limites do boxplot
Q1 = df_agg_boxplot_10['sumtOfExport'].quantile(0.25)
Q3 = df_agg_boxplot_10['sumtOfExport'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Crie uma nova versão do DataFrame excluindo os outliers
df_agg_boxplot_outliers = df_agg_boxplot_10[(df_agg_boxplot_10['sumtOfExport'] >= lower_bound) & (df_agg_boxplot_10['sumtOfExport'] <= upper_bound)]

#retirados os outlier vamos as projeções

#Ajusta a coluna de data para a projeção

#df_agg_boxplot_outliers['Data'] = pd.to_datetime(df_agg_boxplot_outliers['anomes'], format='%Y')
df_agg_boxplot_outliers['Data'] = pd.to_datetime(df_agg_boxplot_outliers['anomes'])


#Definir as colunas ds e y para projeção
df_agg_boxplot_prophet = df_agg_boxplot_outliers.rename(columns={'Data': 'ds', 'sumtOfExport': 'y','País': 'country',})



#exportanto os dataframes tratados:

df_valor.to_csv('./src/data/valores.csv', index=True)
df_volume.to_csv('./src/data/volume.csv', index=True)
df_resultado.to_csv('./src/data/resultado.csv', index=False)
df_total_final.to_csv('./src/data/total_final.csv', index=True)
df_total_por_ano.to_csv('./src/data/total_por_ano.csv', index=False)
df_volume_por_ano.to_csv('./src/data/volume_por_ano.csv', index=False)
dt2_agg_final.to_csv('./src/data/porpo.csv', index=True)
df_cotacao.to_csv('./src/data/cotacao.csv', index=True)
agg.to_csv('./src/data/sigla_venda_total.csv', index=False)
df_agg_boxplot_10.to_csv('./src/data/boxplot_projecao.csv')
df_agg_boxplot_prophet.to_csv('./src/data/previsao.csv', index=False)