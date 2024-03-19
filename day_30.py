# FileNotFound
# with open("file_test.txt") as file:
#     file.read()

# KeyError
# a_dict = {"key": "value"}
# value = a_dict["non_existent_key"]

# IndexError
# fruit_list = ["Apple", "Banana"]
# fruit = fruit_list[3]

# TypeError
# text ="abc"
# print(text + 5)

# Handling exceptions

# try:
#     code to try to be executed

# except:
#     execute if there is an exception

# else:
#     do this if there are no exceptions

# finally:
#     do this no matter what happens prior


try:
    file = open("day30_file_test.txt")
    a_dict = {"key": "value"}
    print(a_dict["etc"])
# except blocks need to be specific to avoid to broad definition of except block
except FileNotFoundError:
    open("day30_file_test.txt", "w")
    file.write("Testings")

except KeyError as error_message:
    print(f"The key {error_message} does not exist")

else:
    content = file.read()
    print(content)

finally:
    raise KeyError

height = float(input("Height:   "))
weight = int(input("Weight:   "))

if height == type(float):
    raise ValueError("Please insert a propper height !")

bmi = weight / height ** 2
print(bmi)

# ## -------------- Auditorium Exercise NO. 1 -------------- ###
fruits = eval(input())

test_input = ["Apple", "Pear", "Orange"]


# 🚨 Do not change the code above
# TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]

    except IndexError:
        print("Fruit pie")

    else:
        print(fruit + " pie")


make_pie(4)

#  🚨 Do not change the code below
make_pie(4)

### -------------- Auditorium Exercise NO. 1 -------------- ###

# test_input =  [{'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Likes': 33, 'Comments':
# 8, 'Shares': 3}, {'Comments': 4, 'Shares': 2},{'Comments': 1, 'Shares': 1}, {'Likes': 19, 'Comments': 3}]

# eval() function will create a list of dictionaries using the input
facebook_posts = eval(input())

total_likes = 0
# TODO: Catch the KeyError exception
for post in facebook_posts:
    # try block on the line with the issue
    try:
        total_likes = total_likes + post['Likes']
    # KeyError - pass the error in an except block, just pass, so it will move to the next element in the list of dicts
    except KeyError:
        pass

print(total_likes)
