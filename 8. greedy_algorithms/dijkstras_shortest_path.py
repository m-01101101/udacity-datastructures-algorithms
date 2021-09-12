"""
Using Dijkstra's algorithm, find the shortest path to all the nodes starting from a given single source node. 
You need to print the distance of each node from the given source node. 
For example, the distance of each node from `A` would be printed as:
>>> {'A': 0, 'D': 2, 'B': 5, 'E': 4, 'C': 3, 'F': 6}
"""
import sys
from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = set()                   # A set cannot contain duplicate nodes
        self.neighbours = defaultdict(list)  # Defaultdict is a child class of Dictionary that provides a default value for a key that does not exists.
        self.distances = {}                  # Dictionary. An example record as ('A', 'B'): 6 shows the distance between 'A' to 'B' is 6 units

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.neighbours[from_node].append(to_node)
        self.neighbours[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance    # lets make the graph undirected / bidirectional 
        
    def print_graph(self):
        print("Set of Nodes are: ", self.nodes)
        print("Neighbours are: ", self.neighbours)
        print("Distances are: ", self.distances)


def dijkstra(graph, source):
    """Find the shortest path from the source node to every other node in the given graph"""

    # Declare and initialize result, unvisited, and path
    result = {i: sys.maxsize if i != source else 0 for i in graph.nodes}  # placeholder, by default set distance to maxsize

    path = {}

    unvisited = set(graph.nodes)

    while unvisited:  # As long as unvisited is non-empty
        min_node = None
        # Find the unvisited node having smallest known distance from the source node.
        for node in unvisited:
            if min_node is None or result[node] < result[min_node]:  # base case
                min_node = node
            """tried to be fancy"""
                    # d = {i[0][1]: i[1] for i in graph.distances.items() if i[0][0] == node}
                    # min_node = min(d, key=d.get)
                    # result[min_node] = d[min_node]

        current_distance = result[min_node]

        # For the current node, find all the unvisited neighbours. 
        # For this, you have calculate the distance of each unvisited neighbour.

        # unvisited_neighbours =  unvisited.intersection(graph.neighbours[min_node])  does not work, might not be a path between nodes
        for neighbour in graph.neighbours[min_node]:
            if neighbour in unvisited:
                distance = current_distance + graph.distances[(min_node, neighbour)]
            # If the calculated distance of the unvisited neighbour is less than the already known distance in result dictionary,
            # update the shortest distance in the result dictionary.        
                if distance < result[neighbour]:
                    result[neighbour] = distance
                    path[neighbour] = min_node

        # Remove the current node from the unvisited set.
        unvisited.remove(min_node)

    # should do an ASSERT to check no values in result dict equal sys.maxsize

    return result


testGraph1 = Graph()
for node in ['A', 'B', 'C', 'D', 'E']:
    testGraph1.add_node(node)

testGraph1.add_edge('A','B',3)
testGraph1.add_edge('A','D',2)
testGraph1.add_edge('B','D',4)
testGraph1.add_edge('B','E',6)
testGraph1.add_edge('B','C',1)
testGraph1.add_edge('C','E',2)
testGraph1.add_edge('E','D',1)

assert dijkstra(testGraph1, 'A') == {'A': 0, 'D': 2, 'B': 3, 'E': 3, 'C': 4}