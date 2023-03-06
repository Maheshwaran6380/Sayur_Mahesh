fruit_list = ["mango", "apple", "banana"]
fruit_Inventory = [20, 30, 25]
fruit_min = [5, 10, 8]
reorder_list = [10,10,10]

def fruitindex(new_fruit_list , new_custInput):
    for i in range(len(new_fruit_list)):
        if new_fruit_list[i] == new_custInput:
            return i

def checkquantity(fruit_inventory , quantity , fruit_index):
    if fruit_inventory[fruit_index] >= quantity:
        return True
    else:
        return False

def checkminimum(fruit_min , fruit_inventory, fruit_index):
    if fruit_inventory[fruit_index] >= fruit_min[fruit_index]:
        return True
    else:
        return False

def reorder(fruit_inventory , reorder_list , fruit_index):
    fruit_inventory[fruit_index] += reorder_list[fruit_index]
    return fruit_inventory

customer_count = 1
while customer_count <= 5:
    custInput = input("What do you want ? : ")
    custInput = custInput.lower()
    fruit_index = fruitindex(fruit_list , custInput)
    quantity = int(input("How much do you want? :"))
    if checkquantity(fruit_Inventory,quantity,fruit_index):
        print("Your order is placed")
        fruit_Inventory[fruit_index] -= quantity
    else:
        print("not enough quantity")
    print(fruit_Inventory)
    if checkminimum(fruit_min,fruit_Inventory,fruit_index):
        pass
    else:
        fruit_Inventory = reorder(fruit_Inventory , reorder_list , fruit_index)

    customer_count +=1 