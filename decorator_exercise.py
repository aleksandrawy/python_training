from functools import wraps #importujemy dekorator


def tags(tag):   #zjawisko clousure (?)
    def inner_decorator(func):  #tu trafia core_string

        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)  #sprawia ze dekorator jest uniwersalny
            return f"<{tag}>{result}</{tag}>"

        return wrapper

    return inner_decorator


@tags("body")
@tags("div")  #zwraca obiekt (nie jest dekoratorem - funkcja ktora go zwroci)

def core_string(name, firstname):
    return f"Hello {firstname} {name}"


print(core_string("Ola", "Siemanko"))