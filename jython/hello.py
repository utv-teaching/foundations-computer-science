def standardHello():
print "Hello world!"	
  
def customHello(sentence):
print sentence

def customNamedHello(name, sentence):
print "Hi! My name is %s, %s" % (name, sentence)

def main():
standardHello();
customHello("Bye bye cruel world!")
customNamedHello("Giacomo", "and yours?")