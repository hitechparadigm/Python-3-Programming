import turtle
import random
import math

wn = turtle.Screen()
wn.bgcolor("black")
tess = turtle.Turtle()
tess.color("white")
colors = ["red", "green", "yellow", "purple", "blue", "chartreuse", "white", "violet", "brown", "gold", "silver", "cyan", "coral", "DarkOrange", "DodgerBlue"]

dist = 150
tess.speed(10)

for i in range(36):
    my_color = random.choice(colors)
    tess.color(my_color)
    tess.pensize(1)
    tess.left(22.5)
    tess.forward(dist)    
    tess.left(90)
    tess.forward(dist)    
    tess.left(90)
    tess.forward(dist)    
    tess.left(90)
    tess.forward(dist)    
    tess.left(90)
    tess.circle(50)
    tess.left(3)
    dist = dist + 2
# colors = ["red", "green", "yellow", "pink", "blue", "purple", "white"]

# #tess.color("blue")
# #tess.shape("turtle")
# distance = 200
# tess.pensize(2)

# for move in range(4):
#     my_color = random.choice(colors)
#     tess.color(my_color)
#     tess.forward(distance)
#     tess.left(90)
# tess.left(90) # tess to turn up 
# tess.forward(200) # tess move up
# tess.right(45)
# #roof = math.sqrt(200**200/2)
# roof = 141.42
# tess.forward(roof)
# tess.right(90)
# tess.forward(roof)

# tess.circle(50)
# tess.right(135)
# tess.forward(200)
# tess.left(225)
# tess.circle(50)

wn.exitonclick()


