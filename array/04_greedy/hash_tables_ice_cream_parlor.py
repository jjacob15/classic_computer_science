# we need to find two values that sums to the money
# can't use two pointer as its not sorted and one hash doesn't work because you can have duplicates
# so use two hashes one for single item and one for multiples
# time complexity becomes 0(n) and space 0(n)
m = 4
cost = [1,4,5,3,2] # prints(1, 4)

m = 4
cost = [2,2,4,2] # prints(1, 2)


def whatFlavors(cost, money):
    from collections import defaultdict
    # Write your code here
    cost_map = {}
    multiple_cost = defaultdict(list)
    for i,c in enumerate(cost):
       if c in cost_map and c not in multiple_cost:
           multiple_cost[c].append(cost_map[c])
           multiple_cost[c].append(i+1)
           del cost_map[c]
       else:
           cost_map[c] = i +1
    
    for i,c in enumerate(cost):
        if money - c in cost_map and cost_map[money - c] != i+1:
            print(i+1, cost_map[money - c])
            break
        if money - c in multiple_cost:
            print(multiple_cost[money - c][0], multiple_cost[money - c][1])
            break