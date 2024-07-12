def bribe(arr):
    bribe = 0
    bribeMap = {}
    swap = True
    while swap:
        swap = False
        for i in range(1,len(arr)):
            if arr[i-1] > arr[i]:
                swap = True
                if arr[i-1] not in bribeMap:
                    bribeMap[arr[i-1]] = 0
                bribeMap[arr[i-1]] +=1
                if bribeMap[arr[i-1]] > 2:
                    return "Too chaotic"
                arr[i-1],arr[i] = arr[i],arr[i-1]
                bribe+=1
        
    return bribe


def minimumBribes(q):
    bribe = 0
    bribeMap = {}
    swap = True
    while swap:
        swap = False
        for i in range(1,len(q)):
            if q[i-1] > q[i]:
                swap = True
                if q[i-1] not in bribeMap:
                    bribeMap[q[i-1]] = 0
                bribeMap[q[i-1]] +=1
                if bribeMap[q[i-1]] > 2:
                    return "Too chaotic"
                q[i-1],q[i] = q[i],q[i-1]
                bribe+=1
        
    return bribe