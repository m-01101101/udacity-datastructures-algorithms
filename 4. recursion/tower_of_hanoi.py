"""
The Tower of Hanoi is a puzzle where we have three rods and n unique sized disks.
The three rods are - source, destination, and auxiliary (which sits between the other two)

The object is to move all the disk from source to destination.

The rules applicable to all rods;
1. Only one disk can be moved at a time.
2. A disk can be moved only if it is on the top of a rod.
3. No disk can be placed on the top of a smaller disk.

You will be given the number of disks num_disks as the input parameter.
Write a recursive function tower_of_Hanoi() 
that prints the "move" steps in order to move num_disks number of disks 
    from Source to Destination using the help of Auxiliary rod.

Assume the disks are stacks currently from smallest first to largest at the bottom of a stack
You have to re-stack them and then move onto destination
"""

def tower_of_Hanoi(num_disks):
    """
    :param: num_disks - number of disks

    d1    #        |        |
    d2   ###       |        |
    d3  #####      |        |
    d4 #######     |        |
         1         2        3

    move (dn, current, target, other) ->
    - move(dn - 1, current, other, target) 
    - dn -> target
    - move(dn - 1, other, current, target)
    """

    return tower_of_Hanoi_func(num_disks, source = [d for d in range(1, num_disks + 1)][::-1], auxiliary = [], destination= [])


def tower_of_Hanoi_func(num_disks, source, auxiliary, destination):

    if num_disks == 1:  # base case
        destination.append(source.pop())
        print('S', 'D')

    else:
        if num_disks % 2 != 0:
            auxiliary.append(source.pop())
            print('S', 'A')
            auxiliary = destination + auxiliary
            print('D', 'A') if len(destination) > 0 else None
            destination = []
        elif num_disks % 2 == 0:
            destination.append(source.pop())
            print('S', 'D')
            destination = auxiliary + destination
            print('A', 'D') if len(auxiliary) > 0 else None
            auxiliary = []
        return tower_of_Hanoi_func(num_disks - 1, source, auxiliary, destination)
    

    return source, auxiliary, destination


# Udacity solution
def tower_of_Hanoi_soln(num_disks, source, auxiliary, destination):
    
    if num_disks == 0:
        return
    
    if num_disks == 1:
        print("{} {}".format(source, destination))
        return
    
    tower_of_Hanoi_soln(num_disks - 1, source, destination, auxiliary)
    print("{} {}".format(source, destination))
    tower_of_Hanoi_soln(num_disks - 1, auxiliary, source, destination)
    
def tower_of_Hanoi(num_disks):
    tower_of_Hanoi_soln(num_disks, 'S', 'A', 'D')
