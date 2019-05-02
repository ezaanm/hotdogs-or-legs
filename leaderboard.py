import operator

class Leaderboard:

#self.scores = dict of user: scores (users are unique or score is overriden)
  def __init__(self):
      self.scores = {}
      print("let the games begin!")
      return

  def __sort__(self):
      print("sorting")

  def __top5__(self):
      sorted_scores = sorted(self.scores.items(), key=operator.itemgetter(-1), reverse=True)
      return sorted_scores[:4])

  def __all__(self):
      return self.scores

  def __add__(self, username, score):
      if username in self.scores.items():
          self.scores.update({username: score})
      else : 
          self.scores[username] = score
      return

#if we really wanted to make this nice you would only add user if > bottom of top 5

# l = Leaderboard()
# l.__add__("sara", 10)
# l.__add__("ez", 5)
# l.__add__("arun", 7)
# l.__add__("arun1", 8)
# l.__add__("arun2", 1)
# l.__top5__()