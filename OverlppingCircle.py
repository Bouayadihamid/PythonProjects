import turtle
#turtle.bgcolor('')
shelly = turtle.Turtle()

#for i in range(36):
#    shelly.circle(100)
#    shelly.right(10)

for n in range(36):
    shelly.penup()
    shelly.forward(200)
    for j in range(6):
        shelly.pendown()
        shelly.circle(5)
        shelly.penup()
        shelly.back(20)
    shelly.back(80)
    shelly.right(10)
shelly.hideturtle()