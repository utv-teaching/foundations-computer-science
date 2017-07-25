# Foundations of Computer Science
# BSc Computer Engineering, University of Rome Tor Vergata
# Exercise: Implement an image greyscale effect.

def greyScalePicture(picture):
# @param picture:Picture;
  pixels = getPixels(picture)
  for pixel in pixels:
    n = (getRed(pixel) + getGreen(pixel) + getBlue(pixel)) / 3
    color = makeColor(n, n, n)
    setColor(pixel, color)

def main():
  file = pickAFile()
  picture = makePicture(file)
  greyScalePicture(picture)
  repaint(picture)
