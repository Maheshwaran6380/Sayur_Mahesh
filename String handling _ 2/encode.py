"""  Encoding problem - Input is a message and  a pattern. Both strings. Output is the message written in the form
of the pattern. 
Eg -  Message - "I Love India".
      Pattern - "*** **** ** **********     *****"
      Output  - "ILo veIn di aILoveIndi     aILov"		"""


msg = "I Love India"
pat = "*** **** ** **********     *****"
# remove the whitespace of the message
msg = msg.replace(" ", "")
# tracking variale to print the letters of the message
track = 0
# index range of the message
length = len(msg) - 1
for i in pat:  # traverse each letter in the pattern
    if i == "*":  # check if the letter is *, then
        print(msg[track], end="")  # print the letter of msg, using track variable
        track =  track + 1 # increament the track variable to , move to the next word of message
    else:  # if the letter is not a * ,then
        print(" ", end="")  # print whitespace
    if track > length:  
        track = 0  # this will help us to , print the first letter after printing last letter.