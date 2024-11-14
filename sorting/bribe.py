# If person  bribes person , the queue will look like this: 1,2,3,5,4,6,7,8. Only 1 bribe is required. Print 1.
# q 4,1,2,3. Person 4 had to bribe 3 people to get the current position. Print too chaotic

# we use a bubble sort technique of look at two adjacent values and sort it will increasing the bribemap dict
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