import heapq

from typing import List
from helpers import Map  # map of the 2D space
from math import sqrt
from typing import NamedTuple

# udacity running 3.6 so does not support dataclass
class Path(NamedTuple):
    nodes: List[int]
    cumulative_cost: float  # g
    distance_to_goal: float  # h
    frontier_node: int


def euclidean_distance(source: List[float], destination: List[float]) -> float:
    """Calculates the euclidean distance between two coordinates (x,y)
    This will act as our admissable heuristic"""

    x1 = source[0]
    y1 = source[1]

    x2 = destination[0]
    y2 = destination[1]

    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def shortest_path(M: Map, start: int, goal: int) -> List[int]:
    """Return a list that represents the shortest path from start to goal"""

    if start == goal:
        return [start]

    nodes_coordinates = M.intersections
    goal_xy = nodes_coordinates[goal]
    start_to_fin = euclidean_distance(nodes_coordinates[start], goal_xy)
    _total_cost = float(
        "inf"
    )  # placeholder to tracking minimum cost to goal for paths that include the goal node
    _short_path = None  # placeholder for list of nodes representing short path
    visited = set()
    paths = []
    path = Path([start], 0, start_to_fin, start)
    heapq.heappush(paths, path)
    visited.add(start)

    while paths:
        _path = heapq.heappop(paths)
        frontier = _path.frontier_node
        frontier_path = M.roads[frontier]

        for road in frontier_path:

            if road in visited:
                continue

            nodes_in_path = _path.nodes + [road]  # append

            cumulative_cost = (
                euclidean_distance(nodes_coordinates[frontier], nodes_coordinates[road])
                + _path.cumulative_cost
            )
            distance_to_goal = euclidean_distance(nodes_coordinates[road], goal_xy)
            f_cost = cumulative_cost + distance_to_goal

            new_path = Path(
                nodes_in_path, cumulative_cost, distance_to_goal, road
            )

            visited.add(road)

            if road == goal:
                if f_cost < _total_cost:
                    _total_cost = f_cost
                    _short_path = new_path.nodes
            else:  # goal not found, keep exploring
                heapq.heappush(paths, new_path)

    return _short_path if _short_path is not None else -1
