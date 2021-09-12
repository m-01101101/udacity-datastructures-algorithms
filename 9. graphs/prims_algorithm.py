"""
# Connect Islands using Prim’s Algorithm
### Problem Statements

In an ocean, there are `n` islands some of which are connected via bridges. 
Travelling over a bridge has some cost attached with it. 
Find bridges in such a way that all islands are connected with minimum cost of travelling. 

You can assume that there is at least one possible way in which all islands are connected with each other. 

You will be provided with two input parameters:
    
1. `num_islands` = number of islands
    
2. `bridge_config` = list of lists. 
    Each inner list will have 3 elements:
        a. island A
        b. island B
        c. cost of bridge connecting both islands
                       
    Each island is represented using a number
     
**Example:**                       
* `num_islands = 4`
* `bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]`
       
Input parameters explanation:
    1. Number of islands = 4
    2. Island 1 and 2 are connected via a bridge with cost = 1
       Island 2 and 3 are connected via a bridge with cost = 4
       Island 1 and 4 are connected via a bridge with cost = 3
       Island 4 and 3 are connected via a bridge with cost = 2
       Island 1 and 3 are connected via a bridge with cost = 10
       
In this example if we are connecting bridges like this...
* between 1 and 2 with cost = 1
* between 1 and 4 with cost = 3
* between 4 and 3 with cost = 2  

...then we connect all 4 islands with `cost = 6` which is the minimum traveling cost.

### Tips
Using the `heapq` module, you can convert an existing list of items into a min-heap. The following two functionalities can be very handy for this problem:

1. `heappush(heap, item)` — add `item` to the `heap`
2. `heappop(heap)` — remove the smallest item from the `heap`

# initialize an empty list 
minHeap = list()

# pop and return smallest element from the heap
smallest = heapq.heappop(minHeap)


### The Idea, based on Prim’s Algorithm:
Our objective is to find the minimum `total_cost` to visit all the islands. 
We will start with any one island, and follow a Greedy approach.

**Step 1 -  Create a Graph**
1. Create a graph with given number of islands, and the cost between each pair of islands. A graph can be represented as a adjacency_matrix, which is a list of lists. For example, given:<br>

```
num_islands = 4
bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
```

The graph would look like:
```
graph =  [[], [(2, 1), (4, 3), (3, 10)], [(1, 1), (3, 4)], [(2, 4), (4, 2), (1, 10)], [(1, 3), (3, 2)]]
```
where, a sublist at $i^{th}$ index represents the adjacency_list of $i^{th}$ island. A tuple within a sublist is `(neighbor, edge_cost)`. <br>

**Step 2 - Traverse the graph in a Greedy way.** <br>  
1. Create a blank `minHeap`, and push any one island (vertex) into it.  
1. While there are elements remaining in the `minHeap`, do the following:
 - Pop out an island having smallest edge_cost, and reduce the heap size. You can use `heapq.heappop()` for this purpose. 
 - If the current island has not been visited before, add the `edge_cost` to the `total_cost`. You can use a list of booleans to keep track of the visited islands.  
 - Find out all the neighbours of the current island from the given `graph`. Push each neighbour of the current island into the `minHeap`. You can use `heapq.heappush()` for this purpose. 
 - Mark current island as visited
 tuple in the adjacency_list of the 

1. When we have popped out all the elements from the `minHeap`, we will have the minimum `total_cost` to visit all the islands.
"""

"""

"""

import heapq  # use heapq to create a custom priority queue


def create_graph(num_islands, bridge_config):
    """
    Helper function to create graph using adjacency list implementation
    """
    # A graph can be represented as a adjacency_list, which is a list of blank lists
    graph = [list() for _ in range(num_islands + 1)]

    # populate the adjacency_list
    for config in bridge_config:
        source = config[0]
        destination = config[1]
        cost = config[2]

        # An entry in a sublist of graph is represented as a tuple (neighbor, edge_cost)
        graph[source].append((destination, cost))
        graph[destination].append((source, cost))

    # Try this: print("graph = ",graph)
    return graph


def minimum_cost(graph):
    """
    Helper function to find minimum cost of connecting all islands
    """

    # start with vertex 1 (any vertex can be chosen)
    start_vertex = 1

    # initialize a list to keep track of vertices that are visited
    visited = [False for _ in range(len(graph) + 1)]

    # Heap is represented as a list of tuples
    # A "node" in heap is represented as tuple (edge_cost, neighbor)
    minHeap = [(0, start_vertex)]
    total_cost = 0

    while minHeap:
        # Here, heapq.heappop() will automatically pop out the "node" having smallest edge_cost, and reduce the heap size
        cost, current_vertex = heapq.heappop(minHeap)

        # check if current_vertex is already visited
        if visited[current_vertex]:
            continue

        # else add cost to total-cost
        total_cost += cost

        for neighbor, edge_cost in graph[current_vertex]:
            heapq.heappush(minHeap, (edge_cost, neighbor))

        # mark current vertex as visited
        visited[current_vertex] = True

    return total_cost


def get_minimum_cost_of_connecting(num_islands, bridge_config):
    graph = create_graph(num_islands, bridge_config)
    return minimum_cost(graph)


def test_function(test_case):
    num_islands = test_case[0]
    bridge_config = test_case[1]
    solution = test_case[2]
    output = get_minimum_cost_of_connecting(num_islands, bridge_config)

    if output == solution:
        print("Pass")
    else:
        print("Fail")


# test case 1
num_islands = 4
bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
solution = 6

test_case = [num_islands, bridge_config, solution]
test_function(test_case)

# test case 2
num_islands = 5
bridge_config = [[1, 2, 5], [1, 3, 8], [2, 3, 9]]
solution = 13

test_case = [num_islands, bridge_config, solution]
test_function(test_case)

# test case 3
num_islands = 5
bridge_config = [[1, 2, 3], [1, 5, 9], [2, 3, 10], [4, 3, 9]]
solution = 31

test_case = [num_islands, bridge_config, solution]
test_function(test_case)
