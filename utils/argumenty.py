def print_arguments(*args, **kwargs):
    print("Positional arguments")
    for arg in args:
        print(arg)

    print("Keyword arguments")
    for kwarg, value in kwargs.items():
        print("{} = {}".format(kwarg, value))


print_arguments(1, 2, x=12, y=14, z=['a', 'b', 'c'])