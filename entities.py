class HotDog:
  def __init__(self):
    self.dogCount = 1
  
  def eat(self):
    print("no sauce? brooooooo")
    
  def __str__(self):
    return("HotDog with " + str(self.dogCount) + " weiners")
    
  def __add__(self, other):
    if isinstance(other, HotDog):
      print("additional weiner added")
      self.dogCount += 1
      return self
  
class Legs:
  def eat(self):
    print("thats now how these work")
    
  def __str__(self):
    return("2 Legs")