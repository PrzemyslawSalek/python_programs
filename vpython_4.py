#Zadanie 4
#Utwórz dwie kule, z których jedna znajduje się w środku
#układu współrzędnych, a druga w pewnej odległości. Zasymuluj
#ruch drugiej kuli po okręgu.

from vpython import *

ball = sphere(pos=vector(0,0,0), radius=0.3, color=color.white)
ball2 = sphere(pos=vector(0,0,2), radius=0.3, color=color.white)

while 1:
    rate(100)
    ball2.rotate(angle=radians(1), origin=vector(0,0,0))