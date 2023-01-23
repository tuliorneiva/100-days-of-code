from turtle import Turtle, Screen, colormode
import random

colormode(255)
dot = Turtle()
dot.pensize(20)
dot.hideturtle()

# Color list retrieved from Damien Hirst Methoxyverapamil using the colorgram library
color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136),
              (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73), (47, 121, 86),
              (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50),
              (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19),
              (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]


def paint():
    dot.color(random.choice(color_list))
    dot.forward(0)
    dot.penup()
    dot.forward(50)
    dot.pendown()


def move_row(pos):
    dot.penup()
    y = pos[1]
    new_y = y + 50
    dot.goto(-250, new_y)
    dot.pendown()


def start():
    dot.penup()
    dot.setpos(-250, -250)
    dot.pendown()
    for rows in range(10):
        for x in range(10):
            paint()
        pos = dot.pos()
        move_row(pos)


start()


screen = Screen()
screen.exitonclick()
