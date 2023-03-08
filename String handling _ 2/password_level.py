'''Print the level of the password security and if the password is acceptable
    Weak - only alphabets or only numbers or only special chars
    Ok - at least one alphabet, one number and one special char
    strong - at least three alphabets, two numbers and one special char
    Very strong - same as strong, but at least 16 count
    All passwords must be at least 8 chars long. You can use RegEx if you want '''

password = input("Enter you password:")  # getting password
alpha = 0  # to count alphabats
special = 0  # to count special
digit = 0  # to count digits
size = len(password)  # length of the password

if size < 8:    #check if size less than 8
    print("Not a vaild password. Your password should have minimum 8 characters")
else:
    for i in password:     
        if (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90):  #  ASCII alphabets ( 65 to 90 and 97 to 122)
            alpha = alpha + 1  # count increased if i  is alphabat
        elif ord(i) >= 48 and ord(i) <= 57:    #ASCII numbers (48 to 57)
            digit = digit + 1  # count increased if the i is  digit
        else:
            special = special + 1   # count increased if the i is special characters

    if size == alpha or size == digit or size == special: # check password is nly alphabets or only numbers or only special chars
        print("WEAK")
    elif alpha >= 3 and digit >= 2 and special >= 1:  #strong - at least three alphabets, two numbers and one special char
        if size >= 16:       #Very strong - same as strong, but at least 16 count
            print("VERY STRONG")
        else:
            print("STRONG")
    elif alpha >= 1 and digit >= 1 and special >= 1:  # Ok - at least one alphabet, one number and one special char
        print("OK")
