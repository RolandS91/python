# 01. ülesanne
# Sobols 05.12.2024


# See impordib kilpkonna mooduli
import turtle

# Kolmnurk
turtle.shape("turtle")
turtle.speed(0) # Reguleeri 1-9
turtle.penup()
turtle.goto(-500,300)
turtle.pendown()
turtle.forward(200) #fd, pikslites
turtle.left(120) # Pööramine kraadides
turtle.fd(200)
turtle.left(120)
turtle.fd(200)
turtle.left(120)

# Süda

turtle.penup()
turtle.goto(-200,300)
turtle.pendown()
turtle.fd(125)
turtle.circle(62.5,180)
turtle.right(90)
turtle.circle(62.5,180)
turtle.fd(125)

# Lõpetab kilpkonna, et ei jookseks kokku
turtle.done()