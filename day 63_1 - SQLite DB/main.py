import sqlite3

# creeate a connection to a database
# if the file does not exist run main.py to auto creeate it
db = sqlite3.connect("books-collection.db")

# creeate cursor to interact with the db
cursor = db.cursor()

# CREATE TABLE -  This will create a new table in the database. The name of the table comes after this keyword.
# books -  This is the name that we've given the new table we're creating.
# () - The parts that come inside the parenthesis after CREATE TABLE books ( ) are going to be the fields in this table.


# -> id INTEGER PRIMARY KEY -  This is the first field, it's a field called "id" which is of data type INTEGER, and it
# will be the PRIMARY KEY for this table. The primary key is the one piece of data that will uniquely identify this
# record in the table.

# -> title varchar(250) NOT NULL UNIQUE -  This is the second field, it's called "title" and it accepts a
# variable-length string composed of characters. The 250 in brackets is the maximum length of the text. NOT NULL
# means it must have a value and cannot be left empty. UNIQUE means no two records in this table can have the same
# title.

# -> author varchar(250) NOT NULL -  A field that accepts variable-length Strings up to 250 characters called author
# that cannot be left empty.

# -> rating FLOAT NOT NULL -  A field that accepts FLOAT data type numbers, cannot be empty and the field is called
# rating.


#  --- https://www.codecademy.com/article/sql-commands ---
# --- https://sqlitebrowser.org/dl/ ---

# creeating database with abow mentions -- Comment after the db is created - else you will get an error

# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) "
#                "NOT NULL, rating FLOAT NOT NULL)")

# adding items to database - based on structure table set up

cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()

#   SQL queries are very sensitive to typos   !!!!!

# we can use a tool called SQLAlchemy to write Python code instead of all these error-prone SQL commands. #
