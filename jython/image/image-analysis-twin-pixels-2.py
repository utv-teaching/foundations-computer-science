# Foundations of Computer Science
# BSc Computer Engineering, University of Rome Tor Vergata
# Exercise: Check if two pictures contain twin pixels.

def getColors(pic):
#@param pic: picture
#@return {color}: colors
  colors = []
  for px in getPixels(pic):
    colpx = getColor(px)
    if colpx not in colors:
      colors.append(colpx)
  return colors

def areTwins(col1, col2):
#@param col1: color
#@param col2: color  
#@return bool (true or false) 
  r1 = col1.getRed()
  g1 = col1.getGreen()
  b1 = col1.getBlue()
  r2 = col2.getRed()
  g2 = col2.getGreen()
  b2 = col2.getBlue()
  if (r1 + g1 + b1 == r2 + g2 + b2):
    return true;
  return false 

def existsTwinInPicture(col1, pic2):
#@ param col1: color
#@ param pic2: picture
#@return bool (true or false) 
  for px2 in getPixels(pic2):
    col2 = getColor(px2)
    if areTwins(col1, col2):
      return true
  return false
 
def checkTwin(pic1, pic2):
#@param pic1: picture
#@param pic2: picture  
#@return bool (true or false) 
  colors1 = getColors(pic1)
  for col1 in colors:
    if not existsTwinInPicture(col1, pic2):
      return false
  return true
  
def main():
  pic1 = makePicture(pickAFile())
  pic2 = makePicture(pickAFile())
  res = checkTwin(pic1, pic2)
  print res