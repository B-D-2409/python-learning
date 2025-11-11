import random
import turtle
from turtle import Turtle, Screen


# timmy_turtle = Turtle()
# timmy_the_turtle = turtle.shape("turtle")
#
#
#
# tot = Turtle()
#
# for _ in range(15):
#     tot.forward(10)
#     tot.penup()
#     tot.forward(10)
#     tot.pendown()
#
#
#
#
#
#




# tim = Turtle()
# num_sides = 5
# colors = ["medium aquamarine","DarkOrchid", "IndianRed", "DeepSkyBlue"]
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#        tim.forward(100)
#        tim.right(angle)
#
#
# for shape_side_n in range(3,11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)
#
#








# import turtle as t
# import random
#
# tim = t.Turtle()
#
# ########### Challenge 4 - Random Walk ########
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
#
# for _ in range(200):
#     tim.color(random.choice(colours))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#
#




import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)







screen = Screen()
screen.exitonclick()

