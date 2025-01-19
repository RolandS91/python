# Ülesanne 6
# Sobols
# 19.12.2024
# https://www.metshein.com/unit/matemaatika-moodul/?id=21723 vajalike käskude jaoks

import turtle
import math

kordaja = 50
nurk = 53
korgus = 4.4

rad = math.radians(nurk)
kaugus = korgus / math.tan(rad)
c = math.sqrt(math.pow(kaugus,2) + math.pow(korgus,2))

print(c)
turtle.fd(kaugus*kordaja)
turtle.left(90)
turtle.fd(korgus*kordaja)
turtle.left(143)
turtle.fd(c*kordaja)

turtle.done()