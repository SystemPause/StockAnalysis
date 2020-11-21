class StockModel:
    def __init__(self, stockTitle, stockFullTitle, **kwargs):
        self.stockTitle = stockTitle
        self.stockFullTitle = stockFullTitle
        self.index = 0
        self.profitMargins = kwargs['profitMargins']
        self.operatingMargins = kwargs['operatingMargins']
        self.debtToEquity = kwargs['debtToEquity']
        self.currentRatio = kwargs['currentRatio']
        self.operatingCashflow = kwargs['operatingCashflow']
        self.trailingPE = kwargs['trailingPE']
        self.pegRatio = kwargs['pegRatio']
        self.dividendYield = kwargs['dividendYield']
        self.revenueGrowth = kwargs['revenueGrowth']
        self.returnOnEquity = kwargs['returnOnEquity']
        self.averageVolume = kwargs['averageVolume']
        self.enterpriseValueToRevenue = kwargs['enterpriseValueToRevenue']

    def __str__(self):
        myString = "stockTitle: " + self.stockTitle  + "\n" 
        myString += "stockFullTitle: " + self.stockFullTitle  + "\n" 
        myString += "index: " + str(self.index) + "\n" 
        myString += "profitMargins: " + str(self.profitMargins) + "\n" 
        myString += "operatingMargins: " + str(self.operatingMargins) + "\n" 
        myString += "debtToEquity: " + str(self.debtToEquity) + "\n" 
        myString += "currentRatio: " + str(self.currentRatio) + "\n" 
        myString += "operatingCashflow: " + str(self.operatingCashflow) + "\n" 
        myString += "trailingPE: " + str(self.trailingPE) + "\n" 
        myString += "pegRatio: " + str(self.pegRatio) + "\n" 
        myString += "dividendYield: " + str(self.dividendYield) + "\n" 
        myString += "revenueGrowth: " + str(self.revenueGrowth) + "\n" 
        myString += "returnOnEquity: " + str(self.returnOnEquity) + "\n" 
        myString += "averageVolume: " + str(self.averageVolume) + "\n" 
        myString += "enterpriseValueToRevenue: " + str(self.enterpriseValueToRevenue) + "\n" 
        return myString







