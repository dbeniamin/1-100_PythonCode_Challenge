# File manipulation with PYTHON

# make a .txt file in the same folder as the python file that you are working on
# name of the file will be used to be accessed and used

### not specifying the mode will pick the default - read only open mode ##

with open("filename.txt") as file:
    # name given can be any preferred choice of the programmer
    # use with method to make sure the file is closed once we are done working with it
    # read method to extract the contests of the file
    contents = file.read()
    print(contents)

### opening file mode types ###
# default "r" - read only
# "w" - write mode - will delete previous saved information in that file
# "a" - append mode - add information to the previous saved one.

with open("filename.txt", mode="a") as file:
    file.write("\n testing adding new text")

# opening a file that does not exist in "w" mode will create it from scratch.
with open("filename.txt", mode="w") as file:
    file.write("testing creating a new file")

# ./ -> look in the current folder for the specified file
# ../ -> go one folder up or behind to the parent folder
# / -> marks the root location C: = / in a path so "C:\Users\beniamin.drimus" becomes ->  "/Users/beniamin.drimus"


# using absolute path to open a file - will always start from the root
with open("/Users/username/Desktop/filename.txt") as file:
    contents = file.read()
    print(contents)

# using relative path to open a file - will always start from the current working directory
with open("../../Users/username/Desktop/filename.txt") as file:
    contents = file.read()
    print(contents)
