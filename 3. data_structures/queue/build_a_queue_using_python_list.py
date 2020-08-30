"""
Before we start let us reiterate the key components of a queue.

A queue is a data structure that consists of two main operations: enqueue and dequeue. 

Enqueue is when you add a element to the tail of the queue and a pop is when you remove an element from the head of the queue. 

Python 3.x conveniently allows us to demonstate this functionality with a list. 
When you have a list such as [2,4,5,6] you can decide which end of the list is the front and the back of the queue respectively.

Once you decide that, you can use the append, pop or insert function to simulate a queue.

We will choose the first element to be the front of our queue and therefore be using the append and pop functions to simulate it. Give it a try by implementing the function below!
"""

class Queue:
    def __init__(self):
         self.values = []
    
    def size(self):
         return len(self.values)
    
    def enqueue(self, item):
         self.values.append(item)

    def dequeue(self):
        return self.value.pop(0)
