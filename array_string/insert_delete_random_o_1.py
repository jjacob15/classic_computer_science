# Implement the RandomizedSet class:

# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.

# INSIGHT -> the trick to keep everythin in O(I) is to have hashmap and not use remove from a list. INSTEAD REPLACE THE INDEX OF ELEMENT YOU WANT TO DELETE WITH THE LAST VALUE 
# AND DO A POP. POP IS O(1) COST

import random
class RandomizedSet:

    def __init__(self):
        self.dict = {}  # Dictionary to store element to index mapping
        self.list = []  # List to store elements for constant-time random access

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        # Get the index of the element to remove
        idx = self.dict[val]
        # Move the last element to the place of the element to remove
        last_element = self.list[-1]
        self.list[idx] = last_element
        self.dict[last_element] = idx
        # Remove the last element
        self.list.pop()
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)
