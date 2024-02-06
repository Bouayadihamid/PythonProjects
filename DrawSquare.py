import turtle
shelly = turtle.Turtle()
shelly.begin_fill()
shelly.color("black", "red")
for n in range (36):
    for i in range (4):
        shelly.forward(100)
        shelly.left(90)
    shelly.right(10)
shelly.end_fill()

