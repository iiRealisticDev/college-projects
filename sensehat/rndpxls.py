from sense_hat import SenseHat
from random import choice

sense = SenseHat() # SenseHat class

purple = (255,0,255)
green = (0,255,0)
orange = (255, 165, 0)
white = (255,255,255)

# clear the SenseHat
def clr():
  pixels = []
  for x in range(0, 64):
    pixels.append(white)
  sense.set_pixels(pixels)

# generate random pixels, 64 of them
def rnd_col():
  cols = [purple, green, orange]
  pixels = []
  
  for x in range(0, 64):
    col = choice(cols)
    pixels.append(col)
  
  sense.set_pixels(pixels)

clr() # clear it on start, just because it's easier to look at

# keep assinging new colours every time the joystick is pressed, with a direction of middle. 
# use the Enter key in the emulator to simulate.
while True:
  for event in sense.stick.get_events():
    if event.action == "pressed" and event.direction == "middle":
      rnd_col()