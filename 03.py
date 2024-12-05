# 3. ülesanne
# Sobols 05.12.2024

# 3.1
nimi = "Roland" # sõne, string, str
vanus = 33 #int, integer, täisarv
keskmine_hinne = 4.53 # komaarv, float

# Plussiga saan stringid kokku
print(nimi+", "+str(vanus)+" aastat vana ja keskmine hinne on "+str(keskmine_hinne)) # string
# komaga saan mitu asja printida
print(nimi,",",vanus,"aastat vana ja keskmine hinne on",keskmine_hinne) # komadega
# lause vormindamine f"" abil lünkadega
print(f"{nimi}, {vanus} aastat vana ja keskmine hinne on {keskmine_hinne}!") # vormindamine f""


# 3.2

toode = "leibu"
kogus = 5
hind = 2.35

print("Soovin "+str(toode)+" "+str(kogus)+", "+"mille tüki hind on "+str(hind))

# 3.3

sihtkoht = "Hispaania"
paevade_arv = 5
oobimise_hind = 120.50

# pooleli
      
      
      
      
# 3.7 kolmnurk

import turtle

kylje_pikkus = 200
nurk = 120
kujundi_varv = "blue"
kaugus = 1.5

# kolmnurk 1
turtle.shape("turtle")
turtle.color(kujundi_varv)
turtle.speed(0) # Reguleeri 1-9
turtle.forward(kylje_pikkus) #fd, pikslites
turtle.left(nurk) # Pööramine kraadides
turtle.fd(kylje_pikkus)
turtle.left(nurk)
turtle.fd(kylje_pikkus)
turtle.left(nurk)

# kolmnurk 2
turtle.penup()
turtle.fd(kylje_pikkus*kaugus)
turtle.pendown()
turtle.forward(kylje_pikkus) #fd, pikslites
turtle.left(nurk) # Pööramine kraadides
turtle.fd(kylje_pikkus)
turtle.left(nurk)
turtle.fd(kylje_pikkus)
turtle.left(nurk)

# kolmnurk 3
turtle.penup()
turtle.fd(kylje_pikkus*kaugus)
turtle.pendown()
turtle.forward(kylje_pikkus) #fd, pikslites
turtle.left(nurk) # Pööramine kraadides
turtle.fd(kylje_pikkus)
turtle.left(nurk)
turtle.fd(kylje_pikkus)
turtle.left(nurk)

turtle.done()      
      
      
      
      
      
      
      
