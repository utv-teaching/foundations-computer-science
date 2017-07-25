# Foundations of Computer Science
# BSc Computer Engineering, University of Rome Tor Vergata
# Exercise: Check if two pictures contain twin pixels.

def areTwins(px1, px2):
#@param px1: pixel
#@param px2: pixel  
#@return bool (true or false) 
  r1=getRed(px1)
  g1=getGreen(px1)
  b1=getBlue(px1)
  r2=getRed(px2)
  g2=getGreen(px2)
  b2=getBlue(px2)
  if (r1 + g1 + b1 == r2 + g2 + b2):
    return true;
  return false 

def existsTwin(px1, pic2):
#@ param px1: pixel
#@ param pic2: picture
#@return bool (true or false) 
  for px2 in getPixels(pic2):
    if areTwins(px1, px2):
      return true
  return false
 
def checkTwin(pic1, pic2):
#@param pic1: picture
#@param pic2: picture  
#@return bool (true or false) 
  for px1 in getPixels(pic1):
    if not existsTwin(px1, pic2):
      return false
  return true
  
def main():
  pic1 = makePicture(pickAFile())
  pic2 = makePicture(pickAFile())
  res = checkTwin(pic1, pic2)
  print res