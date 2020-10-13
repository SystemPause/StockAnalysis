def pegRatio_filter(obj):
    if obj.pegRatio is None:
        return False
        
    if obj.pegRatio <= 1.5:
        return True
    return False

def enterpriseValueToEBITDA_filter(obj):
    if obj.enterpriseValueToEBITDA is None:
        return False
        
    if obj.enterpriseValueToEBITDA <= 15:
        return True
    return False

def returnOnEquity_filter(obj):
    if obj.returnOnEquity is None:
        return False
        
    if obj.returnOnEquity >= 10:
        return True
    return False

def quarterlyRevenueGrowth_filter(obj):
    if obj.quarterlyRevenueGrowth is None:
        return False
        
    if obj.quarterlyRevenueGrowth >= 8:
        return True
    return False 


def currentRatio_filter(obj):
    if obj.currentRatio is None:
        return False
        
    if obj.currentRatio >= 1.2:
        return True
    return False

def operatingCashflow_filter(obj):
    if obj.operatingCashflow is None:
        return False
        
    if obj.operatingCashflow >= 0:
        return True
    return False


def fiveYearAveragedividendYield_filter(obj):
    if obj.fiveYearAveragedividendYield is None:
        return False
        
    if obj.fiveYearAveragedividendYield >= 0:
        return True
    return False


# Add the filter to apply here
FILTERSLIST = [pegRatio_filter,enterpriseValueToEBITDA_filter,returnOnEquity_filter,quarterlyRevenueGrowth_filter,currentRatio_filter,operatingCashflow_filter,fiveYearAveragedividendYield_filter]
