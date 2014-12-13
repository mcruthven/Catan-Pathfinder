class DijkstraPathAlgorithm(object):

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
        self.dist[source] = [self.minimum]
        self.previous = {}

        # build distance and previous node dictionaries
        for v in self.G:
            if v != self.source:
                self.dist[v] = [self.large_number]
            self.previous[v] = {}

    def dijkstra(self, length):
        unvisited_nodes = set(self.G)

        while len(unvisited_nodes):
            # pick the node closest to source that has not been picked
            min_dist = [None, [self.large_number], self.large_number]

            for n in unvisited_nodes:
                x = min(self.dist[n])
                if x <= min_dist[2]:
                    min_dist = [n, self.dist[n], min(self.dist[n])]
            u = min_dist[0]
            unvisited_nodes.remove(u) # remove the node you picked from unvisited_nodes

            v_refs = self.get_refs(u)
            for v in v_refs:
                if v:
                    alt = self.update_distance(self.dist[u])
                    # update dist of the neighbor if this route is less than the length
                    for val in alt:
                        if val <= length:
                            self.dist[v] = [] if self.dist[v] == [self.large_number] else self.dist[v]
                            self.dist[v].append(val)
                            if u not in self.previous[v]:
                                self.previous[v][u] = [val]
                            else:
                                self.previous[v][u].append(val)

    def find_path(self, G, source, target, length, recalculate=False):
        """Return the path to target from the source node
        Inputs:
            G - a list containing all nodes in the graph
            source - start node for the path
            target - node to end at
        """
        if target != self.target:
            self.target = target
        if source != self.source or G != self.G or recalculate:
            self.reset(G, source, target)
            self.dijkstra(length)
        print G
        for g in G:
            print (g, g.v_refs)
        print 'previous', self.previous
        print self.dist
        paths = []
        for v, lengths in self.previous[target].items():
            p= [self.target, v]
            for length in lengths:
                paths.append([length - 1, p + [0 for i in range(length-1)]])
        self.parse_paths(self.target, paths)
        print paths

    def parse_paths(self, v, paths):
        if v == self.source:
            return
        for vertex, lengths in  self.previous[v].items():
            for length in lengths:
                for path in paths:
                    if path[0] == length and path[1][-(length -1)] == v:
                        path[1][-length] = vertex
                        path[0] = path[0] - 1
                self.parse_paths(vertex, paths)

    @staticmethod
    def get_refs(v):
        return v.v_refs

    @staticmethod
    def update_distance(x):
        return [i + 1 for i in x]

    @staticmethod
    def compare(x, y):
        return x[-1] <= y[-1]


