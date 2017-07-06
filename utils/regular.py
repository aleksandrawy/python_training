import re

message = "File saved at 17:23:57"

pattern = "\d\d:\d\d:\d\d"

m = re.search(pattern, message)

if m:
    print(m.group())

message1 = "My e-mail is jan.kowalski@gmail.commmmm"

pattern1 = "[a-z.]+@[a-z\.]+\.[a-z]{1,3}"

m1 = re.search(pattern1, message1)
#ALT+ENTER -> Check regex

if m1:
    print(m1.group())

#message2 = "rngowsgeseog2829djfnsdksd"

#pattern2 = "[\d]+\$"

#m2 = re.search("\d+\$", message2)

#if m2:
#    print(m2.group())