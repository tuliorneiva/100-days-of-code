from turtle import Turtle, Screen, colormode
import random

#LER SOBRE O setheading() E O dot() NA DOCUMENTAÇÃO
colormode(255)
tim = Turtle()
tim.pensize(20)
tim.hideturtle()
tim.penup()

# Color list retrieved from Damien Hirst Methoxyverapamil using the colorgram library
color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]




# 10 dots por 10 filas de dots
# cada dot deve ter size igual a 20
# cada dot deve estar espaçados por 50, tanto horizontalmente quanto verticalmente

tim.setpos(-250, -250)
number_of_dots = 50

for dot in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500) #The length of the painting.
        tim.setheading(0)


screen = Screen()
screen.exitonclick()