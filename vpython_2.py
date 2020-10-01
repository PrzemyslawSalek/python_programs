#Zadanie 2
#Napisz program (rozwinięcie zadania 1), który symuluje
#odbijanie się kuli od ścian pudełka (kula jest wewnątrz pudełka).
#Ściany pudełka powinny być częściowo przezroczyste. Prędkość
#startowa losowa (kierunek, wartość).

from vpython import *

scene.center = vector(-4,-3,0)
scene.forward = vector(-1.13539,-0.0172799,-1.18385)
scene.up = vector(1,1,1)
scene.width = 1800
scene.height = 850
w1 = box(pos = vector(0,0,0), size=vector(4,4,0.01), color=color.red, opacity=0.6)
w2 = box(pos = vector(0,2,2), size=vector(4,0.01,4), color=color.green, opacity=0.6)
w3 = box(pos = vector(2,0,2), size=vector(0.01,4,4), color=color.blue, opacity=0.6)
w4 = box(pos = vector(0,0,4), size=vector(4,4,0.01), color=color.yellow, opacity=0.6)
w5 = box(pos = vector(0,-2,2), size=vector(4,0.01,4), color=color.green, opacity=0.6)
w6 = box(pos = vector(-2,0,2), size=vector(0.01,4,4), color=color.blue, opacity=0.6)

ball = sphere(pos=vector(1,1,1), radius=0.3, color=color.white)
ball.velocity = vector(-1,-1,-1)
dt=0.01
while 1:
    #print(scene.forward)
    rate(100)
    ball.pos = ball.pos + ball.velocity*dt
    #print(ball.pos)
    if ball.pos.x < -1.7:
        ball.velocity.x = 1
    if ball.pos.x > 1.7:
        ball.velocity.x = -1
    if ball.pos.y < -1.7:
        ball.velocity.y = 1
    if ball.pos.y > 1.7:
        ball.velocity.y = -1
    if ball.pos.z < 0.3:
        ball.velocity.z = 1
    if ball.pos.z > 3.7:
        ball.velocity.z = -1
