# Same as above, but the price of Onion is different based on the city. Chennai - Rs30, Trichy Rs27, Madurai Rs 34. Input is budget and city.

budget =float(input("Enter the budget:"))
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
