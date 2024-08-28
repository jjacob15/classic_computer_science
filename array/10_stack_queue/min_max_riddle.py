def min_max_riddle(arr):
    n = len(arr)
    
    # Initialize left and right arrays
    left = [-1] * n
    right = [n] * n

    # Stack to store indexes of array elements
    stack = []
    
    # Fill left array
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1]
        stack.append(i)
    
    # Clear stack for re-use
    stack.clear()

    # Fill right array
    for i in range(n-1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1]
        stack.append(i)
    # Initialize result array
    result = [0] * (n + 1)
    # print(left,right)
    
    # Fill result array
    for i in range(n):
        length = right[i] - left[i] - 1
        result[length] = max(result[length], arr[i])

    # print(result)
    
    
    # Fill the remaining entries in the result array
    for i in range(n-1, 0, -1):
        result[i] = max(result[i], result[i+1])
    
    # print(result)
    # Output the result excluding the zero-th index
    return result[1:]
