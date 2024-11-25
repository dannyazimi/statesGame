import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_States_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct",
                                    prompt="What's another state's name? ").title()
    if answer_state == "Exit" :
        missed_states = []
        for state in data["state"].values:
            if state not in guessed_states:
                missed_states.append(state)
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("States to learn.csv")

        break
    if answer_state in data["state"].values:
        guessed_states.append(answer_state)
        matching_row = data [data["state"] == answer_state]
        x_coor = int(matching_row.iat[0,1])
        y_coor = int(matching_row.iat[0,2])
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        state.goto(x_coor,y_coor)
        state.write(answer_state)



