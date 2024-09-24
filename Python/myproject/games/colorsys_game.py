import turtle
import colorsys

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
n = 36
h = 0

for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1.0, 1.0)
    h += 1/n
    t.color(c)
    t.left(145)
    t.forward(i * 2)
    
turtle.done()
