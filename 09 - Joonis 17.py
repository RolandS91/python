# Ülesanne 9 joonis 17
# Sobols
# 19.01.2025


import turtle

# Akna seaded ja turtle kiirus
screen = turtle.Screen()
screen.setup(width=800, height=600)
turtle.speed(0)

turtle.penup()
turtle.goto(-300, -100)  # algus

for i in range(1, 7):
    suurus = 40 + 10 * i

    # Põhi
    turtle.pendown()
    for m in range(2):
        turtle.forward(suurus)
        turtle.left(90)
        turtle.forward(suurus)
        turtle.left(90)


    # Katus
    turtle.penup()
    turtle.goto(turtle.xcor(), turtle.ycor() + suurus)
    turtle.setheading(0)
    turtle.pendown()
    turtle.setheading(60)
    turtle.pencolor("green")
    for m in range(3):
        turtle.forward(suurus)
        turtle.right(120)

    # Uks
    turtle.penup()
    turtle.pencolor("red")
    turtle.goto(turtle.xcor() + suurus // 4, turtle.ycor() - suurus)
    turtle.setheading(0)
    turtle.pendown()
    for m in range(2):
        turtle.forward(suurus // 2)
        turtle.left(90)
        turtle.forward(suurus // 2)
        turtle.left(90)


    # Järgmine maja
    turtle.pencolor("black")
    turtle.penup()
    turtle.goto(turtle.xcor() + suurus + 20, -100)

# Lõpetus
turtle.done()



