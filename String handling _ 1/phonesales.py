# Write an app for a phone sales man. The Salesman earns Rs10000 every month.
# He earns Rs1000 commission for every phone he sells. If he sells more than 5 phones a month,he earns extra Rs100 per phone (1000+100). If he sells 10 phones or more, he gets extra Rs 200 for each phone over 10. He can only earn max 25000 per month.
# Calculate his monthly salary and avg salary per month in one year. 

salary = 10000
sold = int(input("No of mobiles he selled per month:"))
commission = 1000
for i in range(1,sold+1):
    if(i<=5):
        salary = salary+commission
    elif i>5 and i<=10:
        salary = salary + (commission + 100)
    elif i>10:
        salary = salary + (commission + 200)
print(salary)
