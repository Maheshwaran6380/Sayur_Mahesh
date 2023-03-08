# Same as above, but add 3% of the budget for petrol expenses.

budget =float(input("Enter the budget:"))
budget = (30/100)*budget
city = input("Enter city:")
if city == "chennai":
    onion = 30
elif city == "trichy":
    onion = 27
elif city == "madurai":
    onion = 34
else:
    onion = 20
tomato = 10.5
buy_onion = budget // onion
buy_tomato =  budget // tomato
print(buy_onion)
print(buy_tomato)

