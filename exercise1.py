import random


with open('numbers.txt', 'w') as n_out:
    for i in range(10):
        n_out.write(str(random.randint(1,10)) + "\n")

with open('numbers.txt', 'r') as n_in, open('done.txt', 'w') as n_out:
    for line in n_in:
        n_out.write("X" * int(line) + "\n")
