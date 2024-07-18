from collections import defaultdict

def sherlock(s):
    # Write your code here
    count = defaultdict(int)
    for char in s:
        count[char]+=1
        
    charCountMap = defaultdict(int)
    for val in count.values():
        charCountMap[val] +=1

    if len(charCountMap) == 1:
        return "YES"
    
    if len(charCountMap) > 2:
        return "NO"
    
    keys = list(charCountMap.keys())
    if charCountMap[keys[0]] < charCountMap[keys[1]] and charCountMap[keys[0]] ==1:
        if keys[0]-1 == keys[1]or keys[0]-1 == 0:
            return "YES"
        else:
            return "NO"
    if charCountMap[keys[0]] > charCountMap[keys[1]] and charCountMap[keys[1]] ==1:
        if keys[1]-1 == keys[0] or keys[1]-1 == 0:
            return "YES"
        else:
            return "NO"

    return "NO"

