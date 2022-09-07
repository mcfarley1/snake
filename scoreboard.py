from turtle import Turtle


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.score = 0
        self.numeric_data = ""
        self.name_data = ""
        with open("data.txt", mode="r") as record:
            self.data = record.read()
        for num in range(3):
            self.name_data += self.data[num]
        for num in range(len(self.data) - 4):
            self.numeric_data += self.data[num + 4]
        self.high_score = int(self.numeric_data)
        self.keep_score()

    def keep_score(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.name_data} {self.high_score}", move=False, align='center',
                   font=('Arial', 16, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as record:
                record.write(f"{self.name_data} {str(self.high_score)}")
        self.score = 0
        self.keep_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", move=False, align='center', font=('Arial', 16, 'normal'))
