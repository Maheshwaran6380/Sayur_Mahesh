# Write a program to calculate the milege. Ask the user how many litres of petrol they have. 
# Ask how many km they have to drive. Calcualte the milege. If the mileage is more than 30km per litre, tell the user they have to fill the tank again.


petrol = float(input("Enter the liters of petrol filled "))
distance = float(input("Enter the distance travelled by user:"))
milage = distance / petrol
print("Milage is ",milage,"km per liter")
if(milage >= 30):
    print("You have to fill the tank again")
else:
    print("Petrol is enough")

