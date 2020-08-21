import turtle
wn = turtle.Screen()
wn.bgcolor("hotpink")
alex = turtle.Turtle()
bob = turtle.Turtle()

alex.pensize(2)
alex.pencolor("yellow")

alex.right(180)
alex.forward(50)

bob.pensize(3)
bob.pencolor("blue")
bob.right(90)
bob.forward(100)
bob.left(90)
bob.forward(50)

wn.exitonclick()