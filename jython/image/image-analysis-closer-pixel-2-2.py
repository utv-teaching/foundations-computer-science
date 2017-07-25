# Foundations of Computer Science
# BSc Computer Engineering, University of Rome Tor Vergata
# Exercise: Retrieve the position of the "most red", "most green" and "most blue" pixels of an image.
 
def getCloserPixel(picture):
# @param picture:Picture;
  R = makeColor(255, 0, 0)
  G = makeColor(0, 255, 0)
  B = makeColor(0 ,0, 255)
  dR = 442.0
  dG = 442.0
  dB = 442.0
  xR = -1
  yR = -1
  xG = -1
  yG = -1
  xB = -1
  yB = -1
  for px in getPixels(picture):
  	x = getX(px)
  	y = getY(px)
	pxc = getColor(px)
	dpxR = distance(pxc, R)
	dpxG = distance(pxc, G)
	dpxB = distance(pxc, B)
	if dpxR < dR:
	  dR = dpxR
	  xR = x
	  yR = y
	if dpxG < dG:
	  dG = dpxG
	  xG = x
	  yG = y
	if dpxB < dB:
	  dB = dpxB
	  xB = x
	  yB = y

  return (xR, yR, xG, yG, xB, yB) 
       
def printAnalysis(picture):
# @param picture:Picture;
  res = getCloserPixel(picture)
  print "most-r: (%d, %d)" % (res[0], res[1])
  print "most-g: (%d, %d)" % (res[2], res[3])
  print "most-b: (%d, %d)" % (res[4], res[5])
 
def main():
  file = pickAFile()
  picture = makePicture(file)
  printAnalysis(picture)