import unittest
from dijkstra import dijkstra, find_path

class node(object):
    def __init__(self, name=None, weight=1, neighbors=None):
        self.name = name
        self.weight = weight
        self.v_refs = neighbors if neighbors else []
    
    def __repr__(self):
        return self.name
    
    def add_neighbors(self, neighbors):
        for neighbor in neighbors:
            self.v_refs.append(neighbor)

class TestDijkstra(unittest.TestCase):

    def setUp(self):
        self.a = node('a')
        self.b = node('b')
        self.c = node('c')
        self.d = node('d')
        self.e = node('e')
        self.G = [self.a, self.b, self.c, self.e, self.d]

    def test_basic(self):
        self.c.weight = 5
        self.a.add_neighbors([self.b, self.c]) 
        self.b.add_neighbors([self.a]) 
        path = find_path(self.G, self.b, self.c)
        self.assertEqual([self.b, self.a, self.c], path)

    def test_alternate(self):
        self.b.weight = 3
        self.a.add_neighbors([self.b, self.c]) 
        self.b.add_neighbors([self.e]) 
        self.c.add_neighbors([self.d]) 
        self.d.add_neighbors([self.e]) 
        path = find_path(self.G, self.a, self.e)
        self.assertEqual([self.a, self.c, self.d, self.e], path)

    def test_path(self):
        self.a.add_neighbors([self.b, self.c]) 
        self.b.add_neighbors([self.e]) 
        self.b.add_neighbors([None])
        self.c.add_neighbors([self.d]) 
        self.d.add_neighbors([self.e]) 
        path = find_path(self.G, self.a, self.e)
        self.assertEqual([self.a, self.b, self.e], path)

if __name__ == "__main__":
    unittest.main()
