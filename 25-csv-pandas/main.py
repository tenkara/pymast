# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     # for row in data:
#     #     print(row)
    
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
data = pandas.read_csv("weather_data.csv")
print(sum(data["temp"].to_list())/len(data["temp"].to_list()))
print(data["temp"].mean())
print(data["temp"].max())

# Get data in columns
print(data["condition"])
print(data.condition)

# Get data in row
print(data[data.day == "Monday"])