# TODO revisit heap implementation
class Heap:
    """Min heap implementation"""

    def __init__(self):
        self.storage = []  # initialise array
        self.heap_size = 0  # len(self.storage) does not work

    def __repr__(self) -> str:
        return "".join(
            f"idx: {i[0]} " f"value: {i[1]}\n"
            for i in list(enumerate(self.storage))
        )

    def _heapify_up(self):
        child_idx = len(self.storage) - 1  # tried using -2 as we've already appended

        # while c_idx > p_idx

        while child_idx > 0:
            # possible because we have a complete binary tree
            parent_idx = (child_idx - 1) // 2
            parent_element = self.storage[parent_idx]
            child_element = self.storage[child_idx]

            if parent_element > child_element:  # vice vera if implementing max heap
                # swap
                self.storage[parent_idx] = child_element
                self.storage[child_idx] = parent_element

                child_idx = parent_idx

            else:
                break

    def _heapify_down(self):
        parent_idx = 0

        # -- TODO review this first while clause
        while parent_idx < self.heap_size:  # this means i'll always do worst case O(n)
            left_child_idx = 2 * parent_idx + 1
            right_child_idx = 2 * parent_idx + 2

            parent_element = self.storage[parent_idx]
            left_child = right_child = None
            min_element = parent_element

            if left_child_idx < self.heap_size - 1:  # check left child exists
                left_child = self.storage[left_child_idx]
                min_element = min(parent_element, left_child)

            if right_child_idx < self.heap_size - 1:  # check right child exists
                right_child = self.storage[right_child_idx]
                min_element = min(parent_element, right_child)

            if min_element == parent_element:
                return

            if min_element == left_child:  # swap left and parent
                self.storage[left_child_idx] = parent_element
                self.storage[parent_idx] = min_element
                parent_idx = left_child_idx

            if min_element == right_child:  # swap right and parent
                self.storage[right_child_idx] = parent_element
                self.storage[parent_idx] = min_element
                parent_idx = right_child_idx

    def insert(self, data):
        """
        insertion must maintain heap order property (min or max)
        (1) insert at the end O(1)
        (2) heapify O(log(n)) -> bubble up
        """
        self.storage.append(data)
        self.heap_size += 1
        self._heapify_up()

        # personally i prefer to append the new element and then heapify
        #  it is perhaps more efficient to keep track of "next idx"
        # in this case we have a self.next_idx attribute, init at 0
        # and must add capacity when next_idx == len(storage)

        # # add capacity
        # self.storage[self.next_idx] = data
        # self._max_heapify()
        # self.next_idx += 1

        # if self.next_idx > len(self.storage):
        #     temp = [None] * (2 * len(self.storage))
        #     self.storage.extend(temp)

    def remove(self):
        """
        in a heap we only allow someone to remove the root node
        hence, useful for priority queues
        (1) remove the element O(1)
        (2) make the last element added the root node and heapify -> bubble down
        """
        if self.heap_size == 0:
            return None

        root_element = self.storage[0]  #  to be returned

        last_element = self.storage[-1]
        self.storage[0] = last_element  # overwrite first element with last
        self.storage.pop()  # remove the duplicate element
        self.heap_size -= 1
        self._heapify_down()

        return root_element

    def peek(self):
        """Returns None if empty"""
        return None if self.heap_size == 0 else self.storage[0]

    def is_empty(self) -> bool:
        return self.heap_size == 0


myHeap = Heap()
elements = [1, 2, 3, 4, 1, 2]

for _ in elements:
    myHeap.insert(_)

# assert myHeap == "[(0, 1), (1, 1), (2, 2), (3, 2), (4, 3), (5, 4)]"
# assert myHeap.heap_size == 6
# assert myHeap.peek() == 1
# assert myHeap.remove() == 1
# assert myHeap.remove() == 1
# assert myHeap.remove() == 2
# assert myHeap.remove() == 2
# assert myHeap.peek() == 3
# assert myHeap.remove() == 3
# assert myHeap.remove() == 4
# assert myHeap.is_empty() == True
# assert myHeap.peek() == None
# assert myHeap.remove() == None
