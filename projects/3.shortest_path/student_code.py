from typing import List
from helpers import Map
from math import sqrt

def distance(source: List[float, float], destination: List[float, float]) -> float:
    """Calculates the euclidean distance between two coordinates"""

    x1 = source[0]
    y1 = source[1]
    
    x2 = destination[0]
    y2 = destination[1]
    
    return sqrt((x1-x2)**2 + (y1-y2)**2)    

# def shortest_path(M: Map, start: int, goal: int) -> List[int]:
#     print("shortest path called")
#     return