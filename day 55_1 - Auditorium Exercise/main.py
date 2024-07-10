inputs = eval(input())


# TODO: Create the logging_decorator() function 👇

def logging_decorator(func):
    def wrapper(*args):
        print(f"You called {func.__name__}{args}")
        result = func(args[0], args[1], args[2])
        print(f"It returned: {result}")

    return wrapper


# TODO: Use the decorator 👇
@logging_decorator
def a_function(a, b, c):
    return a * b * c


a_function(inputs[0], inputs[1], inputs[2])
