class DijkstraAlgorithm(object):

    def __init__(self):
        self.large_number = 1e4            # large number greater than any distance in the tree
        self.minimum = 0
        self.G = None
        self.source = None
        self.target = None

    def reset(self, G, source, target):
        self.G = G
        self.source = source
        self.target = target
        self.dist = {}
        self.dist[source] = self.minimum
        self.previous = {}

        # build distance and previous node dictionaries
        for v in self.G:
            if v != self.source:
                self.dist[v] = self.large_number
            self.previous[v] = None

    def dijkstra(self):
        unvisited_nodes = set(self.G)

        while len(unvisited_nodes):
            # pick the node closest to source that has not been picked
            min_dist = [None, self.large_number]

            for n in unvisited_nodes:
                if self.compare(self.dist[n], min_dist[1]):
                    min_dist = [n, self.dist[n]]
            u = min_dist[0]
            unvisited_nodes.remove(u) # remove the node you picked from unvisited_nodes

            v_refs = self.get_refs(u)
            for v in v_refs:
                if v:
                    alt = self.update_distance(self.dist[u], v)
                    # update dist of the neighbor if this is a closer route
                    if self.compare(alt, self.dist[v]):
                        self.dist[v] = alt
                        self.previous[v] = u

    def find_path(self, G, source, target):
        """Return the path to target from the source node
        Inputs:
            G - a list containing all nodes in the graph
            source - start node for the path
            target - node to end at
        """
        if target != self.target:
            self.target = target
        if source != self.source or G != self.G:
            self.reset(G, source, target)
            self.dijkstra()

        path = [self.target]
        u = self.target
        while self.previous[u]:
            u = self.previous[u]
            path.append(u)
        if path[-1] != self.source:
            raise ValueError('%s does not equal the expected start node, %s'
                             % (path[-1], self.source))
        return path[::-1]

    @staticmethod
    def get_refs(v):
        return v.v_refs

    @staticmethod
    def update_distance(x, v):
        return x + v.weight

    @staticmethod
    def compare(x, y):
        return x <= y

class DijkstraResourceAlgorithm(DijkstraAlgorithm):

    def __init__(self):
        DijkstraAlgorithm.__init__(self)
        self.large_number = [1e4, 1e4, 1e4, 1e4] # large number greater than any distance in the tree
        self.minimum = [0, 0, 0, 0]

    @staticmethod
    def compare(x, y):
        return sum([v **2 for v in x]) <= sum([v**2 for v in y])

    @staticmethod
    def update_distance(x, v):
        return [res_val + v.resources[i] for i, res_val in enumerate(x)]

class DijkstraSettlementAlgorithm(DijkstraAlgorithm):

    @staticmethod
    def get_refs(v):
        return v.s_refs

class DijkstraSettlementAlgorithm(DijkstraAlgorithm):

    @staticmethod
    def get_refs(v):
        return v.s_refs
