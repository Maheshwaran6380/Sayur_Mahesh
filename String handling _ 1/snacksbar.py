# Write an app to calculate the total bill at the Snack bar. The price of coffee is Rs 100, Vadai (1) is Rs100,
#    Sandwich is Rs 200, Coke Rs 60. If the customer buys more than one sandwich or two or more vadai, 
#    the price of one coffee  is Rs 50. 
#    If the customer buys one of each item, then there is discount of 20% of the total. No further discounts after the 20% discount.
#    If the total price of the bill (before any discount) is more than Rs1000, then also there is a 20% discount.


coffee = 100
vadai= 100
sandwich = 200
coke = 60

coffee_buy = int(input("How many coffee you bought : "))
vadai_buy = int(input("How many vadai you bought : "))
sandwich_buy = int(input("How many sandwich you bought : "))
coke_buy = int(input("How many coke you bought : "))

if  sandwich_buy >1 or vadai_buy >=2:
    coffee = 50

total = (coffee*coffee_buy) + (vadai * vadai_buy) + (sandwich * sandwich_buy)+(coke * coke_buy)

if sandwich_buy>=1 and vadai_buy >=1 and coke_buy >=1 and coffee_buy >= 1 or total>1000:

    total = total - (0.2 * total)

print("total is " ,total)   
