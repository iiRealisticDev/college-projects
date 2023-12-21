from sense_hat import SenseHat

sense = SenseHat() 

b = (0, 0, 0)
c = (255, 255, 0)

alien = [
  c, b, b, b, b, b, b, c,
  b, c, b, b, b, b, c, b,
  b, c, c, c, c, c, c, b,
  b, c, b, c, c, b,
]

sense.set_pixels(alien)