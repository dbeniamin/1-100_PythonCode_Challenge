# DICTIONARIES 
# {key : value , key : value, etc .}
# format the dictionary - open { -> indent -> each item  row start -> end with , 
# inside a dictionary => strings for keys

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# retrieve an item from a dictionary use [] and specifying what item you want to access
print(programming_dictionary["Bug"])

# adding an item to dictionary - dictionary name[" key to be added"] = "Value to be stored"
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# # create an empty dictionary 
# empty_dictionary = {}

# # wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# adit an item in a dictionary
# if the key is not in the dictionary - it will create a new key
programming_dictionary["Bug"] = "Editing this entry"

# loop through in a dictionary
# the below example just gives the keys
for thing in programming_dictionary:
    print(thing)

# the below example will print the keys called with 1-st print and value called with 2-nd print
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# EXERCISE NO. 1 - Grade scores

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

# Create an empty dictionary called student_grades.
student_grades = {}

# add the grades to student_grades
# creating a loop to acces the score
for student in student_scores:
    # create new variable and use the key to get the score
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "FAIL!"

print(student_grades)

# Nesting 
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Koln"]
}

# Nesting Dictionary in a Dictionary
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 4,
    },
    "Germany": ["Berlin", "Hamburg", "Koln"]
}

# Nestikng a Dictionary in a List 
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 4,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Koln"],
        "total_visits": 11,
    },
]

# EXERCISE NO. 2 -  Dictionary in a list
# provide and add country name
country = input("Please type the country ...\n")

# provide and add number of visits
visits = int(input("Please tell me how many times you visited ...\n"))
# create list from formatted string 
# cities need to be provided ["city a", "city b", "city c"] in order to be taken
list_of_cities = eval(input("Please list the cities you visited ...\n"))
print(list_of_cities)
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# function that will allow new countries to be added to the travel_log.
def add_new_country(name, times_visited, cities_visited):
    # creating an empty dictionary
    new_country = {}

    # assign values based on existing keys
    new_country["country"] = name
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited

    # use append to add to the existing dictionary
    travel_log.append(new_country)


# call the function to include newlly added item
add_new_country(country, visits, list_of_cities)

# print f string based on arguments provided
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
