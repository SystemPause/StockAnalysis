from HelperFunctions import *
import time


# Asks for input from user 
inputLink = input("\n>>>Type Yahoo Screener URL:\n")
stocks = get_values_from_yahoo(inputLink)
print(stocks)
print("\n>>>Computing...\n")
print("###################################################")
start_time = time.time()

stockObjList = extract_stats(stocks)
for stockObj in stockObjList:
    print(stockObj)

print("\nTotal execution time " + str((time.time() - start_time)))
print("###################################################")


# Close the program
print("\n Press ENTER to close the shell")
string = input()
string = ""
if string == "":
    exit()
