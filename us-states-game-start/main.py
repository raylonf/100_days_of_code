import turtle
import pandas as pd
from states import State


screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

states_country = pd.read_csv('50_states.csv')
list_states = states_country.state.to_list()
guessed_correct_states = []

while len(guessed_correct_states) < 50:
    screen.update()
    answer_state = screen.textinput(title=f'{len(guessed_correct_states)}/50 Guess the State', prompt="What's another state's name?").capitalize().strip()
    if answer_state == 'Exit':
        break
    if answer_state in list_states:
        correct_state = states_country[states_country.state == answer_state]
        x = int(correct_state.x)
        y = int(correct_state.y)
        answer = State()
        answer.setposition(x, y)
        answer.write(correct_state.state.item())
        guessed_correct_states.append(answer)
        list_states.remove(answer_state)

missing_states = [state for state in list_states]
data_save = pd.DataFrame(missing_states)
data_save.to_csv('Missing_states.csv')