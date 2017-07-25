# Foundations of Computer Science
# BSc Computer Engineering, University of Rome Tor Vergata
# Exercise: Implement an image complementary effect.

def complementaryPicture(picture):
# @param picture:Picture;
  pixels = getPixels(picture)
  for pixel in pixels:
    setRed(pixel, 255 - getRed(pixel))
    setGreen(pixel, 255 - getGreen(pixel))
    setBlue(pixel, 255 - getBlue(pixel))
  

def main():
  file = pickAFile()
  picture = makePicture(file)
  complementaryPicture(picture)
  repaint(picture)