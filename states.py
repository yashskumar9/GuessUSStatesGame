from turtle import Turtle


class States(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def update(self, state):
        self.write(state, align='center', font=('Arial', 10, 'normal'))

    def enter_state(self, new_x, new_y, state):
        self.goto(new_x, new_y)
        self.update(state)
