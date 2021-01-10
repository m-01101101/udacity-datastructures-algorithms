# Explanations

## Problem 1: LRU Cache

The `LRU_Cache` implemented inherits from an `OrderedDict`. This is a specialised dictionary that remembers the insertion order of keys. It is particularly useful in that it comes built in with a `move_to_end()` method. Each time a value is called using `LRU_Cache.get()` we are able to move the value to the right end of the cache. This means, when we `popitem()` we must include `False` so that the left end represents the least recently used item `(FIFO)`.

### 1: Time and space complexity

Operations will be $O(1)$ as we use a key to lookup values. Equally, if the cache hits capacity we just remove the most left item (`popitem(False)`).

The `move_to_end()` method is also $O(1)$ as the length of the dictionary does not impact the time taken to move the element to the end [\[ref]][1]:

```python
def move_to_end(self, key, last=True):
	"""Move an existing element to the end (or beginning if last is false).

        Raise KeyError if the element does not exist."""

        link = self.__map[key]  # The internal self.__map dict maps keys to links in a doubly linked list
        link_prev = link.prev
        link_next = link.next
        soft_link = link_next.prev
        link_prev.next = link_next
        link_next.prev = link_prev
        root = self.__root
        if last:
            last = root.prev
            link.prev = last
            link.next = root
            root.prev = soft_link
            last.next = link
        else:
            first = root.next
            link.prev = root
            link.next = first
            first.prev = soft_link
            root.next = link
```

In terms of space complexity, the upper limit will be determined by the user when setting `capacity`, this is linear complexity $O(n)$.

## Problem 2: File recursion

Using Python’s built-in `pathlib` module allows for a more eloquent implementation of iterating through the directory `path.iterdir()` and checking the suffix of a file `file.suffix`

### 2: Time and space complexity
The `find_files` function is implemented recursively, checking all possible directories. As a result, the time complexity is linear $O(n)$, depending on the number of directories and files that must be traversed.

In terms of space complexity, the list returned is extended (appended would create a list of lists) each time there is a match, therefore the complexity is determined by the number of matches are found, again this is linear $O(n)$.

## Problem 3: Huffman Coding

When calling `huffman_decoding` I initialise another class of the `HuffmanEncoder`, this is perhaps inefficient but felt more in-line with the principles of functional programming.

When merging nodes I used Python's built in min heap implementation `heapq`. This is because I sort the nodes in a list, and would have to create a copy of the list to then iterate and modify over it. Alternatively, I could have created a separate class specifically for merging the nodes, but this felt unnecessary. The `heapq` allowed me to bypass that step and create a min heap data structure whilst merging nodes.

### 3: Time and space complexity

Time complexity of functions;

- Linear $O(n)$ when creating a frequency dictionary using `Counter` as dependent on the number of characters in the string.
- Linear $O(n)$ when merging the nodes into a min heap structure, as dependent on the number of nodes.
- Generating the codes is $O(n * log(n))$, this is because we must traverse the tree (which is $log(n)$), and we must do this for $n$ element.
- Encoding and decoding is linear $O(n)$, as we do a single action for each element.
- The space complexity is also linear $O(n)$, as it is directly informed by the length of the string provided to encode.

## Problem 4: Active Directory

The program aims to reach the “best case” scenario as quickly as possible. Unlike problem 2, where we must check all possibilities, here we can exit as soon as the `True` criteria is met.

### 4: Time and space complexity

However, time complexity is based on “worst case”. The worst case would still require us checking every possibility in the directory. As a result time is linear $O(n)$ it depends directly on how many possible lists of users there are to explore.

Space complexity is $O(1)$ as we return a single boolean variable.

## Problem 5: Blockchain

### 5: Time and space complexity

By having a `tail` attribute to the `Blockchain` class, blocks can be appended in a time complexity of $O(1)$. However, the trade-off is that only one block can be added at a time.

In previous examples we used a `while` loop to get to the tail.

In order for this implementation to work, the `previous_hash` attribute of a block, must be a Block, it cannot just be the hash string of the last linked Block.

The space allocated for our Blockchain is dependent on the number of blocks, and is therefore linear in terms of complexity $O(n)$.

## Problem 6: Linked Lists

I added a function with first converts the Linked List into a Python list, this allows me to iterate over the two linked lists provided. Alternatively, I could have implemented a `__next__` operator on the Linked List.

I have used a Python set for both `union` and `intersection` to ensure duplicate values are not returned.

### Time and space complexity

Converting Linked Lists to a Python list is linear $O(n)$ as I iterate over each element.

`union` is $0(n)$ (really it's $2*O(n)$) as I convert both Linked Lists to a Python list, and then iterate over that Python list, one element at a time.

In terms of space complexity, we create a number of lists, again this is $0(n)$ (really $3*O(n)$)

`intersection` is $0(n)$, again converted Linked Lists to lists. Though the `set` operation will be much faster, the programme is still linearly dependent on the inputs.

Intersection follows the same logic also in terms of space complexity ($O(n)$)

[1]:	https://github.com/python/cpython/blob/master/Lib/collections/__init__.py "cpython source code"
