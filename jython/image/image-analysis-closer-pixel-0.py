# Foundations of Computer Science
# BSc Computer Engineering, University of Rome Tor Vergata
# Exercise: Retrieve the position of the "most red", "most green" and "most blue" pixels of an image.

def getPicture(file):
  picture = makePicture(file)
  return picture

def selectPicture():
  file = pickAFile()
  picture = getPicture(file)
  return picture

def getRedCloserPixel(picture):
  x = getX(getPixels(picture)[0])
  y = getY(getPixels(picture)[0])
  d = distance(makeColor(255, 0, 0), getColor(getPixels(picture)[0]))
  for px in getPixels(picture):
    pxd = distance(makeColor(255, 0, 0), getColor(px))
    if (pxd < d):
      d = pxd
      x = getX(px)
      y = getY(px)
    else:
      d = d
      x = x
      y = y
  return (x, y)

def getGreenCloserPixel(picture):
  x = getX(getPixels(picture)[0])
  y = getY(getPixels(picture)[0])
  d = distance(makeColor(0, 255, 0), getColor(getPixels(picture)[0]))
  for px in getPixels(picture):
    pxd = distance(makeColor(0, 255, 0), getColor(px))
    if (pxd < d):
      d = pxd
      x = getX(px)
      y = getY(px)
    else:
      d = d
      x = x
      y = y
  return (x, y)

def getBlueCloserPixel(picture):
  x = getX(getPixels(picture)[0])
  y = getY(getPixels(picture)[0])
  d = distance(makeColor(0, 0, 255), getColor(getPixels(picture)[0]))
  for px in getPixels(picture):
    pxd = distance(makeColor(0, 0, 255), getColor(px))
    if (pxd < d):
      d = pxd
      x = getX(px)
      y = getY(px)
    else:
      d = d
      x = x
      y = y
  return (x, y)

def printDetails(picture):
  print "most-r: %s" % (getRedCloserPixel(picture),)
  print "most-g: %s" % (getGreenCloserPixel(picture),)
  print "most-b: %s" % (getBlueCloserPixel(picture),)
    
def main():
  picture = selectPicture()
  printDetails(picture)