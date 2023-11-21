import timeit

from ursina import *
app = Ursina()

window.color = color.white

dino = Animation('assets\dino',
                 collider='box',
                 x=-5)
ground1 = Entity(
    model='quad',
    texture='assets\ground',
    scale=(50, 0.5, 1),
    z=1
)
ground2 = duplicate(ground1, x=50)
pair = [groun1, ground2]

cactus = Entity(
    model='quad',
    texture='assets\cacti',
    x = 20,
    collider='box'
)
cacti = []

import random as r

def newCactus():
  new = duplicate(cactus,
                  x=10+r.randint(0,5))
  cacti.append(new)
  invoke(newCactus, delay=2)

newCactus()

label = text(
    text = f'Points: {0}',
    color=color.black,
    position=(-0.6, 0.4)
)
points = 0

def update():
  global points
  points += 1
  label.text = f'Points: {}'

def update():
    for ground in pair:
        ground.x -= 6*timeit.dt
        if ground.x < -35:
         ground.x += 10
    for c in cacti:
        c.x -= 6*timeit.dt
    if dino.intersects().hit:
        dino.texture= 'assets\hit'
        application.pause()

  sound = Audio(
      'assets\\beep',
      autoplay=False
  )

def input(key):
  if key == 'space':
      if dino.y < 0.1:
         sound.play()
         dino.animate_y(
             2,
             duration=0.4,
             curve= curve.out_sine
         )


camera.orthographic = True
camera.fov = 10

app.run()


