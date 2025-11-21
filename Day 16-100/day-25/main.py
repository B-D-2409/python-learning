# with open("weather_data.csv") as data_file:
#     data = data_file.readline()
#     print(data)
#
#
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         print(row[1])
#
#
#

import pandas


data = pandas.read_csv("weather_data.csv")
#
# print(data["temp"])

data_dict = data.to_dict()
# print(data_dict)
#
#
# temp_list = data["temp"].to_list()
#
# print(temp_list)


# average = sum(temp_list) / len(temp_list)
# print(average)


# print(data['temp'].mean())
# print(data['temp'].max())
#
#
# print(data["condition"])
#
# print(data.condition)
#
# print(data[data.day == 'Monday'])
#
# print(data.temp == data.temp.max())
#
#
# monday = data[data.day == 'Monday']
# print(monday.condition)
#
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)
#



#Create Data Frame
data_dict = {
    "students": ["Any", "James","Angela"],
    "scores": [76,56,65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")