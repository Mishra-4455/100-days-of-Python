# with open("weather_data.csv", mode= "r") as file:
#     data = file.readlines()
#     for set in data:
#         full_data = set.strip().split(",")
#         cvs.append(full_data)
# print(cvs)

# import csv
# with open("weather_data.csv", mode= "r") as file:
#     data = csv.reader(file)
#     tempratures = []
#     for row in data:
#         if row[1] == "temp":
#             pass
#         else:
#             tempratures.append(int(row[1]))

#     print(tempratures)

import pandas
data = pandas.read_csv("weather_data.csv")

#or use the traditional way 
# temp_list = data["temp"].to_list()
# no_of_days = len(temp_list)
# sum_of_temps = sum(temp_list)
# print(sum_of_temps / no_of_days)

#either use this process (shorter)
# print(data["temp"].mean())
# print(data["temp"].max())

# monday = data[data["day"] == "Monday"]
# print(monday)
# temp = int(monday.temp.iloc[0])
# F = (temp *1.8)+32
# print(F)

# data_dict = {
#     "students" : ["Amy", "James", "Angela"],
#     "scores" : [76, 76, 65]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("Score_data.csv")