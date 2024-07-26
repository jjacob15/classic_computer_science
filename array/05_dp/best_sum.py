# as with all number based problem. you create an array with the target + 1
# seed the intial value to an empty array and the rest as False
# iterate through the arr and if the current position of i is not False, place the value of the arr in its appropirate position.
# inc i and keep appended the arr with values of curr positoin.
def best_sum(target, arr):
    if target < 0 : return None
    if target == 0: return []

    best_result = None
    for i in range(len(arr)):
        remainder = target - arr[i];
        result = best_sum(remainder,arr)
        if result != None:
            result.append(arr[i])
            if best_result == None or len(result) < len(best_result):
                best_result = result
    
    return best_result
    
            


