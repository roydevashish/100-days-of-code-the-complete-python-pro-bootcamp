# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))

#     print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")
# temp_list = data.temp
# print(temp_list.mean())

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * (9/5) + 32
# print(monday_temp_F)

# Create a DataFrame
# data_dict = {
#     "students": ["A", "B", "C"],
#     "scores": [8, 10, 15]
# }

# data_frame = pandas.DataFrame(data_dict)
# DataFrame to csv and save.
# data_frame.to_csv("new_data.csv")



# The Great Squirrel Census Data Analysis (with Pandas!)
data = pandas.read_csv("Squirrel_Data.csv")
primary_fur_color_column = data["Primary Fur Color"]
gray_count = len(primary_fur_color_column[primary_fur_color_column == "Gray"])
cinnamon_count = len(primary_fur_color_column[primary_fur_color_column == "Cinnamon"])
black_count = len(primary_fur_color_column[primary_fur_color_column == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "count": [gray_count, cinnamon_count, black_count]
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("Squirrel_Count.csv")