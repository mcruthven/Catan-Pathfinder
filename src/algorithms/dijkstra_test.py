from dijkstra import dijkstra, find_path

# This isnt finished
class node(object):
  def __init__(self, name=None, neighbors=None):
    self.name = name
    if neighbors:
      self.neighbors = neighbors
      self.neighbor_names = [n.name for n, d in neighbors]
    else:
      self.neighbors = []
      self.neighbor_names = []
  
  def __repr__(self):
    return self.name
  
  def add_neighbor(self, neighbor, dist):
    self.neighbors.append([neighbor, dist])
    self.neighbor_names.append(neighbor.name)
  
a = node('a')
b = node('b', [[a, 1]])
c = node('c')
a.add_neighbor(b, 1)
a.add_neighbor(c ,5)

G = [a,b,c]
#d, p = dijkstra(G, b)
print find_path(G, b, c)

