# Calculate wedding expenses. Cost for lunch per person is Rs200. Cost for Breakfast per person is half of lunch cost. Cost of the hall is Rs 200 per person.  Decoration is 50% of Hall cost. Parking is 10% of the Hall cost. 
# Decide what should be the input and calculate the cost. 

persons = int(input("How many members attend the wedding "))
lunch_per_head = 200
breakfast_per_head = 100
hall_per_head = 200
decoration = 100
parking = 20
lunch_tot = persons * lunch_per_head
breakfast_tot = persons * breakfast_per_head
hall_tot = persons * hall_per_head
parking_tot = persons * parking
Total_cost = lunch_tot + breakfast_tot + hall_tot + parking_tot + decoration
print("Total cost is :" + str(Total_cost))
