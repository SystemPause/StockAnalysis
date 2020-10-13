from HelperFunctions import *
import time
from StockObjFilters import *


# Asks for input from user 
inputLink = input("\n>>>Type Yahoo Screener URL:\n")
stocks = get_values_from_yahoo(inputLink)
print("\n>>>Computing...\n")
print("###################################################")
start_time = time.time()

# We first extract all relevant stats
stockObjList = extract_stats(stocks)
# Apply all filters, so we filter out what does not satisy our criteria
for customFilter in FILTERSLIST:
    stockObjList = list(filter(customFilter, stockObjList))

# Sort by properties
stockObjList = apply_sorting(stockObjList)

print('\n')
for i in range(len(stockObjList)):
    stockObj = stockObjList[i]
    print(str(i+1) + ": " + stockObj.stockTitle)

print("\nTotal execution time " + str((time.time() - start_time)))
print("###################################################")


# Close the program
print("\n Press ENTER to close the shell")
string = input()
string = ""
if string == "":
    exit()
