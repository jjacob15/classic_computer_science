def max_sum_subarr(arr,size):
    if len(arr) < size:
        return None
    max_sum = sum(arr[:size])
    curr = max_sum
    for i in range(size,len(arr)):
        curr = curr + arr[i] - arr[i - size]
        max_sum = max(max_sum,curr)
    return max_sum



