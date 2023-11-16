from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
        current = frontier.pop()
        for neighbor in graph[current]:
            if neighbor not in result:
                result.add(neighbor)
                frontier.add(neighbor)
        ###TODO
        pass
    return result





def connected(graph):
    if not graph:
        return False  
    start_node = list(graph)[0]
    reachable_nodes = reachable(graph, start_node)
    connect = len(reachable_nodes) == len(graph)
    return connect
    ### TODO
    pass




def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    if not graph:
        return 0

    visited = set()
    components = 0

    for node in graph:
        if node not in visited:
            components += 1
            reachable_nodes = reachable(graph, node)
            visited.update(reachable_nodes)

    return components
    ### TODO
    pass

