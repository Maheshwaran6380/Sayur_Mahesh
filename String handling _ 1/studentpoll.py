# Take an opinion poll among students. Ask the students whether they like online class
#  (input as 1), in person class (input as 2) or mixed (input as 3).
#  Display the percentage of the female students that like online classes.
#   You can end the poll when someone answers ‘No comment (input as 4)’ or when the poll 
#   reaches at least 10 students.


print("1 . If you like online class")
print("2 . If you like in person class ")
print("3 . If you like mixed class ")
count = 0
total_count=0
i=1
while i<=10:
    gender = input("Enter your gender  m or f : ")
    option = int(input("Enter your option:"))
    total_count = total_count+1
    if gender=='f' and option==1:
        count=count+1
    if option==4:
        break
percentage = (count/100)*total_count
print(str(percentage)+"%")

