import pandas

data = pandas.read_csv("Central_Park_Squirrel_Census.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}
# initialize data frame from pandas to turn the dictionary in to a Data Frame
df = pandas.DataFrame(data_dict)

# converting to csv and create a new file with the given name
df.to_csv("updated_count.csv")
