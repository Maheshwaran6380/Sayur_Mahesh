def fun(sent):
      newstr=''
      newstr+=sent[0]
      newstr+=sent[2]
      newstr+=sent[-3:]
      return newstr


mail = "maheshjik@gmail.org"
password="mhjik123"
if "@" not in mail:
    print("incorrect username. put @ symbol")
    exit()
if (not mail.endswith(".com") and not mail.endswith(".edu") and not mail.endswith(".tech") and not mail.endswith(".org")):
        print(f"Incorrect username.put .com etc..")
        exit()
username = mail.split("@")
username = username[0]   
process_pass = ''
for i in password:
    if i.isdigit():
        break;
    else:
        process_pass += i
last = "".join(password[-3:])
process_name = fun(username)
if process_pass == process_name:
     if last.isdigit():
          print("Correct password")
else:
     print("Incorrect password")