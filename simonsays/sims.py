from random import randint, choice
from time import sleep

simon_says = dict("Hands on head", "Hands on ears", "Right hand up", "Left hand up", "Hands on shoulders")
intros = ["Simon Says... ", ""]

for x in range(0,10):
  index = randint(0,4)
  instruction = simon_says[index]
  intro = choice(intros)
  print(f"{intro}{instruction}")
  sleep(4)

