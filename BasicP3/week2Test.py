import turtle            # set up alex
wn = turtle.Screen()
alex = turtle.Turtle()
boob = turtle.Turtle()

for aColor in ["yellow", "red", "purple", "blue"]: # repeat four times
    alex.forward(50)
    alex.left(90)
    alex.pencolor(aColor)
    alex.speed(10)

for bColor in ["pink", "green", "hotpink", "lightgreen"]: # repeat four times
    boob.right(90)
    boob.forward(50)
    boob.pencolor(bColor)
    boob.speed(0)

wn.exitonclick()
