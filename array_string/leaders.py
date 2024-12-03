# Given an array, print all the elements which are leaders. A Leader is an element that is greater than all of the elements on its right side in the array.Input:

# arr = [4, 7, 1, 0]
# Output 7 1 0
# Explanation:
# Rightmost element is always a leader. 7 and 1 are greater than the elements in their right side.
import sys


def leaders(arr):
    max_val = -sys.maxsize - 1
    for i in range(len(arr)-1, -1, -1):
        if arr[i] > max_val:
            print(arr[i])
            max_val = arr[i]


leaders([4, 7, 1, 0])
leaders([10, 22, 12, 3,0,6])        