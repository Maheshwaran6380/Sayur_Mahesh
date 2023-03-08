''' 7. Same as above, but the pattern can be multi line.
Eg 
Message - "I Love India".
Pattern - 
'This is 
          a 
             Test'
Output  -
'ILov eI 
          n
             diaI' '''


msg = "I love India"
pat = "This is \n\t a\n\t   test"
pattern = pat.split("\n")  # ['This is ', '\t a', '\t   test']
track = 0
msg = msg.replace(" ", "")
length = len(msg) - 1
for i in pattern:
    for j in i:
        if j == " ":
            print(" ", end="")
        elif j=="\t":
            print("\t")
        else:
            print(msg[track], end="")
            track = track + 1
        if track > length:
            track = 0