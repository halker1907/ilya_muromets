import turtle as t
import math

t.shape("turtle")
t.color("red")
t.speed(0)

walls_width = 300
walls_hight = 100
door_width = 30
door_width = 50
roof_hight = 150
roof_side = math.sqrt(roof_hight ** 2 + (walls_width / 2) ** 2)
roof_angle = math.degrees(math.atan(roof_hight / (walls_width / 2)))

walls_width = int(input())
walls_hight = int(input())
door_width = int(input())
door_width = int(input())
roof_hight = int(input())


for i in range(2):
    t.fd(walls_width)
    t.left(90)
    t.fd(walls_hight)
    t.left(90)

t.fd(walls_width / 2 - door_width / 2)
for i in range(2):

    t.fd(door_width)
    t.left(90)
    t.fd(door_hight)
    t.left(90)

t.left(180)
t.fd(walls_width / 2 - door_width / 2)
t.right(90)
t.fd(walls_hight)
t.right(90)
t.left(roof_angle)
t.fd(roof_side)
t.right(roof_angle * 2)
t.fd(roof_side)

t.done()