import turtle
import pandas

data = pandas.read_csv('states_data.csv')
screen = turtle.Screen()
screen.title("Indian States Game")
image = "img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []
all_states = data['state'].to_list()
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/29 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        df = pandas.DataFrame(missing_states)
        df.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = data[data['state'] == answer_state]
        timmy = turtle.Turtle()
        timmy.penup()
        timmy.hideturtle()
        timmy.goto(int(state_data['x']), int(state_data['y']))
        timmy.write(answer_state)

# This code will have for creating coordinates of x and y
# def get_mouse_click_corr(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_corr)
# turtle.mainloop()
