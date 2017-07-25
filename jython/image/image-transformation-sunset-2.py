# Foundations of Computer Science
# BSc Computer Engineering, University of Rome Tor Vergata
# Exercise: Implement an image sunset effect.

def reduceBlue(pix):
# @param picture:Picture;
  setBlue(pix, getBlue(pix) * 0.7)    
    
def reduceGreen(pix):
# @param picture:Picture;
  setGreen(pix, getGreen(pix) * 0.7)

def sunset(picture):
# @param picture:Picture;
  for pix in getPixels(picture):
    reduceBlue(pix)
    reduceGreen(pix)

def main():
  file = pickAFile()
  picture = makePicture(file)
  sunset(picture)
  repaint(picture)