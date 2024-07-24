def minimumSwaps(arr):
    pos = {arr[i]:i for i in range(len(arr))}
    visited = {arr[i]: True if i+1 == arr[i]else False for i in range(len(arr))}
    swap = 0

    for i in range(len(arr)):
        key = arr[i]
        if visited[key]: 
            continue
        cycle_size = 0
        while True:
            keyIdx = pos[key]
            if visited[key]:
                break
            needKey = keyIdx+1
            needVal = pos[needKey]
            pos[needKey] = keyIdx
            visited[needKey] = True

            pos[key] = needVal
            visited[key] = True if needVal + 1 == needKey else False
            cycle_size += 1
        
        # print(key,cycle_size)
        if cycle_size > 1:
            swap += (cycle_size - 1)
    return swap 

def minimumSwapsOld(arr):
    map = {arr[i]: (i, True if i+1 == arr[i]else False) for i in range(len(arr))}
    swap = 0

    for i in range(len(arr)):
        key = arr[i]
        _,keyVisited = map[key]
        if keyVisited: 
            continue
        cycle_size = 0
        while True:
            keyIdx,keyVisited = map[key]
            if keyVisited: break
            needKey = keyIdx+1
            needVal,_ = map[needKey]
            map[needKey] = (keyIdx, True)
            map[key] = (needVal,True if needVal + 1 == needKey else False)
            cycle_size += 1
        
        # print(key,cycle_size)
        if cycle_size > 1:
            swap += (cycle_size - 1)
    return swap 

def minimumSwaps1(arr):
    n = len(arr)
    # Create a list of tuples where each tuple is (element, index)
    arrpos = [(arr[i], i) for i in range(n)]
    print(arrpos)
    # Sort the array by the element values
    arrpos.sort()
    print(arrpos)
    # Initialize a visited array to keep track of visited elements
    visited = [False] * n
    swaps = 0

    for i in range(n):
        # If element is already visited or is in the correct position, skip it
        if visited[i] or arrpos[i][1] == i:
            continue
        cycle_size = 0
        j = i
        # Follow the cycle of positions
        while not visited[j]:
            visited[j] = True
            j = arrpos[j][1]
            cycle_size += 1
        # If cycle size is greater than 1, add the number of swaps for this cycle
        if cycle_size > 1:
            swaps += (cycle_size - 1)

    return swaps
