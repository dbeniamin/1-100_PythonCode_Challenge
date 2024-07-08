# # Auditorium Exercise No. 35 - day 54
import time


# current_time = time.time()
# print(current_time)  # seconds since Jan 1st, 1970


# Write your code below 👇

# define speed calc decorator
def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time - start_time}s")

    return wrapper_function


# number of iterations from the range decides if the func is slow or fast
# the fast func has 12345678 iterations and slow func has 123456789 iterations
# changed the i * i from the auditorium to have a var assigned due to PEP 8 rules
@speed_calc_decorator
def fast_function():
    result = 0
    for i in range(12345678):
        result += i * i


@speed_calc_decorator
def slow_function():
    result = 0
    for i in range(123456789):
        result += i * i


fast_function()
slow_function()
