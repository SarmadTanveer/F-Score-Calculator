import requests
import json
import re

def getPriceReturn(ticker,startingYear):
    endingYear = str(int(startingYear) + 1)
    HS_p = requests.get(
        f"https://financialmodelingprep.com/api/v4/historical-price-full/{ticker}/{startingYear}-01-03?apikey=d684d9ac76fc9902f5608b588fff159b")
    HS_p = HS_p.json()
    print(json.dumps(HS_p))
    HS_1 = requests.get(
        f"https://financialmodelingprep.com/api/v4/historical-price-full/{ticker}/{endingYear}-01-04?apikey=d684d9ac76fc9902f5608b588fff159b")
    HS_1 = HS_1.json()
    print(json.dumps(HS_1))
    comissions = 20.00

    cost = HS_p['close']
    price = HS_1['close']
    percentReturn = ((price - cost) / (cost)) * 100

    info = [HS_p,HS_1]
    with open(ticker + '-priceData.json', 'w') as file:
        json.dump(info, file, indent=4)
        file.close()
    return percentReturn