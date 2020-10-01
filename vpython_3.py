#Zadanie 3
#Utwórz napis przestrzenny 'Python'. Następnie napisz
#symulację, w której kamera z pewnej odległości zbliża się do
#napisu, okrąża go po półokręgu (180 stopni) i oddala się na
#początkową odległość.

from vpython import *

scene.range = 7
T = text(text='Python',
     align='center', color=color.orange)

while scene.range > 2:
    rate(100)
    scene.range -=  0.009

licznik = 0
while 1:
    rate(100)
    T.rotate(angle=radians(1), axis=vector(0,1,0))
    #print(licznik)
    licznik += 1
    if licznik == 360:
        break

while scene.range < 7:
    rate(100)
    scene.range +=  0.009


