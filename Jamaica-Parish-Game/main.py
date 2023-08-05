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
guessed_parishes = []

# check if parish exist
def parish_guess(guess):
    if guess in parish_list:
        correct_answer(guess)
        return 1
    elif guess == 'exit':
        return -1
    else:
        return 0


# Place name by parish if it exists
def correct_answer(answer):
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
    guessed_parishes.append(parish_name)
    if parish_guess(parish_name) >= 0:
        score += parish_guess(parish_name)
    else:
        break

# learn_material = []
# for parish in parish_list:
#     if parish not in guessed_parishes:
#         learn_material.append(parish)
learn_material = [parish for parish in parish_list if parish not in guessed_parishes]
study_df = pd.DataFrame(learn_material)
study_df.to_csv("learning_material.csv",index=False)

# close on click when done
screen.exitonclick()

