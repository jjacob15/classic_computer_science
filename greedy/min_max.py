# create a subarray such that the max(sub) - min(sub) provides the minimum unfairness
# WITH THE INSIGHT THAT THE CLOSEST DIFFERENCE IS ALWASY BETWEEN ADJACENT NUMBERS, WE SORT IT FIRST
# then we loop through the items with the window size and find the unfairness
def min_max(k,arr):
    # Write your code here
    arr.sort()
    if k == 2:
        return 0
    unfairness = float("inf")
    for i in range(len(arr)-k+1):
        max_val = arr[k+i-1]
        min_val = arr[i]
        unfairness = min(unfairness, max_val - min_val)

    return unfairness