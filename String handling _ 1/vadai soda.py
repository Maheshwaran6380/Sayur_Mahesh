'''The user just bought a few things in your  shop. Ask the user what he bought. 
Cost of one vadai is Rs 30, one soda is Rs20 and one sandwich is Rs 100. Calculate the total cost.
Ask the user to pay the amount. Receive the amount from the user (get money as input). 
Print the change amount you have to give to the user. 
Hint - use float datatype'''


vadai_quant = int(input("Enter quantity of vadai:"))
soda_quant = int(input("Enter quantity of vadai:"))
sandwich_quant = int(input("Enter quantity of vadai:"))
total = float( (vadai_quant * 30) + (soda_quant * 20) + (sandwich_quant * 100))
print("Total cost is:", total)
amount = int(input("Pay your bill:"))
bal = float(amount - total)
print("Balance is :",bal)
