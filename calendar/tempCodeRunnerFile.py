from turtle import *
import colorsys

speed(0)
bgcolor("black")

h = 0
for i in range(200):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    pencolor(c)
    h += 0.01
    forward(i)
    left(59)

done()