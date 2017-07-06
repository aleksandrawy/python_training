import re


class Pattern():
    def __init__(self, format_type):
        self.choose_format = format_type

def timePattern():
    return "\d\d:\d\d:\d\d"


def emailPattern():
    return "[a-z.]+@[a-z\.]+\.[a-z]{1,3}"




time = Pattern(format_type = timePattern)
time = time.choose_format()

email = Pattern(format_type = emailPattern)
email = email.choose_format()

m1 = re.search(time, "File saved at 17:23:57")
m2 = re.search(email, "Email: jan.kowalski@gmail.com")

if m1:
    print(m1.group())

if m2:
    print(m2.group())
