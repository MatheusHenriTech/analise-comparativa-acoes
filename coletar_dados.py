import yfinance as yf

ativos = ["BBSE3.SA", "ITSA4.SA", "VALE3.SA"]

dados = yf.download(
    tickers=ativos,
    start="2025-11-17",
    end="2026-11-18",
    interval="1d"
)

dados.to_csv("analise-carteira_b3/dados_acoes.csv")

print("Dados coletados e salvos com sucesso!")
