import time
from turtle import Screen
from snake import Snake
from food import Food


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()

screen.listen()
screen.onkeypress(snake.move_up, "Up")
screen.onkeypress(snake.move_left, "Left")
screen.onkeypress(snake.move_right, "Right")
screen.onkeypress(snake.move_down, "Down")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()



screen.exitonclick()
