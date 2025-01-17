from turtle import Turtle


class ScoreBoard:

    def __init__(self):
        self.score = 0
        self.print_score = Turtle()
        self.print_score.penup()
        self.print_score.hideturtle()

    def add_score(self):
        self.score += 1

    def won_game(self):
        self.print_score.write("YOU WON \nFinal Score: 50/50", align='center',
                               font=('Courier', 15, 'bold'))

    def game_over(self):
        self.print_score.goto(0, 0)
        self.print_score.write("GAME OVER", align='center', font=('Courier', 15, 'bold'))
        self.print_score.goto(0, -25)
        self.print_score.write(f"Final Score: {self.score}/50", align='center', font=('Courier', 15, 'bold'))
