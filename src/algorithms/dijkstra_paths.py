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
        self.dist[source] = [[self.minimum, [self.source]]]
        self.previous = {}

        # build distance and previous node dictionaries
        for v in self.G:
            if v != self.source:
                self.dist[v] = [[self.large_number, []]]
            self.previous[v] = {}

    def find_min(self, paths):
        minimum = self.large_number
        for l, p in paths:
            if minimum >= l:
                minimum = l
        return minimum

    def dijkstra(self, length):
        unvisited_nodes = set(self.G)

        while len(unvisited_nodes):
            # pick the node closest to source that has not been picked
            min_dist = [None, self.large_number]

            for n in unvisited_nodes:
                x = self.find_min(self.dist[n])
                if x <= min_dist[1]:
                    min_dist = [n, self.find_min(self.dist[n])]
            u = min_dist[0]
            unvisited_nodes.remove(u) # remove the node you picked from unvisited_nodes
            v_refs = self.get_refs(u)
            for v in v_refs:
                if v:
                    alt = self.update_distance(self.dist[u], v)
                    # add path option if it is less than the max length
                    for val in alt:
                        if val[0] <= length:
                            if self.dist[v] == [[self.large_number, []]]:
                                self.dist[v] = []
                            self.dist[v].append(val)
                            if u not in self.previous[v]:
                                self.previous[v][u] = [val]
                            else:
                                self.previous[v][u].append(val)

    def find_all_paths(self, G, source, target, length, recalculate=False):
        """Return the path to target from the source node
        Inputs:
            G - a list containing all nodes in the graph
            source - start node for the path
            target - node to end at
            length - max length of paths
        """
        if target != self.target:
            self.target = target
        if source != self.source or G != self.G or recalculate:
            self.reset(G, source, target)
            self.dijkstra(length)
        return [p for l, p in self.dist[target]]

    @staticmethod
    def get_refs(v):
        return v.v_refs

    @staticmethod
    def update_distance(x, v):
        return [[i + 1, p + [v]] for i, p in x if v not in p]


