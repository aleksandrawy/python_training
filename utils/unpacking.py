l = [1,2,3]

a1, b1, c1 = l

kw = {"a1": 23, "b1": 24, "c1": 25}

def func(a1, b1, c1):
    print(f"First arg {a1}")
    print(f"Second arg {b1}")
    print(f"Thirs arg {c1}")

func(*l)   #rozpakowanie listu/tupla
func(**kw) #slownika (podwojne gwiazdki)

#------------------------------------------------
def f(i, j, k):
    print("Got three arguments, {}, {}, {}".format(i, j, k))

x = (1, 2, 3)

a, b, c = x  # using unpacking on assignment

f(*x)  # unpack the list x into positional arguments of f

# -> Got three arguments, 1, 2, 3

keyword_arguments = {"i": 10, "j": 20, "k":30}

f(**keyword_arguments)  # unpack the dict into the fuction arguments

# -> Got three arguments, 10, 20, 30

#----------------------------

#DON'T DO THAT!

f = lambda a, b: a + b

#it's equal to

def f(a,b):
    return a+b