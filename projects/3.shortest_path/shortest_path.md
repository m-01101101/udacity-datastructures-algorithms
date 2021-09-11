# Notes

## Uniform cost search

Expands out equally in all directions, may expend additional effort getting to a fairly direct path to the goal.

- Start with an initial state
- Expand along different paths, adding the cumulative cost as we go
- We expand in terms of contours, like on a topological map, i.e. we are not exploring in a single direction
- We are not searching towards the goal but rather expanding out in the space in every direction. This guarantees we find the shortest path eventually
- When the space we are exploring is large, this can be a problem, as on average we'll have to assume we need to explore half the space to find the goal

<img src=../../md_refs/uniform_cost_search1.png width=50% />

## Greedy best-first search

In order to improve our ability to find the goal faster, we must first estimate the distance from our source to destination.

The greedy approach then allows us to expands outwards in incremental approaches that are estimated as closer to the goal. Our search is now directed.

<img src=../../md_refs/greedy_bestfirst_search1.png width=50% />

If a direct path is available, this expends much less effort than Uniform Cost; however, it does not consider any routes in which it may need to temporarily take a further away path in order to arrive at an overall shorter path (i.e. one step back, two steps forward).

For example, rather than going backwards, greedy best-first search will only ever go forward, resulting in a longer overall route;

<img src=../../md_refs/greedy_bestfirst_search2.png width=50% />

## A\* Search

Utilises both of these:

- Greedy search - which explores a small number of nodes in many cases
- Uniform cost search - which is guaranteed to find the shortest path

A\* Search works by always expanding to the path that has a minimum value of `f`

`f` is defined as the sum of `g` (cumulative cost) and `h` (estimated distance to the goal)

<img src=../../md_refs/a_star1.png width=50% />

Minimising `g` helps to keep the paths short. Minimising `h` ensures we are optimising towards finding the goal.

This ensures we find the shortest/cheapest length path, while expanding the minimum number of paths possible. Giving us the `best estimated total path cost first`.

A\* is not guaranteed to find the shortest path, it depends on the `h` function.
- A\* __will__ find the shortest path is `h(s)` is less than the true cost of taking the path
- You never want `h` to over estimate the distance to the goal. `h` is optimistic
- `h` must also be uniformly "wrong" 

### Implementation

From [The Algorithms](https://github.com/TheAlgorithms/Python/blob/master/graphs/a_star.py)

```Python
grid = [
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],  # 0 are free path whereas 1's are obstacles
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
]

"""
heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]"""

init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]  # all coordinates are given in format [y,x]
cost = 1

# the cost map which pushes the path closer to the goal
heuristic = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        heuristic[i][j] = abs(i - goal[0]) + abs(j - goal[1])
        if grid[i][j] == 1:
            heuristic[i][j] = 99  # added extra penalty in the heuristic map


# the actions we can take
delta = [[-1, 0], [0, -1], [1, 0], [0, 1]]  # go up  # go left  # go down  # go right


# function to search the path
def search(grid, init, goal, cost, heuristic):

    closed = [
        [0 for col in range(len(grid[0]))] for row in range(len(grid))
    ]  # the reference grid
    closed[init[0]][init[1]] = 1
    action = [
        [0 for col in range(len(grid[0]))] for row in range(len(grid))
    ]  # the action grid

    x = init[0]
    y = init[1]
    g = 0
    f = g + heuristic[x][y]  # cost from starting cell to destination cell
    cell = [[f, g, x, y]]

    found = False  # flag that is set when search is complete
    resign = False  # flag set if we can't find expand

    while not found and not resign:
        if len(cell) == 0:
            return "FAIL"
        else:  # to choose the least costliest action so as to move closer to the goal
            cell.sort()
            cell.reverse()
            next = cell.pop()
            x = next[2]
            y = next[3]
            g = next[1]

            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):  # to try out different valid actions
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            f2 = g2 + heuristic[x2][y2]
                            cell.append([f2, g2, x2, y2])
                            closed[x2][y2] = 1
                            action[x2][y2] = i
    invpath = []
    x = goal[0]
    y = goal[1]
    invpath.append([x, y])  # we get the reverse path from here
    while x != init[0] or y != init[1]:
        x2 = x - delta[action[x][y]][0]
        y2 = y - delta[action[x][y]][1]
        x = x2
        y = y2
        invpath.append([x, y])

    path = []
    for i in range(len(invpath)):
        path.append(invpath[len(invpath) - 1 - i])
    print("ACTION MAP")
    for i in range(len(action)):
        print(action[i])

    return path


a = search(grid, init, goal, cost, heuristic)
for i in range(len(a)):
    print(a[i])
```