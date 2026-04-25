import turtle

screen = turtle.Screen()
screen.bgcolor("lightyellow")

t = turtle.Turtle()
t.speed(5)
t.pensize(3)

# -------- Krishna --------
t.penup()
t.goto(-120,0)
t.pendown()

# Head
t.color("blue")
t.begin_fill()
t.circle(30)
t.end_fill()

# Body
t.right(90)
t.forward(80)

# Legs
t.backward(40)
t.left(30)
t.forward(60)
t.backward(60)
t.right(60)
t.forward(60)
t.backward(60)
t.left(30)

# Arms
t.backward(40)
t.left(90)
t.forward(60)
t.backward(30)
t.right(180)
t.forward(60)

# Flute
t.penup()
t.goto(-160,-10)
t.pendown()
t.color("brown")
t.forward(80)

# -------- Radha --------
t.penup()
t.goto(120,0)
t.setheading(0)
t.pendown()

# Head
t.color("pink")
t.begin_fill()
t.circle(30)
t.end_fill()

# Body
t.right(90)
t.forward(80)

# Legs
t.backward(40)
t.left(30)
t.forward(60)
t.backward(60)
t.right(60)
t.forward(60)
t.backward(60)
t.left(30)

# Arms
t.backward(40)
t.left(90)
t.forward(60)
t.backward(30)
t.right(180)
t.forward(60)

# Text
t.penup()
t.goto(0,-150)
t.color("purple")
t.write("Radha Krishna", align="center", font=("Arial",24,"bold"))

turtle.done()