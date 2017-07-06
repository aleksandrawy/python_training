some_string = ''

if some_string:
    print('The string is not empty')

#-----------------

x = 1
y = []
x or y  # returns 1
x and y # returns []
y or x # returns 1

#-----------------

def get_full_name(name, default="Gonzales"):
    first_name = "Juan"
    last_name = name or default

    return f"{first_name} {last_name}"


print(get_full_name(None))

#------------------

default_list = [1, 2, 3, 4, 5]

some_other_list = []

new_list = some_other_list or default_list

print(new_list is default_list) # -> True