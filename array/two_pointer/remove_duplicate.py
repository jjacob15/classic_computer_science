def remove_duplicate(arr):
    if len(arr) == 1:
        return arr
    
    slow = 0
    fast = 1
    while fast < len(arr):
        if arr[slow] == arr[fast]:
            fast+=1
        else:
            arr[slow+1] = arr[fast]
            slow +=1 

    return arr[:slow+1]