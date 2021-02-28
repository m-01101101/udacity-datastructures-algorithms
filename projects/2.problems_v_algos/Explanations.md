# Explanations

## Problem 1: Square root

We're able to find the square root using binary search.

We know the square root will be <= x/2, so we're able to take the mid point of x/2 and determine at each iteration if we should go higher or lower. 

This approach results in a time complexity of $O(log($\frac{n}{2}$))$ though we evaluate to $O(log(n))$ as we only care about exponents.

No additional data structures or memory is required, resulting in a time complexity of $O(1)$

## Problem 2: Search rotated array

We're able to use binary search as the array is sorted.

Binary search in the worst case evaluates to a time complexity $n * \frac{1}{2}^s$ where $n$ is the array size and $s$ the number of steps.

This ensures we have a run time of $O(log(n))$

No duplicates or copies are requires to search the array, resulting in a space complexity of $O(1)$

## Problem 3: Rearrange digits

As we only need to iterate through half the length of the array, adding numbers alternatively to two lists we have a runtime of $O(log n)$, note to self, log because we are in base 2.

## Problem 4: Dutch national flag

Time complexity of $O(n)$ as we only need to traverse the list once. This is done at the expense memory, as we create separate lists for each of `0`, `1`, `2`. As a result our space complexity is $O(2n)$, though in the analysis we only care about exponents.

## Problem 5: Autocomplete with Trie

We use a dictionary because we want to do (1) fast look-ups, $O(1)$ and (2) have the flexibility to store values as single characters or a group of characters.

Each insertion is $O(n)$ as we must loop through the word one character at a time.

Our `find` method is looking through the keys of a dictionary, this is equivalent to looking through a hash table though the worst case for a look up is still $O(n)$

In the worst case, words will have no overlapping characters and each character would be saved as values in our dictionary. This would result in a space complexity on $O(n)$

## Problem 6: Max Min unsorted array

We're able to traverse the list once $O(n)$ by taking the first element as the default min and max, and then assessing each future elements against our defaults $O(1)$

This gives us $O(2n)$, which we evaluate as $O(n)$.

## Problem 7: Request routing

Similar to problem 5. Each node is dictionary, providing us with fast look-ups and ability to store a variety of characters as values.

Insertion is time and space complexity of $O(n)$ as each element in the part must be iterated through and a new node created for each element.

The look up method has a time complexity of $O(n)$ as we split the path into a list and iterate through each element. No additional space is required, resulting in a space complexity of $O(1)$
