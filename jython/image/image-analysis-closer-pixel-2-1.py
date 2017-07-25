# Foundations of Computer Science
# BSc Computer Engineering, University of Rome Tor Vergata
# Exercise: Retrieve the position of the "most red", "most green" and "most blue" pixels of an image.

def getCloserPixel(picture, color):
# @param picture:Picture;
# @param color:Color;
  x = -1
  y = -1
  d = 442.0
  for px in getPixels(picture):
    pxd = distance(color, getColor(px))
    if (pxd < d):
      d = pxd
      x = getX(px)
      y = getY(px)
  return (x, y)

def printAnalysis(picture):
# @param picture:Picture;
  R = makeColor(255, 0, 0)
  G = makeColor(0, 255, 0)
  B = makeColor(0 ,0, 255)
  print "most-r: %s" % (getCloserPixel(picture, R),)
  print "most-g: %s" % (getCloserPixel(picture, G),)
  print "most-b: %s" % (getCloserPixel(picture, B),)
    
def main():
  file = pickAFile()
  picture = makePicture(file)
  printAnalysis(picture)