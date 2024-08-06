# given an array of cost, find two 1 based index that adds to money [2,1,3,5,6] and 5. print(1,3). You can also have mutiple costs of the same value.
# naive 0(n2) will not work
# Use a cost map for all single values
# Use a double cost map for all mutiple values. This will make it O(n)




from collections import defaultdict
def whatFlavors(cost, money):
    # Write your code here
    cost_map = {}
    double_cost = defaultdict(list)
    for i,c in enumerate(cost):
       if c in cost_map and c not in double_cost:
           double_cost[c].append(cost_map[c])
           double_cost[c].append(i+1)
           del cost_map[c]
       else:
           cost_map[c] = i +1
    
    for i,c in enumerate(cost):
        if money - c in cost_map and cost_map[money - c] != i+1:
            print(i+1, cost_map[money - c])
            break
        if money - c in double_cost:
            print(double_cost[money - c][0], double_cost[money - c][1])
            break
            

# given an array of values, find a pair that have a difference of K. similar technique. Using hashmap to avoid On2


from collections import defaultdict
def pairs(k, arr):
    # Write your code here
    arr_map = defaultdict(int)
    for i,a in enumerate(arr):
        arr_map[a] = i
    
    pair_count = 0
    for i,a in enumerate(arr):
        if a + k in arr_map and arr_map[a+k] != i:
            pair_count+=1
            
    return pair_count
