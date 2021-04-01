import random
from turtle import Turtle, Screen
import turtle as t

turtle = Turtle()
screen = Screen()
t.colormode(255)
t.tracer(False)  # Change this to True to enable animation
turtle.penup()
turtle.goto(-350, -300)

# You can use any combinations of colours. I have provided 2 list below.
colourlist = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157)]
colourlist2 = [(227, 227, 225), (249, 212, 93), (150, 69, 97), (53, 99, 155),
               (232, 137, 62), (107, 174, 211), (243, 237, 241), (114, 83, 59), (201, 146, 177), (200, 77, 109),
               (145, 134, 72),
               (230, 90, 59), (141, 192, 140), (72, 103, 90), (68, 162, 92), (5, 165, 179), (227, 161, 183),
               (115, 126, 142),
               (163, 196, 221), (16, 66, 123), (187, 24, 34), (13, 56, 103), (235, 172, 160), (175, 201, 179),
               (163, 200, 215),
               (186, 27, 25), (80, 55, 37), (96, 61, 30), (53, 74, 65)]

# Change the below parameters as per your wish
rows = 100
columns = 100
gap = 5
size = 5

for _ in range(rows):
    for _ in range(columns):
        turtle.forward(gap)
        turtle.dot(size, random.choice(colourlist))
    turtle.setheading(90)
    turtle.forward(gap)
    turtle.setheading(180)
    turtle.forward(gap * columns)
    turtle.right(180)

screen.exitonclick()
