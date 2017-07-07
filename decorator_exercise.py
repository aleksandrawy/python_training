
def tags(tag):
    def inner_decorator(func):

        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"<{tag}>{result}</{tag}>"

        return wrapper

    return inner_decorator


@tags("body")
@tags("div")

def core_string(name):
    return f"Hello {name}"


print(core_string("Ola"))