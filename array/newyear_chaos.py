def minimumBribes(q):
    pos =0
    bribe = 0
    isCaotic = False
    while pos < len(q):
        curr = q[pos]
        next = q[pos +1]
        if curr + 1 != next :
            bribe += next - pos
            print(bribe, next, curr)
            if bribe > 3:
                isCaotic = True
                break
            pos -= 2
        else:
            pos -=1 

    if isCaotic:
        return "Too chaotic"
    
    return bribe




# print(minimumBribes([2,1,5,3,4]))
# print(minimumBribes([2,5,1,3,4]))
# print(minimumBribes([2,5,1,3,4]))
# print(minimumBribes([5, 1, 2, 3, 7, 8, 6, 4]))
print(minimumBribes([1, 2, 5, 3, 4, 7, 8, 6]))