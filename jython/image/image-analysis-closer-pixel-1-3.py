# Foundations of Computer Science
# BSc Computer Engineering, University of Rome Tor Vergata
# Exercise: Retrieve the position of the "most red", "most green" and "most blue" pixels of an image.

def getCloserPixel(picture, color):
# @param picture:Picture;
# @param color:Color;
  closerpx = None
  d = 442.0
  for px in getPixels(picture):
    pxcol = getColor(px)
    pxdis = distance(pxcol, color)
    if (pxdis < d):
      d = pxdis
      closerpx = px
  return closerpx

def printAnalysis(picture):
# @param picture:Picture;
  R = makeColor(255, 0, 0)
  G = makeColor(0, 255, 0)
  B = makeColor(0, 0, 255)
  pxR = getCloserPixel(picture, R)
  pxG = getCloserPixel(picture, G)
  pxB = getCloserPixel(picture, B)
  if (pxR == None):
    print "most-r: (-1, -1)"
    print "most-g: (-1, -1)"
    print "most-b: (-1, -1)"
  else:
    print "most-r: (%d, %d)" % (getX(pxR), getY(pxR))
    print "most-g: (%d, %d)" % (getX(pxG), getY(pxG))
    print "most-b: (%d, %d)" % (getX(pxB), getY(pxB))

def main():
  file = pickAFile()
  picture = makePicture(file)
  printAnalysis(picture)