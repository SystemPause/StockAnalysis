class StockModel:
    def __init__(self, stockTitle,  **kwargs):
        self.stockTitle = stockTitle
        self.index = 0
        self.trailingPE = kwargs['trailingPE']
        self.pegRatio = kwargs['pegRatio']
        self.priceToSales = kwargs['priceToSales']
        self.priceToBook = kwargs['priceToBook']
        self.enterpriseValueToRevenue = kwargs['enterpriseValueToRevenue']
        self.enterpriseValueToEBITDA = kwargs['enterpriseValueToEBITDA']
        self.profitMargins = kwargs['profitMargins']
        self.operatingMargins = kwargs['operatingMargins']
        self.returnOnAssets = kwargs['returnOnAssets']
        self.returnOnEquity = kwargs['returnOnEquity']
        self.quarterlyRevenueGrowth = kwargs['quarterlyRevenueGrowth']
        self.totalCashPerShare = kwargs['totalCashPerShare']
        self.totalDebtToEquity = kwargs['totalDebtToEquity']
        self.currentRatio = kwargs['currentRatio']
        self.operatingCashflow = kwargs['operatingCashflow']
        self.fiveYearAveragedividendYield = kwargs['fiveYearAveragedividendYield']
        
        
        
        
        
        

    def __str__(self):
        myString = "stockTitle: " + self.stockTitle  + "\n" 
        myString += "index: " + str(self.index) + "\n" 
        myString += "trailingPE: " + str(self.trailingPE) + "\n" 
        myString += "pegRatio: " + str(self.pegRatio) + "\n" 
        myString += "priceToSales: " + str(self.priceToSales) + "\n" 
        myString += "priceToBook: " + str(self.priceToBook) + "\n" 
        myString += "enterpriseValueToRevenue: " + str(self.enterpriseValueToRevenue) + "\n" 
        myString += "enterpriseValueToEBITDA: " + str(self.enterpriseValueToEBITDA) + "\n" 
        myString += "profitMargins: " + str(self.profitMargins) + "\n" 
        myString += "operatingMargins: " + str(self.operatingMargins) + "\n" 
        myString += "returnOnAssets: " + str(self.returnOnAssets) + "\n" 
        myString += "returnOnEquity: " + str(self.returnOnEquity) + "\n" 
        myString += "quarterlyRevenueGrowth: " + str(self.quarterlyRevenueGrowth) + "\n" 
        myString += "totalCashPerShare: " + str(self.totalCashPerShare) + "\n" 
        myString += "totalDebtToEquity: " + str(self.totalDebtToEquity) + "\n" 
        myString += "currentRatio: " + str(self.currentRatio) + "\n" 
        myString += "operatingCashflow: " + str(self.operatingCashflow) + "\n" 
        myString += "fiveYearAveragedividendYield: " + str(self.fiveYearAveragedividendYield) + "\n" 

        return myString







