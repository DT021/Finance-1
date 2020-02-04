import AnalysisModule as Ass
import GraphFunctions as Gfs
import yfinance as yf

listOfStocksToAnalyze = ["AAPL", "ACIW", "ADS.DE", "ADSK", "ALO", "AMD", "AZPN", "BA", "BABA", "BAYN.DE", "BLL",
                         "BYND", "BMW.DE", "CVNA", "DDOG", "DIS", "EQT", "F", "FB", "FCEL", "GE", "GOOG", "GPRO",
                         "GRMN",
                         "INCY", "JD", "KEX", "KO", "MA", "MSFT", "MAERSK-B.CO", "MCD", "NFLX", "NIO", "NKE", "NLOK",
                         "NVDA", "NOVO-B.CO", "NZYM-B.CO", "OKTA", "ON", "PCG", "ROKU", "SHOP", "SNAP", "SPCE", "SPOT",
                         "SQ", "SQQQ",
                         "STM", "SU.PA", "SYY", "TEVA", "TSLA", "TWTR", "UBER", "ULTA", "UPS", "V", "VLO", "VWS.CO",
                         "VZ",
                         "WB", "WORK", "ZM"]


proposedbuylist = []
proposedselllist = []

for stock in listOfStocksToAnalyze:
    StockData = yf.Ticker(stock).history(period="1y")
    if Ass.macd_potential_buy(StockData):
        proposedbuylist.append(stock)
        print("Something you might wanna buy because of MACD is " + stock)
        continue

    if Ass.macd_potential_sell(StockData):
        proposedselllist.append(stock)
        print("Something you might wanna sell because of MACD is " + stock)


for stock in proposedbuylist:
    StockData = yf.Ticker(stock).history(period="1y")
    Gfs.draw_macd_buy(StockData, "BUY " + stock)

for stock in proposedselllist:
    StockData = yf.Ticker(stock).history(period="1y")
    Gfs.draw_macd_sell(StockData, "SELL " + stock)

print(proposedselllist)
print(proposedbuylist)
