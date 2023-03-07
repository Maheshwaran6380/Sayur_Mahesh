""" 1. Write an app for a cafe. Decide on the items in the cafe, stock of each item in the morning, 
stock in the evening, sales amount at the end of the day and profit for each item. You need to restock an item 
if the supply reaches 20% of the stock. Print the 3 items with highest sales, and top 3 highest profit."""

items = ["coffee", "cookies", "tea", "donuts", "icecreams"]
itemPrice = [15, 10, 15, 20, 20]
itemStocks = [100, 50, 100, 40, 30]
refillitem = [100,50,100,40,30]
itemSale = [0,0,0,0,0]
itemProfit = [3, 2, 3, 5, 4]
eachitemprofit = [0,0,0,0,0]


def process(list1):
        numberList1 = ["1","2","3","4","5","6","7","8","9"]
        numberList2 = ["one","two","three","four","five","six","seven","eight","nine"]
        quantity = 0
        quantityList = [0,0,0,0,0]
        for i in list1:
                if i in numberList1:
                        quantity = int(i)
                elif i in numberList2:
                        quantity = numberList2.index(i) + 1
                elif i in items:
                        indexitem = items.index(i)
                        quantityList[indexitem] = quantity
        return quantityList

def refillstock():
       for i in range(len(itemStocks)):
            if itemStocks[i] == itemStocks[i]*0.2:
                   itemStocks[i] = refillitem[i]

def findmax(li):
    return li.index(max(li))

print("------MENU CARD------")
for j in range(len(items)):
        print(f"{items[j]} : {itemPrice[j]}rs")

customers = 1
yourbill=0

while customers <= 5:
    print(f"\n Customer no:{customers}")
    customerInput = input("What would you like to order ? ").lower().split(" ")
    customerInput = process(customerInput)
    for i in range(len(itemStocks)):
        itemStocks[i] -= customerInput[i]
        itemSale[i]+=customerInput[i]
    refillstock()
    customers += 1

print("\nITEMS SOLD...")
for i in range(len(itemSale)):
    if not itemSale[i]==0:
        print(f"{items[i]} sold : {itemSale[i]}")
    eachitemprofit[i] = itemSale[i] * itemProfit[i]     #profit calculation

print("\nAvailable stock...")
for i in range(len(itemSale)):
        print(f"{items[i]} sold : {itemStocks[i]}")

print("\nTop 3 highest profit : ")
for i in range(3):
    a = findmax(eachitemprofit)
    print(items[a])
    eachitemprofit[a]=0

print("\nTop 3 highest sales : ")
for i in range(3):
    a = findmax(itemSale)
    print(items[a])
    itemSale[a]=0