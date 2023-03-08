# Ask the user to input 3 numbers. Ask the user if they want to find the max of these numbers or mininum.Find the answer and print.


num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
option = int(input("To  find maximum enter 1 , To find minimum enter 2 :"))

if(option == 1):
    if num1>num2 and num1>num3:
        print(num1 ," is the max number")
    elif num2>num1 and num2>num3:
        print(num2, " is the max number")
    else:
        print(num3, " is the max number")
else:
    if num1<num2 and num1<num3:
        print(num1 ," is the min number")
    elif num2<num1 and num2<num3:
        print(num2, " is the min number")
    else:
        print(num3, " is the min number")

