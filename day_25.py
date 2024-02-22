### CSV file manipulation with Python ###

# traditional way of opening and listing a content of the csv - hard to use
with open("weather_data.csv") as test_data:
    weather_data = test_data.readlines()
    print(weather_data)

# separating temp column from the file using just csv
import csv
with open("weather_data.csv") as test_file:
    data = csv.reader(test_file)
    temperatures = []
    for row in data:
        print(row)
        if row[1] != "temp":
            temperatures.append(row[1])
    print(temperatures)

### https://pandas.pydata.org/docs/ ###
### https://pandas.pydata.org/docs/getting_started/index.html#getting-started ###
import pandas
data = pandas.read_csv("weather_data.csv")
# adding the column name from the file you read will show only that column i.e. ["day"] , ["temp"], ["condition"]
# print(type(data["day"]))

# conversion to a dictionary
data_dict = data.to_dict()
print(data_dict)

# taking a specific column and turning in to a list
temp_list = data["temp"].to_list()

### https://pandas.pydata.org/docs/reference/series.html ###
# use .mean to calculate the average value of the series
# use .max to get the max value for the specific column

average = data["temp"].mean()
max_value = data["temp"].max()
print(average, max_value)

# you can get hold of a specific column by passing that column name to the read file
print(data.day)

# get specific data in the Row
# print(data[data.day == "Monday"])

# personal solution to ge the row with the max value temp
print(data[data.temp == max_value])


print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]

# converting from Celsius to Fahrenheit
monday_temp_F = monday_temp * 9/5 + 32




