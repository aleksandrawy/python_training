class Animal():
    def __init__(self, name, make_sound_method):
        self.name = name
        self.make_sound = make_sound_method


def quack():
    print('Quack!')


def moo():
    print('Moooo!')


def bah():
    print('Bah!')


bah = Animal(name='Sheep', make_sound_method=moo)

bah.make_sound()

#---------------------

def some_function():
    return "Hello"


hello = some_function()
hello_func = some_function

print(hello)
# -> Hello

print(hello_func)
# -> <function some_function at 0x01290DF8>

print(hello_func())
# -> Hello

#----------------------

def wait_until(condition, timeout=10, raise_exception=True, msg=""):
    """Wait until the condition returned by 'condition' function is fulfilled,
    or the timeout is expired. The condition should be checked every 100ms

    Args:
        condition: a function that checks a condition and returns True or False
        timeout: maximal timeout after which the function will raise TimeoutException
                or return False (if raise_exception is False)
        msg: message added to the TimeoutException
    Returns:
        True when the condition is fulfilled within the timeout,
        False when the condition is not fulfilled within the timeout
                and 'raise_exception' is False
    Raises:
        TimeoutException: if raise_exception is True
                        and the condition is not fulfilled within timeout

    """

