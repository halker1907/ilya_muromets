import turtle as t
import math
import os

t.shape("turtle")
t.speed(0)


walls_width = int(input("ширина стен"))
os.system("cls")
walls_hight = int(input("высота стен"))
os.system("cls")
walls_color = input("цвет стен (hex)")
os.system("cls")
door_width = int(input("ширина двери"))
os.system("cls")
door_hight = int(input("высота двери"))
os.system("cls")
door_color = input("цвет дери")
os.system("cls")
roof_hight = int(input("высота крыши"))
os.system("cls")
roof_color = input("цвет крыши")
os.system("cls")
roof_side = math.sqrt(roof_hight ** 2 + (walls_width / 2) ** 2)
roof_angle = math.degrees(math.atan(roof_hight / (walls_width / 2)))

x = (walls_width / 2)
y = (walls_hight + roof_hight) / 2 -1
t.setposition(x,y)



t.fillcolor(walls_color)
t.begin_fill()
for i in range(2):
    t.fd(walls_width)
    t.left(90)
    t.fd(walls_hight)
    t.left(90)
t.fd(walls_width / 2 - door_width / 2)
t.end_fill()

t.fillcolor(door_color)
t.begin_fill()
for i in range(2):

    t.fd(door_width)
    t.left(90)
    t.fd(door_hight)
    t.left(90)
t.end_fill()

t.left(180)
t.fd(walls_width / 2 - door_width / 2)
t.fillcolor(roof_color)
t.begin_fill()
t.right(90)
t.fd(walls_hight)
t.right(90)
t.left(roof_angle)
t.fd(roof_side)
t.right(roof_angle * 2)
t.fd(roof_side)
t.setheading(180)
t.fd(walls_width)

t.end_fill()


t.done()