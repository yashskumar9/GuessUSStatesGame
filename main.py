from states import States
from score_board import ScoreBoard
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
available_state = data.state.to_list()

my_state = States()
score_board = ScoreBoard()


def find_state(ans_state, av_states):
    if ans_state in av_states:
        state_index = av_states.index(ans_state)
        return state_index
    else:
        return False


def add_missed_states(ms):
    ms = [state for state in available_state if state not in correct_guesses]
    missed_states_data = pandas.Series(ms)
    missed_states_data.to_csv("Missed States.csv")


correct_guesses = []
missed_states = []
game_on = True

while game_on:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state's "
                                                                                              "name? ").title()
    if answer_state == 'Exit':
        add_missed_states(missed_states)
        break
    elif answer_state is None:
        score_board.game_over()
        add_missed_states(missed_states)
        game_on = False

    index = find_state(answer_state, available_state)
    already_guessed = find_state(answer_state, correct_guesses)
    if already_guessed is not False:
        print("You've already guessed this state. Try again.")
    elif index is not False:
        guessed_state = data[data.state == answer_state]
        new_x = guessed_state.x.item()
        new_y = guessed_state.y.item()
        correct_guesses.append(answer_state)
        my_state.enter_state(new_x, new_y,
                             answer_state)  # instead of answer_state, we can use guessed_state.state.item()
        score_board.add_score()

    elif len(correct_guesses) == 49 and index >= 0:
        score_board.won_game()
        game_on = False

    else:
        score_board.game_over()
        add_missed_states(missed_states)
        game_on = False

screen.exitonclick()
