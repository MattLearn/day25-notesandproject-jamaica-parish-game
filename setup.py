import pandas as pd
import turtle

# import csv as reader
# reading csv data the hard way
# with open("weather_data.csv") as weather_file:
#     data = csv.reader(weather_file)
#     temperatures = []
#     for row in data:
#         print(row[1])
#         if row[1] !="temp":
#             temperatures.append(row[1])
#     print(temperatures)

# # reading data using pandas
# pd_data = pd.read_csv("weather_data.csv")
# print(pd_data["temp"])
# temperatures = pd_data["temp"].tolist()

# some more examples of navigating csv using pandas
# print(temperatures, pd_data["temp"].max())
# print(pd_data[pd_data.temp == pd_data.temp.max()])
# monday = (pd_data[pd_data.day == "Monday"])
# monday_temp = (monday.iloc)
# monday_temp_f = monday.temp * 9/5 + 32
# print(monday_temp_f)

# create a new dataframe without source save to csv
# new_dict= {
#     "source": [1,2,3,4],
#     "value": [1,2,5,6]
# }
# frame = pd.DataFrame(new_dict)
# frame.to_csv("newfile.csv")

answers = {
    "parish": [],
    "x": [],
    "y": []
}
screen = turtle.Screen()
screen.title("Jamaica Parish Game")
image = "./Jamaica-Parish-Game/jamaica-blank-map.gif"
screen.addshape(image)
turtle.shape(image)


def add_coordinate(x_cor, y_cor):
    parish_name = screen.textinput("Location", "Which Parish is this?")
    answers["parish"].append(parish_name)
    answers["x"].append(x_cor)
    answers["y"].append(y_cor)


screen.onscreenclick(add_coordinate)

turtle.mainloop()

df = pd.DataFrame(answers)
df.to_csv("Jamaica-Parish-Game/12_parishes.csv", mode='a', index=False)
# screen.exitonclick()
