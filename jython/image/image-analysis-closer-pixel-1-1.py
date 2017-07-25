# Foundations of Computer Science
# BSc Computer Engineering, University of Rome Tor Vergata
# Exercise: Retrieve the position of the "most red", "most green" and "most blue" pixels of an image.
 
def getCloserPixelX(picture, color):
# @param picture:Picture;
# @param color:Color;
  x = -1
  d = 442.0
  for pixel in getPixels(picture):
    pcol = getColor(pixel)
    pxd = distance(color, pcol)
    if (pxd < d):
      d = pxd
      x = getX(pixel)
  return x
 
def getCloserPixelY(picture, color):
# @param picture:Picture;
# @param color:Color;
  y = -1
  d = 442.0
  for pixel in getPixels(picture):
    pcol = getColor(pixel)
    pxd = distance(color, pcol)
    if (pxd < d):
      d = pxd
      y = getY(pixel)
  return y
 
def printAnalysis(picture):
# @param picture:Picture; 
  R = makeColor(255, 0, 0)
  G = makeColor(0, 255, 0)
  B = makeColor(0, 0, 255)
  print "most-r: (%d, %d)" % (getCloserPixelX(picture, R), getCloserPixelY(picture, R))
  print "most-g: (%d, %d)" % (getCloserPixelX(picture, G), getCloserPixelY(picture, G))
  print "most-b: (%d, %d)" % (getCloserPixelX(picture, B), getCloserPixelY(picture, B))

def main():
  file = pickAFile()
  picture = makePicture(file)
  printAnalysis(picture)