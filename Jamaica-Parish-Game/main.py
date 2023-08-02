import pandas as pd
import turtle

# initialise the screen
screen = turtle.Screen()
screen.title("Jamaica Parish Game")
image = "jamaica-blank-map.gif"
screen.addshape(image)
turtle.shape(image)

# answers
data_source = pd.read_csv("12_parishes.csv")
parish_list = data_source.parish.to_list()


# check if parish exist
def parish_guess(guess):
    if guess in parish_list:
        right_answer(guess)
        return 1
    elif guess == '':
        screen.exitonclick()  # closes if you press "cancel" or just entered nothing and "ok"
    else:
        return 0


# Place name by parish if it exists
def right_answer(answer):
    marker = turtle.Turtle()
    marker.hideturtle()
    marker.penup()
    parish_marker = data_source[data_source.parish == answer]
    marker.goto(float(parish_marker.x), float(parish_marker.y))
    marker.write(answer)


# bring up the window where you guess the parish
score = 0
while score < 14:
    if score == 0:
        parish_name = screen.textinput("Guess a parish", "Name a Parish").title()
    else:
        parish_name = screen.textinput(f"{score}/14 parish", "Name a Parish").title()
    score += parish_guess(parish_name)

# close on click when done
screen.exitonclick()
