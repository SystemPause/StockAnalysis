from HelperFunctions import *
import time
from StockObjFilters import *
import sys

# This file gets the following arguments as input
# - sys.argv[1]: inter/auto (first one asks for user input the second one proceeds manually)
# - sys.argv[2]: the screener url

# If interactive mode
if sys.argv[1] == "inter":
    # Asks for input from user 
    inputLink = input("\n>>>Type Yahoo Screener URL:\n")

    # Get number of estimated results
    estimatedResults = int(input("\n>>>Type the number of estimated results:\n"))
if sys.argv[1] == "auto":
    inputLink = sys.argv[2]
    estimatedResults = get_estimated_results(inputLink)
    print("Estimated Results: " + str(estimatedResults))


# This step is required in order to clean the input link and remove any provided
# url parameters
if "?" in inputLink: 
    inputLink = inputLink.split("?")[0]

stocks = get_values_from_yahoo(inputLink, estimatedResults)
print("\n>>>Computing...\n")
print("###################################################")
start_time = time.time()

stockObjList = extract_stats(stocks)
# Apply all filters
for customFilter in FILTERSLIST:
    stockObjList = list(filter(customFilter, stockObjList))
# Sort by properties
stockObjList = apply_sorting(stockObjList)

print('\n')

# Write a file and save the results
with open(inputLink.split("/")[-1]+".txt", "w+") as f:
    print("Processed stocks: " + str(estimatedResults) + "\n")
    f.write(inputLink.split("/")[-1].upper() + "\n")
    f.write("Processed stocks: " + str(estimatedResults) + "\n\n")
    for i in range(len(stockObjList)):
        stockObj = stockObjList[i]
        resultLine = str(i+1) + ": " + stockObj.stockTitle + " - " + stockObj.stockFullTitle
        print(resultLine)
        f.write(resultLine + "\n")
    f.write("=====================\n\n")
print("\nTotal execution time " + str((time.time() - start_time)))
print("###################################################")


# Close the program
# print("\n Press ENTER to close the shell")
# string = input()
# string = ""
# if string == "":
#     exit()
