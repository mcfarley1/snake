from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

snake = Snake()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
food = Food()
scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) <= 15:
        food.refresh()
        scoreboard.score += 1
        scoreboard.keep_score()
        snake.extend()

    # Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        if scoreboard.score > scoreboard.high_score:
            scoreboard.name_data = ""
            initials = screen.textinput("Snake", "Enter your initials: ")
            screen.listen()
            for num in range(3):
                scoreboard.name_data += initials[num].upper()
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            if scoreboard.score > scoreboard.high_score:
                scoreboard.name_data = ""
                initials = screen.textinput("Snake", "Enter your initials: ")
                screen.listen()
                for num in range(3):
                    scoreboard.name_data += initials[num].upper()
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
