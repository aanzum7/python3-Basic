import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.shape("turtle")
alex.color("green")
distance = 5
alex.up()
for x in range (30):
    alex.stamp()
    alex.forward(distance)
    alex.right(24)
    distance= distance + 2

window.exitonclick()