import pandas as pd

###Leitura do CSV ###
dfposicaofinanceira = pd.read_csv('Dados_Tabela_PosicaoFinanceira.csv',  delimiter=";")

### Definição das colunas com tempo bugado ###
temposbugados = ["DataVenda","DataLiberacaoChaves","DataCessao","DataDesembolso","DataEntregaInicial","DataHabiteSe","DataChaves","DataPrevisaoEntrega","DataQuitacao","LR_DataVencimento","LR_DataRenegociacao","DataUltimaPrestacaoPaga","DataUltimaAlteracao"]
###Transformação em datetime ###
dfposicaofinanceira[temposbugados] = dfposicaofinanceira[temposbugados].apply(pd.to_datetime)
###Formatação Ano mês e dia###
dfposicaofinanceira[temposbugados] = dfposicaofinanceira[temposbugados].apply(lambda x : x.dt.strftime('%Y-%m-%d'))



###Substituições ###
dfposicaofinanceira["FormaPagamento"] = dfposicaofinanceira["FormaPagamento"].replace({0:"Quitação a vista",1:"Financiamento bancário",2:"Alienação fiduciária",3:"Securitização"})

dfposicaofinanceira["SituacaoUnidade"] = dfposicaofinanceira["SituacaoUnidade"].replace({"Q ":"Quitada", "VD":"Vendida"})
dfposicaofinanceira["FaseIncorporacao"] = dfposicaofinanceira["FaseIncorporacao"].replace({0:"Sim"})

###Preenchimento dos Not a numbers e substituições ###
dfposicaofinanceira["StatusDistrato"] = dfposicaofinanceira["StatusDistrato"].fillna(0)
dfposicaofinanceira["StatusDistrato"] = dfposicaofinanceira["StatusDistrato"].replace({0:"Não", 1:"Sim"})

###Leitura dos CSVs ###
dfclientes = pd.read_csv('Dados_Tabela_Clientes.csv',  delimiter=";")
dfcontrolesessao = pd.read_csv('Dados_Tabela_Controlesessao.csv',  delimiter=";")
dflognavegacao = pd.read_csv('Dados_Tabela_LogNavegacao.csv',  delimiter=";")
dfparcelas = pd.read_csv('Dados_Tabela_Parcelas.csv',  delimiter=";")

###Transformação da matriz em excel ###
dfposicaofinanceira.to_excel("posicaofinanceira.xlsx")
dfclientes.to_excel("dfclientes.xlsx")
dfcontrolesessao.to_excel("dfcontrolesessao.xlsx")
dflognavegacao.to_excel("dflognavegacao.xlsx")
dfparcelas.to_excel("dfparcelas.xlsx")