import requests
from bs4 import BeautifulSoup
from StockModel import *
import pprint
from tqdm import tqdm

def get_values_from_yahoo(inputUrl):
    offset = 0
    estimatedResults = int(input("\n>>>Type the number of estimated results:\n"))

    temp = []
    while offset < estimatedResults:
        r  = requests.get(inputUrl + "?offset=" + str(offset))
        data = r.text
        soup = BeautifulSoup(data,"html.parser")
        for link in soup.find_all("a"):
            if 'Fw(600)' in link.get("class"):
                if ' ' not in str(link.text):
                    temp.append(str(link.text))
        offset += 25
    print("Checksum on extracted results:" + str(len(temp)))
    return temp

def extract_stats(stockList):
    finalResult = []
    elementsToFind = {
        'trailingPE': 'Trailing P/E',
        'pegRatio': 'PEG Ratio (5 yr expected)',
        'priceToSales': 'Price/Sales',
        'priceToBook': 'Price/Book',
        'enterpriseValueToRevenue': 'Enterprise Value/Revenue',
        'enterpriseValueToEBITDA': 'Enterprise Value/EBITDA',
        'profitMargins': 'Profit Margin',
        'operatingMargins': 'Operating Margin',
        'returnOnAssets': 'Return on Assets',
        'returnOnEquity': 'Return on Equity',
        'quarterlyRevenueGrowth': 'Quarterly Revenue Growth',
        'totalCashPerShare': 'Total Cash Per Share',
        'totalDebtToEquity': 'Total Debt/Equity',
        'currentRatio': 'Current Ratio',
        'operatingCashflow': 'Operating Cash Flow',
        'fiveYearAveragedividendYield': '5 Year Average Dividend Yield',
    }
    for index in tqdm(range(len(stockList))):
        stock = stockList[index]
        paramDict = {
            'trailingPE': '',
            'pegRatio': '',
            'priceToSales': '',
            'priceToBook': '',
            'enterpriseValueToRevenue': '',
            'enterpriseValueToEBITDA': '',
            'profitMargins': '',
            'operatingMargins': '',
            'returnOnAssets': '',
            'returnOnEquity': '',
            'quarterlyRevenueGrowth': '',
            'totalCashPerShare': '',
            'totalDebtToEquity': '',
            'currentRatio': '',
            'operatingCashflow': '',
            'fiveYearAveragedividendYield': '',
        }
        
        stockModel = None
        try:
            r  = requests.get("https://finance.yahoo.com/quote/" + stock + "/key-statistics")
            pageResponse = r.text
            soup = BeautifulSoup(pageResponse,"html.parser")
            for key, value in elementsToFind.items():
                extractedText = soup.find("span", string=value).parent.findNext("td")
                if(extractedText == None):
                    extractedText = None
                else:
                    extractedText = clean_value(key, extractedText.text)
                paramDict[key] = extractedText
            stockModel = StockModel(stock, **paramDict)
            
        except:
            print('\n' + stock + " : " + value)
            continue
        finalResult.append(stockModel)
    return finalResult


def clean_value(key, value):

    maxList = ["profitMargins", "operatingMargins", "returnOnAssets", "returnOnEquity", "quarterlyRevenueGrowth", "totalCashPerShare", "currentRatio", "operatingCashflow", "fiveYearAveragedividendYield"]
    minList = ["trailingPE", "pegRatio", "priceToSales", "priceToBook", "enterpriseValueToRevenue", "enterpriseValueToEBITDA", "totalDebtToEquity"]
    if '%' in value:
        return float(value.replace('%',''))
    if 'T' in value:
        return float(value.replace('T','')) * 10**12
    if 'B' in value:
        return float(value.replace('B','')) * 10**9
    if 'M' in value:
        return float(value.replace('M','')) * 10**6
    if 'K' in value:
        return float(value.replace('K','')) * 10**3
    try:
        return float(value)
    except:
        if(key in maxList):
            return float('-inf')
        else:
            return float('inf')


def apply_sorting(customListObj):

    # NEGATIVES
    customListObj.sort(key=lambda x: x.trailingPE, reverse=False)
    customListObj = sorting_index_calc(customListObj)

    customListObj.sort(key=lambda x: x.pegRatio, reverse=False)
    customListObj = sorting_index_calc(customListObj)

    customListObj.sort(key=lambda x: x.priceToSales, reverse=False)
    customListObj = sorting_index_calc(customListObj)

    customListObj.sort(key=lambda x: x.priceToBook, reverse=False)
    customListObj = sorting_index_calc(customListObj)

    customListObj.sort(key=lambda x: x.enterpriseValueToRevenue, reverse=False)
    customListObj = sorting_index_calc(customListObj)

    customListObj.sort(key=lambda x: x.enterpriseValueToEBITDA, reverse=False)
    customListObj = sorting_index_calc(customListObj)

    customListObj.sort(key=lambda x: x.totalDebtToEquity, reverse=False)
    customListObj = sorting_index_calc(customListObj)
    



    # POSITIVES
    customListObj.sort(key=lambda x: x.profitMargins, reverse=True)
    customListObj = sorting_index_calc(customListObj)

    customListObj.sort(key=lambda x: x.operatingMargins, reverse=True)
    customListObj = sorting_index_calc(customListObj)

    customListObj.sort(key=lambda x: x.returnOnAssets, reverse=True)
    customListObj = sorting_index_calc(customListObj)

    customListObj.sort(key=lambda x: x.returnOnEquity, reverse=True)
    customListObj = sorting_index_calc(customListObj)

    customListObj.sort(key=lambda x: x.quarterlyRevenueGrowth, reverse=True)
    customListObj = sorting_index_calc(customListObj)

    customListObj.sort(key=lambda x: x.totalCashPerShare, reverse=True)
    customListObj = sorting_index_calc(customListObj)

    customListObj.sort(key=lambda x: x.currentRatio, reverse=True)
    customListObj = sorting_index_calc(customListObj)


    # This is the final sorting to sort by index. It's false because we want the smallest first
    customListObj.sort(key=lambda x: x.index, reverse=False)

    return customListObj

    



def sorting_index_calc(customListObj):
    for i in range(len(customListObj)):
        customListObj[i].index += i
    return customListObj
