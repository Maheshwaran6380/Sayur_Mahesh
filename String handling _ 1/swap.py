# Write a program that will swap two numbers.

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
print("Before swapping num1 : ",num1," num2 : ",num2)
temp = num1
num1 = num2
num2 = temp
print("After swapping num1 : ",num1," num2 : ",num2)