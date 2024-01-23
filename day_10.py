# # Functions with inputs
# def my_function(something)
#     do this with something
#     than do this
#     fianll do this 


# # Functions with Outputs
# def my_function():
#     result = 3 * 2
#     return


# .title() - will capitalize the first letter of the string

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name(input("What is your Fist name?"), input("What is your last name")))
format_name("BeNjAmIN", "ART")


# EXERCISE No. 01

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap(year):
        return 29
    else:
        return month_days[month - 1]


# 🚨 Do NOT change any of the code below
year = int(input())  # Enter a year
month = int(input())  # Enter a month
days = days_in_month(year, month)
print(days)


# Docstring
def my_function():
    # first line in the definition of the function
    """documentation string"""
