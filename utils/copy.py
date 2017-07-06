l1 = [1,2,3]

l2 = []
l2 = l1.copy()
print(l2)

l2 = l1[:]

#BETTER
for item in some_list:

#instead of
for item in range(len(some_list)):

for index, value in enumerate(some_list):
    print("Value of index {0} is {1}".format(index,value))

for a, b in zip(A, B): #A i B to jakies listy - iterowanie po dwoch listach
    print("A: {} B: {}".format(a, b))


#iterowanie po slowniku

dictionary = {"name" : "Bob", "last_name":"der Baumeister"}

for key, value in d.items():
    print("Value of index {} is {}".format(key, value)

#best way to open file
with open(some_file.txt) as f_in:
    x = f_in.read() #no need to close file