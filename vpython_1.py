from vpython import *
import random

scene.center = vector(-4,-3,0)
scene.forward = vector(-1.13539,-0.0172799,-1.18385)
scene.up = vector(1,1,1)
scene.width = 1800
scene.height = 850

w1 = box(pos = vector(0,0,0), size=vector(8,4,0.2), texture=textures.wood)

w2 = box(pos = vector(0,2,0.25), size=vector(8,0.2,0.5), texture=textures.wood)
w3 = box(pos = vector(4,0,0.25), size=vector(0.2,4,0.5), texture=textures.wood)
w5 = box(pos = vector(0,-2,0.25), size=vector(8,0.2,0.5), texture=textures.wood)
w6 = box(pos = vector(-4,0,0.25), size=vector(0.2,4,0.5), texture=textures.wood)

l1 = box(pos = vector(3.5,1.5,-1), size=vector(0.5,0.5,2), texture=textures.wood)
l2 = box(pos = vector(3.5,-1.5,-1), size=vector(0.5,0.5,2), texture=textures.wood)
l3 = box(pos = vector(-3.5,1.5,-1), size=vector(0.5,0.5,2), texture=textures.wood)
l4 = box(pos = vector(-3.5,-1.5,-1), size=vector(0.5,0.5,2), texture=textures.wood)

ball = sphere(pos=vector(0.3,0.3,0.3), radius=0.2, color=color.white)
ball.velocity = vector(1,1,0)
dt=0.01

while(1):
    #print(scene.forward)
    rate(100)
    ball.pos = ball.pos + ball.velocity*dt
    print(ball.pos)
    if ball.pos.x < -3.7:
        ball.velocity.x = random.uniform(1, 2.5)
    if ball.pos.x > 3.7:
        ball.velocity.x = random.uniform(-1, -2.5)
    if ball.pos.y < -1.7:
        ball.velocity.y = random.uniform(1, 2.5)
    if ball.pos.y > 1.7:
        ball.velocity.y = random.uniform(-1, -2.5)