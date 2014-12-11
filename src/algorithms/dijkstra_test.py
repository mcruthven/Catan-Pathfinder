import unittest
from dijkstra import DijkstraAlgorithm, DijkstraResourceAlgorithm

class node(object):
    def __init__(self, name=None, weight=1, neighbors=None, resources=[1,1,1,1]):
        self.name = name
        self.weight = weight
        self.v_refs = neighbors if neighbors else []
        self.resources = resources    
    def __repr__(self):
        return self.name
    
    def add_neighbors(self, neighbors):
        for neighbor in neighbors:
            self.v_refs.append(neighbor)

class TestDijkstra(unittest.TestCase):
    def setUp(self):
        self.e = node('e')
        self.c = node('c')
        self.b = node('b', neighbors=[self.e])
        self.a = node('a', neighbors=[self.b, self.c])
        self.d = node('d', neighbors=[self.e])
        self.c.add_neighbors([self.d]) 
        self.G = [self.a, self.b, self.c, self.d, self.e]

    def test_basic(self):
        self.a.add_neighbors([self.e])
        algorithm = DijkstraAlgorithm(self.G, self.a, self.e)
        path = algorithm.find_path(self.G, self.a, self.e)
        self.assertEqual([self.a, self.e], path)

    def test_change_source(self):
        self.a.add_neighbors([self.e])
        algorithm = DijkstraAlgorithm(self.G, self.a, self.e)
        path = algorithm.find_path(self.G, self.d, self.e)
        self.assertEqual([self.d, self.e], path)

    def test_change_target(self):
        self.a.add_neighbors([self.e])
        algorithm = DijkstraAlgorithm(self.G, self.a, self.e)
        path = algorithm.find_path(self.G, self.a, self.b)
        self.assertEqual([self.a, self.b], path)

    def test_alternate(self):
        self.b.weight = 4
        algorithm = DijkstraAlgorithm(self.G, self.a, self.e)
        path = algorithm.find_path(self.G, self.a, self.e)
        self.assertEqual([self.a, self.c, self.d, self.e], path)

    def test_path(self):
        algorithm = DijkstraAlgorithm(self.G, self.a, self.e)
        path = algorithm.find_path(self.G, self.a, self.e)
        self.assertEqual([self.a, self.b, self.e], path)

    def test_basic_resource(self):
        self.a.add_neighbors([self.e])

        self.algorithm = DijkstraResourceAlgorithm(self.G, self.a, self.e)
        path = self.algorithm.find_path(self.G, self.a, self.e)
        self.assertEqual([self.a, self.e], path)

    def test_alternate_resource(self):
        self.b.resources = [3, 3, 3, 3]

        self.algorithm = DijkstraResourceAlgorithm(self.G, self.a, self.e)
        path = self.algorithm.find_path(self.G, self.a, self.e)
        self.assertEqual([self.a, self.c, self.d, self.e], path)

    def test_path_resource(self):
        self.algorithm = DijkstraResourceAlgorithm(self.G, self.a, self.e)
        path = self.algorithm.find_path(self.G, self.a, self.e)
        self.assertEqual([self.a, self.b, self.e], path)
    # TODO: make better resource tests

if __name__ == "__main__":
    unittest.main()
