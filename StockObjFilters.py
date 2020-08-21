
def currentRatio_filter(obj):
    if obj.currentRatio is None:
        return True
        
    if obj.currentRatio >= 1.25:
        return True
    return False

def operatingCashflow_filter(obj):
    if obj.operatingCashflow is None:
        return True
        
    if obj.operatingCashflow >= 0:
        return True
    return False

def pegRatio_filter(obj):
    if obj.pegRatio is None:
        return True
        
    if obj.pegRatio <= 1.5:
        return True
    return False

def dividendYield_filter(obj):
    if obj.dividendYield is None:
        return True
        
    if obj.dividendYield >= 0:
        return True
    return False

def revenueGrowth_filter(obj):
    if obj.revenueGrowth is None:
        return True
        
    if obj.revenueGrowth >= 8:
        return True
    return False 

def averageVolume_filter(obj):
    if obj.averageVolume is None:
        return True
        
    if obj.averageVolume >= 400000:
        return True
    return False 

# Add the filter to apply here
FILTERSLIST = [currentRatio_filter, operatingCashflow_filter, pegRatio_filter, dividendYield_filter, revenueGrowth_filter, averageVolume_filter]
