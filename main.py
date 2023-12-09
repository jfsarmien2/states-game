import turtle
import pandas

screen = turtle.Screen()

screen.title('U.S. States Game')

screen.setup(700, 500)

image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")

all_states = data["state"].to_list()

guess_states = []

missing_states = []

while len(guess_states) < 50:

    answer_state = screen.textinput(title=f"{len(guess_states)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":

        for state in all_states:

            if state not in guess_states:

                missing_states.append(state)

        states_to_learn = pandas.DataFrame(missing_states)

        states_to_learn.to_csv("states_to_learn.csv")

        break
 

    if answer_state in all_states:

        guess_states.append(answer_state)

        t = turtle.Turtle()

        t.hideturtle()

        t.penup()

        state_data = data[data["state"] == answer_state]

        t.goto(int(state_data["x"]), int(state_data["y"]))

        t.write(answer_state)
    

screen.mainloop()