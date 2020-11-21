import requests
from bs4 import BeautifulSoup
from StockModel import *
import pprint
from tqdm import tqdm

def get_estimated_results(inputUrl):
    r  = requests.get(inputUrl)
    data = r.text
    soup = BeautifulSoup(data,"html.parser")
    estimatedResults = int((soup.find(class_="Mstart(15px) Fw(500) Fz(s)").text).split(" ")[2])
    return estimatedResults

# The function returns a list of tuples containing
# the stock code and the stock title
def get_values_from_yahoo(inputUrl, estimatedResults):
    offset = 0

    temp = []
    while offset < estimatedResults:
        r  = requests.get(inputUrl + "?offset=" + str(offset))
        data = r.text
        soup = BeautifulSoup(data,"html.parser")
        for link in soup.find_all("a"):
            if 'Fw(600)' in link.get("class"):
                if ' ' not in str(link.text):
                    # Now we append a tuple to the list. 
                    # - The first value is the stock code 
                    # - The second value is the stock full name
                    temp.append((str(link.text), link['title']))
        offset += 25
    print("Checksum on extracted results:" + str(len(temp)))
    return temp

def extract_stats(stockList):
    finalResult = []
    elementsToFind = {
        'profitMargins': 'Profit margin',
        'operatingMargins': 'Operating margin',
        'debtToEquity': 'Total debt/equity',
        'currentRatio': 'Current ratio',
        'operatingCashflow': 'Operating cash flow',
        'trailingPE': 'Trailing P/E',
        'pegRatio': 'PEG ratio (5-yr expected)',
        'dividendYield': '5-year average dividend yield',
        'revenueGrowth': 'Quarterly revenue growth',
        'returnOnEquity': 'Return on equity',
        'averageVolume': 'Avg vol (10-day)',
        'enterpriseValueToRevenue': 'Enterprise value/revenue'
    }
    for index in tqdm(range(len(stockList))):
        stock = stockList[index]
        paramDict = {
            'profitMargins': "",
            'operatingMargins': "",
            'debtToEquity': "",
            'currentRatio': "",
            'operatingCashflow': "",
            'trailingPE': "",
            'pegRatio': "",
            'dividendYield': "",
            'revenueGrowth': "",
            'returnOnEquity': "",
            'averageVolume': "",
            'enterpriseValueToRevenue':""
        }
        
        stockModel = None
        try:
            # Notice we need stock[0] as we are accessing the first element in the tuple
            r  = requests.get("https://uk.finance.yahoo.com/quote/" + stock[0] + "/key-statistics")
            pageResponse = r.text
            soup = BeautifulSoup(pageResponse,"html.parser")
            for key, value in elementsToFind.items():
                extractedText = soup.find("span", string=value).parent.findNext("td")
                if(extractedText == None):
                    extractedText = None
                else:
                    extractedText = clean_value(key, extractedText.text)
                paramDict[key] = extractedText
            stockModel = StockModel(stock[0], stock[1], **paramDict)
            
        except:
            print('\n' + stock[0] + " - " + stock[1] + " : " + value)
            continue
        finalResult.append(stockModel)
        
    return finalResult


def clean_value(key, value):

    maxList = ["profitMargins", "operatingMargins", "currentRatio", "revenueGrowth"]
    minList = ["debtToEquity", "trailingPE", "pegRatio", "enterpriseValueToRevenue"]
    if ',' in value: 
        value = value.replace(',','')
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
    customListObj.sort(key=lambda x: x.profitMargins, reverse=True)
    sorting_index_calc(customListObj)

    customListObj.sort(key=lambda x: x.operatingMargins, reverse=True)
    sorting_index_calc(customListObj)

    customListObj.sort(key=lambda x: x.debtToEquity, reverse=False)
    sorting_index_calc(customListObj)

    customListObj.sort(key=lambda x: x.currentRatio, reverse=True)
    sorting_index_calc(customListObj)

    customListObj.sort(key=lambda x: x.trailingPE, reverse=False)
    sorting_index_calc(customListObj)

    customListObj.sort(key=lambda x: x.pegRatio, reverse=False)
    sorting_index_calc(customListObj)

    customListObj.sort(key=lambda x: x.revenueGrowth, reverse=True)
    sorting_index_calc(customListObj)

    customListObj.sort(key=lambda x: x.enterpriseValueToRevenue, reverse=False)
    sorting_index_calc(customListObj)

    customListObj.sort(key=lambda x: x.index, reverse=False)

    return customListObj

    



def sorting_index_calc(customListObj):
    for i in range(len(customListObj)):
        customListObj[i].index += i
    return customListObj
