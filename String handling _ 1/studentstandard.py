'''Calcualte and print which standard the student is studying - Write a program to ask the user for his/her name and print 'Hello', user's name. 
Ask what year they were born.  get the year from the user. 
Calculate if the user is going to elementary school, middle school, highschool or college.
(hint - use if/elif) '''


name = input("Enter your name:")
print("Hello "+name)
year = int(input("Enter birth year:"))
age = 2023 - year
if age>=6 and age<=10:
    print("Elimentry school")
elif age>=11 and age<=15:
    print("Middle school")
elif age>=16 and age<18:
    print("high school")
else:
    print("College")
