# Start with the above. The total cost is split equally by bride and groom.
# Bride has saved Rs50000. Determine if the bride has to take a loan or not. 
# If loan, how much?

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
cash_bride =Total_cost//2
if cash_bride < 50000 :
    print("No need to take loan")
else:
    print("need to take loan "+str((cash_bride-50000)))
