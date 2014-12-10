def dijkstra(G, source):
    """Find all paths to source
    Inputs:
        G - a list containing all nodes in the graph
        source - the source node
    """
    dist = {}
    dist[source] = 0
    large_number = 1e4            # large number greater than any distance in the    tree
    unvisited_nodes = set()
    previous = {}
    
    # build distance and previous node dictionaries    
    for v in G:
        if v != source:
            dist[v] = large_number    
        previous[v] = None
        unvisited_nodes.add(v)     
    

    while len(unvisited_nodes):
        # pick the node closest to source that has not been picked
        min_dist = [None, large_number]
        for n in unvisited_nodes:
            if dist[n] <= min_dist[1]:
                min_dist = [n, dist[n]]
        u = min_dist[0]
        unvisited_nodes.remove(u) # remove the node you picked from unvisited_nodes
        
        for v in u.v_refs:
            if v:
                alt = dist[u] + v.weight
                # update dist of the neighbor if this is a closer route
                if alt < dist[v]:             
                    dist[v] = alt
                    previous[v] = u
    return dist, previous
 
def find_path(G, source, target):
    """Return the path to target from the source node
    Inputs:
        G - a list containing all nodes in the graph
        source - start node for the path
        target - node to end at
    """
    _, previous = dijkstra(G, source)
    path = [target]
    u = target
    while previous[u]:
        u = previous[u]
        path.append(u)

    if path[-1] != source:
        raise ValueError('%s does not equal the expected start node, %s' 
                         % (path[-1], source))
    return path[::-1]
 
