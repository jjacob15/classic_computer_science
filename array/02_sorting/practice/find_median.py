#Insight -> rebalancing is simple arr len check. heapq (priority queue in python always keeps the assending order)
# to remove an item from here, check if its lesser that -low [0] and remove from the low queue. rebalance. Else remove from high and rebalance.
# finding a running median of a fixed size adding the initial values and getting the median, then removing the head and adding the tail.

import heapq

def median(arr):
    low, high = [],[]
    def add(val):
        if len(low) > 0 and val < -low[0]:
            heapq.heappush(low, -val)
        else:
            heapq.heappush(high,val)

        if len(low) < len(high):
            heapq.heappush(low, -heapq.heappop(high))
        elif len(high) > len(low):
            heapq.heappush(high, -heapq.heappop(low))

    for val in arr:
        add(val)
        print(low,high)
    
    if len(arr) % 2 == 0:
        return (-low[0] + high[0])/2
    else:
        return -low[0]

    

# arr1 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
arr2 = [2, 3, 5, 2, 3, 4, 3, 2, 4, 6, 123, 123, 2, 120, ]

# print(median(arr1))
print(median(arr2))
