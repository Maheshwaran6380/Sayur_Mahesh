""" Input is an encrypted  string where there will be chars followed by number. The way to decrypt is 
to repeat the chars, by the number of times. Print the decrypted word and its length. If there are any special 
chars, all the chars between the number and special char are ignored.
 eg - ac2bd3 means acacbdbdbd. 
 ac2acc#cd3 acaccdcdcd """

encrypt_str = input("Enter encrypted string:")
current_word = ""
new_word = ""
for i in encrypt_str:  # travarse each letter of the encrypted string
    if i.isalpha():  # check the current  letter in digit or not
        new_word = new_word + i
    elif i.isdigit():
        current_word = current_word + (
            new_word * (int(i))
        )  # if the letter in digit , then multiply the newword
        new_word = ""  # clear the new_word
    else:
        new_word = ""
print(current_word)
print(f"Length : {len(current_word)}")
