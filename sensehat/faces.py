from sense_hat import SenseHat
from time import sleep

sense = SenseHat() 
r = (255, 0, 0) # Red
b = (0, 0, 180) # Blue

smile_1 = [
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, r, b, b, r, b, b,
  b, b, b, b, b, b, b, b,
  b, r, b, b, b, b, r, b,
  b, b, r, r, r, r, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b
]

smile_2 = [
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, r, b, b, r, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, r, r, r, r, r, r, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b
]

smile_3 = [
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, r, b, b, r, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, r, r, r, r, b, b,
  b, r, b, b, b, b, r, b,
  b, b, b, b, b, b, b, b
]

all_smiles = [smile_1, smile_2, smile_3]

while True:
  for smile in all_smiles:
    sense.set_pixels(smile)
    sleep(.2)
  