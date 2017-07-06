import sys


def stringi1():
    name = "Bob"
    age = 23
    hobbies = ['Python', 'Programming', 'Tomb Rider']

    string_template = "My name is {}. I am {} years old. My hobbies are {}"
    output_string = string_template.format(name, age, hobbies)
    print (output_string)


def stringi2():
    introduction = "My name is {0}, I'm {1} years old. {0} is a nice name".format("Bob",23)
    vers = "Hello {name}. This is Python {version}".format(name="Bob", version=sys.version)
    print(introduction)
    print(vers)


def stringi3(): #tylko python 3.6!!!
    name = "Bob"
    age = 23
    hobbies = ['Python', 'Programming', 'Tomb Rider']

    f_string =f"My name is {name}, I am {age} years old. My hobbies are {hobbies}"

    print(f_string)


def main():
    print("Main")
    str1 = "Hello Academy"
    #str2 =
    stringi1()
    stringi2()
    stringi3()


if __name__ == "__main__":
    main()