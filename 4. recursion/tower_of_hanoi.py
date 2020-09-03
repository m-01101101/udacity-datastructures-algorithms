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

num_disks = 3
1. move disk from source to destination
2. move disk from source to auxiliary
3. move disk from destination to auxiliary
4. move disk from source to destination
5. move disk from auxiliary to source
6. move disk from auxiliary to destination
7. move disk from source to destination

Print
S D
S A
D A
S D
A S
A D
S D

function
1. arg1 - number of disks
2. arg2 - rod A - this rod acts as the source 
    (at the time of calling the function)
2. arg3 - rod B - this rod acts as the auxiliary
2. arg4 - rod C - this rod acts as the destination
"""

def tower_of_Hanoi(num_disks):
    """
    :param: num_disks - number of disks
    TODO: print the steps required to move all disks from source to destination

    num_disks == 1. This must be the termination condition

    For num_disks > 1, just think of your FIRST set of steps. 
    You want to pick the bottom most disk on the source, to be transferred to the destination. 
    For this reason, you will will perform the steps below:
    Step 1: Move num_disks - 1 from source to auxiliary
    Step 2: Now you are left with only the largest disk at source. 
    Move the only leftover disk from source to destination
    Step 3: You had num_disks - 1 disks available on the auxiliary, as a result of Step 1. 
    Move num_disks - 1 from auxiliary to destination
    """

    """
    treat each disk as a node
    and each column as a stack
    """
    source = [d for d in range(1, num_disks + 1)][::-1]

    auxiliary = []

    destination = []

    return tower_of_Hanoi_func(num_disks, source, auxiliary, destination)

def tower_of_Hanoi_func(num_disks, source, auxiliary, destination):

    if len(source) == 1:  # base case
        disk = source.pop()
        destination.append(disk)

    else:
        disk = source.pop()

        if len(auxiliary) == 0 or disk < auxiliary[-1]:
            auxiliary.append(disk)
        elif disk < destination[-1]:
            destination.append(disk)

        if len(destination) != 0:
            disk = destination.pop()
            if disk < auxiliary[-1]:
                auxiliary.append(disk)

        if len(auxiliary) != 0:
            disk = auxiliary.pop()
            if disk < source[-1]:
                source.append(disk)
            elif disk < destination[-1]:
                destination.append(disk)

        tower_of_Hanoi_func(num_disks - 1, source, auxiliary, destination)
    

    return source, auxiliary, destination

    # FOR MARTJIN *UNPACKING GENERALLY - HOW DOES IT WORK
    

# def binary_search(arr, target):
#     return binary_search_func(arr, 0, len(arr) - 1, target)

# def binary_search_func(arr, start_index, end_index, target):
#     if start_index > end_index:
#         return -1

#     mid_index = (start_index + end_index)//2

#     if arr[mid_index] == target:
#         return mid_index
#     elif arr[mid_index] > target:
#         return binary_search_func(arr, start_index, mid_index - 1, target)
#     else:
#         return binary_search_func(arr, mid_index + 1, end_index, target)    




# class LinkedListNode:

#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class Stack:

#     def __init__(self):
#         self.num_elements = 0
#         self.head = None

#     def push(self, data):
#         new_node = LinkedListNode(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node
#         self.num_elements += 1

#     def pop(self):
#         if self.is_empty():
#             return None
#         temp = self.head.data
#         self.head = self.head.next
#         self.num_elements -= 1
#         return temp

#     def top(self):
#         if self.head is None:
#             return None
#         return self.head.data

#     def size(self):
#         return self.num_elements

#     def is_empty(self):
#         return self.num_elements == 0