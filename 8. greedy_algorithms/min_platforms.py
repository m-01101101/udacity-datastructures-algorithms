"""
Given arrival and departure times of trains on a single day in a railway platform,
find out the minimum number of platforms required
so that no train has to wait for the other(s) to leave.
In other words, when a train is about to arrive, at least one platform must be available to accommodate it.

You will be given arrival and departure times both in the form of a list. 
The size of both the lists will be equal, with each common index representing the same train. 
Note: Time `hh:mm` would be written as integer `hhmm` for e.g. `9:30` would be written as `930`.

Example
Input:  A schedule of 6 trains:
arrival = [900,  940, 950,  1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]

Expected output: Minimum number of platforms required = 3
"""
from typing import List

def min_platforms(arrival: List[int], departure: List[int]) -> int:
    if(len(arrival) != len(departure)): # Mismatch in the length of the lists
        return -1

    # Sort both the lists.    
    arrival.sort()
    departure.sort()
    
    platform_required = 1              # Count of platforms required at the moment when comparing i^th arrival and j^th departure
    max_platform_required = 1          # Keep track of the max value of platform_required

    # Iterate such that (i-j) will represent platform_required at that moment
    i = 1
    j = 0

    # Traverse the arrival list with iterator `i`, and departure with iterator `j`.
    while i < len(arrival) and j < len(arrival):
        
        # if i^th arrival is scheduled before than j^th departure, 
        # increment platform_required and i as well.
        print(f"new arrival: {arrival[i]}, departure: {departure[j]}")
        if arrival[i] < departure[j]:
            platform_required += 1
            i += 1

            # Update the max value of platform_required
            if platform_required > max_platform_required:
                max_platform_required = platform_required
         
        # Otherwise, decrement platform_required count, and increase j.
        else:
            platform_required -= 1
            j += 1

    return max_platform_required

arrival1 = [200, 210, 300, 320, 350, 500]
departure1 = [230, 340, 320, 430, 400, 520]  
assert min_platforms(arrival1, departure1) == 2


arrival2 = [900,  940, 950,  1100, 1500, 1800]
departure2 = [910, 1200, 1120, 1130, 1900, 2000]
assert min_platforms(arrival2, departure2) == 3