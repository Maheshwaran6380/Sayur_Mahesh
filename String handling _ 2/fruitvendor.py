'''
3. Write an app for the input vendor. input vendor has a list of inputs (apple, Orange, banana etc).
When the customer comes in, vendor asks "What do you want to buy?" .
The customer can say "I want apple", or "Apple" or "three apple" or something like that.
Your program will find out what input the customer is asking. 
Your program will also find, if the customer already asked for the quantity of the input (one apple or 5 orange etc).
Print the quantity if the customer says the quantity. If not, ask him how much he wants.
Hint : Use string manipulation and lists. https://www.w3schools.com/python/python_ref_string.asp 
You can limit the quantity to single digit number. '''

listOfFruits = ['apple','orange','banana']

userInput = input("What do you want to buy? ")
userInput = userInput.lower()
QuantityList = ['one','two','three','four','five','six','seven','eight','nine'
                '1','2','3','4','5','6','7','8','9']
userWords = userInput.split()
quantity=0
fruitName=0
fruitName1=''
quantity1 = ""
# checks if the input is in the list
for i in range (len(userWords)):
    if userWords[i] in listOfFruits:
        #print(f"The customer is asking {input}.")
        fruitName = fruitName1 + userWords[i]
        print(fruitName)

    if userWords[i] in QuantityList :
        quantity = userWords[i]
        print(quantity) 

if quantity == 0:
    quantity = input("enter the quantity ")
    quantity = quantity+quantity1
  
if fruitName in listOfFruits:
    print(f'You have ordered {quantity} of {fruitName}')
else :
    print('You have ordered something not in our shop')