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
    
            


