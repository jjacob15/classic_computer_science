def find_sum(arr,target):
    left = 0
    right = len(arr) -1 
    found = False
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            found = True
            break
        elif target < s:
            right -=1
        else:
            left +=1
        
    return found