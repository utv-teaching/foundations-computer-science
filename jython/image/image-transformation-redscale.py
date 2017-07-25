# Foundations of Computer Science
# BSc Computer Engineering, University of Rome Tor Vergata
# Exercise: Implement an image redscale effect.

def redScalePicture(picture):
# @param picture:Picture;
  pixels = getPixels(picture)
  for pixel in pixels:
    setGreen(pixel, 0)
    setBlue(pixel, 0)

def main():
  file = pickAFile()
  picture = makePicture(file)
  redScalePicture(picture)
  repaint(picture)