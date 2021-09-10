class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.children = []

    def add_child(self, new_node):
        self.children.append(new_node)

    def remove_child(self, del_node):
        self.children.remove(del_node) if del_node in self.children else None

    # def __repr__(self):
    #     return f"Node {self.value}, Children {self.children}"


class Graph(object):
    def __init__(self, node_list):
        self.nodes = node_list

    def add_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(node2)
            node2.add_child(node1)

    def remove_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.remove_child(node2)
            node2.remove_child(node1)

    # def __str__(self):
    #     return f"{self.nodes}"


def dfs_search_iterative(root_node, search_value):
    """Return the GraphNode with the value == search_value"""
    visited = set()  # Sets are faster for lookups
    stack = [root_node]  # Start with a given root node

    while len(stack) > 0:  # Repeat until the stack is empty

        current_node = stack.pop()  # Pop out a node added recently
        visited.add(current_node)  # Mark it as visited

        if current_node.value == search_value:
            return current_node

        # Check all the neighbours
        for child in current_node.children:

            # If a node hasn't been visited before, and not available in the stack already.
            if (child not in visited) and (child not in stack):
                stack.append(child)


def dfs_search_recursive(start_node, search_value):
    """Return the GraphNode with the value == search_value"""
    visited = set()  # Set to keep track of visited nodes.
    return dfs_recursion(start_node, visited, search_value)


# Recursive function
def dfs_recursion(node, visited, search_value):
    # Base case, don't search in other branches if found = True
    if node.value == search_value:
        found = True
        return node

    visited.add(node)
    found = False
    result = None

    # Conditional recurse on each neighbour
    for child in node.children:
        if child not in visited:
            result = dfs_recursion(child, visited, search_value)
            # Once the match is found, no more recursion
            if found:
                break
    return result


# create a graph
nodeG = GraphNode("G")
nodeR = GraphNode("R")
nodeA = GraphNode("A")
nodeP = GraphNode("P")
nodeH = GraphNode("H")
nodeS = GraphNode("S")

graph1 = Graph([nodeS, nodeH, nodeG, nodeP, nodeR, nodeA])
graph1.add_edge(nodeG, nodeR)
graph1.add_edge(nodeA, nodeR)
graph1.add_edge(nodeA, nodeG)
graph1.add_edge(nodeR, nodeP)
graph1.add_edge(nodeH, nodeG)
graph1.add_edge(nodeH, nodeP)
graph1.add_edge(nodeS, nodeR)

# To verify that the graph is created accurately.
# Let's just print all the parent nodes and child nodes.
for each in graph1.nodes:
    print("parent node = ", each.value, end="\nchildren\n")
    for each in each.children:
        print(each.value, end=" ")
    print("\n")


assert nodeA == dfs_search_iterative(nodeS, "A")
assert nodeS == dfs_search_iterative(nodeP, "S")
assert nodeR == dfs_search_iterative(nodeH, "R")

assert nodeA == dfs_search_recursive(nodeG, "A")
assert nodeA == dfs_search_recursive(nodeS, "A")
assert nodeS == dfs_search_recursive(nodeP, "S")
assert nodeR == dfs_search_recursive(nodeH, "R")
