from turtle import Screen, Turtle
import time
from scoreboard import Scoreboard
from snake import Snake
from food import Food

tuple = (0, 1, 2, 3, 4, 5)
print (tuple[1:])

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("LA VIBORITAAAAAAAh")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.scoreadd()
        snake.extend_snake()
    if snake.head.xcor() >280 or snake.head.xcor() <-280 or snake.head.ycor() > 280 or snake.head.ycor() <-280:
        scoreboard.gameover()
        game_is_on = False


    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.gameover()
            game_is_on = False

screen.exitonclick()
