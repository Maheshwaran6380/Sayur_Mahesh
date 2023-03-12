""" 1. Write an app for a cafe. Decide on the items in the cafe, stock of each item in the morning, 
stock in the evening, sales amount at the end of the day and profit for each item. You need to restock an item 
if the supply reaches 20% of the stock. Print the 3 items with highest sales, and top 3 highest profit."""

items = ["coffee", "tea", "cookies", "donuts", "bun"]
itemPrice = [20, 20, 10, 15, 5]
itemStock = [100, 100, 50, 60, 40]
refillStock = [100, 100, 50, 60, 40]
itemProfit = [5, 5, 3, 4, 2]
soldItems = [0, 0, 0, 0, 0]
profitItem = [0, 0, 0, 0, 0]
customers = 1

def processinput(inputList):
    # function for give the proccessed input
    numList1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    numList2 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    quantity = 0
    quantityList = [0, 0, 0, 0, 0]
    for word in inputList:
        if word in numList1:
            quantity = int(word)
        elif word in numList2:
            quantity = numList2.index(word) + 1
        elif word in items:
            quantityList[items.index(word)] = quantity
    return quantityList

def billing(custIn):
    bill = 0
    for i in range(len(custIn)):
        bill += custIn[i] * itemPrice[i]
    return bill

def updateStock(custIn):
    # updating stock
    for i in range(len(itemStock)):
        itemStock[i] -= custIn[i]

    # refilling stock if it reaches 20%
    for i in range(len(itemStock)):
        if itemStock[i] == itemStock[i] * 0.2:
            itemStock[i] = refillStock[i]

def updateSoldItems(custIn):
    for i in range(len(soldItems)):
        soldItems[i] += custIn[i]

def updateProfit(custIn):
    for i in range(len(itemProfit)):
        profitItem[i] += custIn[i] * itemProfit[i]

def printProfit(custIn,count):
    print("High Profit Items : ")
    enumProfit = list(enumerate(profitItem))
    enumProfit_Sort = sorted(enumProfit,key=lambda x:x[1],reverse=True)
    for i in enumProfit_Sort[0:count]:
        print(items[i[0]])

def printSold(custin,count):
    print("High sold Items : ")
    enumSold = list(enumerate(soldItems))
    enumSold_Sort = sorted(enumSold,key=lambda x:x[1],reverse=True)
    for i in enumSold_Sort[0:count]:
        print(items[i[0]])

while customers <= 5:
    # begin loop
    print("Customer no : " , customers)
    print("----- MENU CARD -----")
    for i in range(len(items)):
        print(f"{items[i]} : {itemPrice[i]}")  # to print the menu
    custIn = input("What would you like to order:").lower().split(" ")  # input of the customer
    custIn = processinput(custIn)
    print("Thanks for ordering ,  Enjoy your food")
    print("Your bill is :", billing(custIn))
    billing(custIn)
    updateStock(custIn)
    updateSoldItems(custIn)
    updateProfit(custIn)
    customers = customers + 1
    # end loop

print("Item sold")
for i in range(len(items)):
    print(f"{items[i]} sold : {soldItems[i]}")

print("Available stock")
for i in range(len(items)):
    print(f"{items[i]} available  : {itemStock[i]}")

count = 0
for i in soldItems:
    if not i == 0:
        count = count +1

printProfit(custIn,count)
printSold(custIn,count)