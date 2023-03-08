# Program to find out how many Kg of onion or tomato we can buy. One Kg of Onion is 20rs, Tomato is 10.5rs.  Input is the budget.

onion = 20.0
tomato = 10.5
budget =float(input("Enter the budget:"))
buy_onion = budget // onion
buy_tomato =  budget // tomato
print(buy_onion)
print(buy_tomato)