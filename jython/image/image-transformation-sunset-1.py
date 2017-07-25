# Foundations of Computer Science
# BSc Computer Engineering, University of Rome Tor Vergata
# Exercise: Implement an image sunset effect.

def reduceBlue(picture):
# @param picture:Picture;
  for pix in getPixels(picture):
    setBlue(pix, getBlue(pix) * 0.7)    
    
def reduceGreen(picture):
# @param picture:Picture;
  for pix in getPixels(picture):
    setGreen(pix, getGreen(pix) * 0.7)

def sunset(picture):
# @param picture:Picture;
  reduceBlue(picture)
  reduceGreen(picture)

def main():
  file = pickAFile()
  picture = makePicture(file)
  sunset(picture)
  repaint(picture)