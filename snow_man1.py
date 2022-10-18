import turtle as t
import random

t.speed(0)

while True:
    t.colormode(255)
    x = random.randint(-200, 200)
    y = random.randint(-100, 100)
    circle = random.randint(3,6)
    radios = random.randint(-100, 100)
    red = random.randint(0, 255)
    green = random.randint(0, 255) 
    blue = random.randint(0, 255)

    t.penup()
    t.setposition(x,y)
    t.pendown()

    for i in range(3):
        t.pendown()
        t.fillcolor(red,green,blue)
        t.begin_fill()
        t.circle(radios)
        t.end_fill()
        t.penup()
        t.setheading(90)
        t.fd(radios * 2)
        t.setheading(0)
        radios = radios / 2
        

t.down()