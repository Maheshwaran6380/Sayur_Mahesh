# 1. Calcualte and print users age - Write a program to ask the user for his/her name and print 'Hello', user's name. Ask what year they were born.  get the year from the user. Print 'You are <age> years old'.


name = input("Enter your name:")
print("Hello "+name)
year = int(input("Enter birth year:"))
current_year = int(input("Enter current year:"))
age = current_year - year
print("Yoy are "+ str(age) + "years old")