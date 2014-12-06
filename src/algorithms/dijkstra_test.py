from dijkstra import dijkstra, find_path

# This isnt finished
class node(object):
  def __init__(self, name=None, weight=1, neighbors=None):
    self.name = name
    self.weight = weight
    if neighbors:
      self.neighbors = neighbors
    else:
      self.neighbors = []
  
  def __repr__(self):
    return self.name
  
  def add_neighbor(self, neighbor):
    self.neighbors.append(neighbor)
  
a = node('a')
b = node('b',1, [a])
c = node('c',5)
a.add_neighbor(b)
a.add_neighbor(c)

G = [a,b,c]
#d, p = dijkstra(G, b)
print find_path(G, b, c)

