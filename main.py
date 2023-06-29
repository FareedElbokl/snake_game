from turtle import  Screen
import time

from scoreboard import Scoreboard
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Fareed's Snake Game")
screen.tracer(0)


snake = Snake() #creating the snake object
food = Food()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")



game_is_on = True
while game_is_on == True:
    screen.update()
    time.sleep(0.1) #screen will update every 0.1 seconds
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_one()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()


    #detect collision with body
    #if head collides with any segment in the tail, trigger game over sequence.
    for segment in snake.segments[1:]: #using slicing here loop from POSITION (not item) 1 to the end of the list (thats why didnt include a 2nd number) Third number would significy the increment.
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


























screen.exitonclick()