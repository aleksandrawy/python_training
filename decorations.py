from selenium.common.exceptions import WebDriverException


def gui_interaction(func):

    def wrapper(*args, **kwargs):
        print("Gui interaction starts")
        exception = None
        for i in range(3):
            try:
                result = func(*args, **kwargs)
                print("Gui interaction done")
                return result
            except WebDriverException as e:
                exception = e
                pass
        else:
            if exception:
                raise exception

    return wrapper


@gui_interaction
def click_some_element():
    print("I try to click element")


click_some_element()