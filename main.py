from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.speed("fastest")
Screen().colormode(255)
timmy.hideturtle()

def colorco():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

def circle():
    timmy.color(colorco())
    timmy.circle(100)

def draw_spirograph():
    for _ in range(361):
        circle()
        timmy.color(colorco())
        timmy.fd(1)
        timmy.left(2)

draw_spirograph()

screen = Screen()
screen.exitonclick()
