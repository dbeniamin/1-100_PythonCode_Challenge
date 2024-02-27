### List Comprehension ##

import random


# creeate a new list #
numbers = [1, 2, 3]

# Classic Way #
new_list = []
for n in numbers:
    add_1 = n + 1

new_list.append(add_1)
final_list = numbers + new_list

# list comprehenstion way #
new_list = [n + 1 for n in numbers]

print(final_list)

# can be used to split a list using the comprehension method #
name = "Angela"
letters_list = [letter for letter in name]
print(letters_list)

### Apply list comprehension to a range ###
# long version
# creeate a list from a range #
# than pass that list and apply comprehension to get the values doubled
practice_test = list(range(1, 5))
update_practice_test = [n * 2 for n in practice_test]
print(update_practice_test)

# short version
range_list = [num * 2 for num in range(1, 5)]


### Conditional list Comprehension ###

#  example pattern --> new_list = [new_item for item in list if test] <--

# "if" the test passes "only than" the new item will be creeated in the list and added

names_list = ["Benjamin", "Cezar", "Calin", "Adrian", "Kris", "Cipri"]
short_names = [name for name in names_list if len(name) < 5]
print(short_names)

# Challange - New list that contains the names longer than 5 characters in ALL CAPS
# to make it all caps just add .upper() attribute to the name parameter to be saved in the new list
caps_names = [name.upper() for name in names_list if len(name) > 5]
print(caps_names)


## Auditorium Exercise No. 1 ###
# squaring the numbers in the list using list comprehension

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

# Write your 1 line code 👇 below:
squared_numbers = [(n * n) for n in numbers]
# Write your code 👆 above:

print(squared_numbers)


## Auditorium Exercise No. 2 - Filtering even numbers

list_of_strings = input().split(',')

# 🚨 Do  not change the code above
# TODO: Use list comprehension to convert the strings to integers 👇:
result_ints = [int(test_input) for test_input in list_of_strings]
# TODO: Use list comprehension to filter out the odd numbers
# and store the even numbers in a list called "result"
# you can get the odd numbers by using "element name % 2 == 0 " as condition in list comprehension
results = [even_num for even_num in result_ints if even_num % 2 == 0]
# Write your code 👆 above:

print(results)


### Auditorium Exercise No. 3 - Data overlap
### different solution than the one presented in the course ###
### passed Auditorium tests with the code below ###
# open the files
with open("day26_file1.txt") as file_1:
    # save the content
    contents_file_1 = file_1.readlines()
    # strip the new lines \n and convert the items to integers
    file_1_strip = [int(item.strip()) for item in contents_file_1]
    # print for debugg purposes
    print(file_1_strip)

with open("day26_file2.txt") as file_2:
    contents_file_2 = file_2.readlines()
    file_2_strip = [int(item.strip()) for item in contents_file_2]
    print(file_2_strip)
# compare the 2 lists using comprehension and passing the pressence of number in the 2nd file as a condition
result = [test_number for test_number in file_1_strip if test_number in file_2_strip]

# Write your code above 👆
print(result)

## Dictionary Comprehension ###
# Comprehension works with dictionaries as well by using the below code
#
# example for creating new dict from scratch #
# ->  new_dic = {new_key:new_value for item in list}  <-
#
# example for creating new dict based on existing dict
# -> new_dict = {new_key:new_value for (key, value) in dict.items()} <-

# example for creating new dict based on existing dict and a condition
# -> new_dict = {new_key:new_value for (key, value) in dict.items() if test} <-

# import random ## import statement for separate script running

names_list = ["Benjamin", "Cezar", "Calin", "Adrian", "Kris", "Cipri"]
student_scores = {student: random.randint(1, 100) for student in names_list}
print(student_scores)
passed_scores = {name: score for (name, score) in student_scores.items() if score >= 60}
print(passed_scores)


## Auditorium Dict Comprehension - Exercise No. 1 ###
# any sentence you input in the console

sentence = input()
# 🚨 Don't change code above 👆
# Write your code below 👇

dict_sentence = sentence.split()
print(dict_sentence)   # debbug / intermediate testing purpose only
result = {word: len(word) for word in dict_sentence}

print(result)


## Auditorium Dict Comprehension - Exercise No. 2 ###

weather_c = eval(input())
# test input: {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22,}
# 🚨 Don't change code above 👆
# Write your code 👇 below:

weather_f = {day: (temp_c * 9 / 5 + 32) for (day, temp_c) in weather_c.items()}
# temp_f = (temp_c * 9 / 5) + 32  -> formula to transform Celsius to Farenheit

print(weather_f)

import pandas


student_dicts = {
    "student": ["Benjamin", "Kris", "Cezar", "Adrian"],
    "score": [66, 55, 77, 88]
}
student_data_frame = pandas.DataFrame(student_dicts)
print(student_data_frame)

# ## Loop through a data frame - clasic method
# for (key, value) in student_data_frame.items():
#     print(value)

## Loop through rows of a data frame -> use pandas build in function of .itterows()
# than each row cand be accessed by using row.student/score in this case
for (index, row) in student_data_frame.iterrows():
    if row.student == "Benjamin":
        print(row.score)
