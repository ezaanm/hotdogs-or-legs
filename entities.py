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
    
class Leaderboard:
  def __init__(self):
    self.timeArr = []
    
  def put(self, name, time):
    if len(self.timeArr) > 0 and time < self.timeArr[-1][1]:
      if len(self.timeArr) == 5:
        self.timeArr[-1] = (name, time)
      else:
        self.timeArr.append((name, time))
        
      self.timeArr = sorted(self.timeArr, key=lambda x: x[1])
    elif len(self.timeArr) == 0:
      self.timeArr.append((name, time))
      
  def __str__(self):
      return str(self.timeArr)
      
  def html(self):
    string = ""
    for t in self.timeArr:
      string += "<li>" + str(t) + "</li>"
    
    return string