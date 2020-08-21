import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.pensize(3)
alex.pencolor("green")
distance = 10
angle = 90
for x in range (15):
    alex.forward(distance)
    alex.right(angle)
    distance = distance + 10

window.exitonclick()