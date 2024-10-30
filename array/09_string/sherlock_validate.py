from collections import defaultdict

# is valid if all characters of the string appear the same number of times or 
# you remove just 1 character at 1 index in the string and the remaining characters will occur the same number of times
def sherlock(s):
    # Write your code here
    count = defaultdict(int)
    for char in s:
        count[char]+=1 # find each character count
        
    charCountMap = defaultdict(int)
    for val in count.values():
        charCountMap[val] +=1 #now keep a map of the number of occurance. so if a and b occurs 2 times and c 1time, 
                                #you have {2: 2, 1: 2}. If the count is one then you are good
                                # this case is a false because 1 can't be reduced to zero or matched to the 2's value.

    if len(charCountMap) == 1:
        return "YES"
    
    if len(charCountMap) > 2:
        return "NO" #if there are more that 2 then its a no
    
    keys = list(charCountMap.keys())
    if charCountMap[keys[0]] < charCountMap[keys[1]] and charCountMap[keys[0]] ==1:
        if keys[0]-1 == keys[1]or keys[0]-1 == 0:
            return "YES" #you are checking if the least occuring item can be either reduced to zero or reduced to the value of the majority 
        else:
            return "NO"
    if charCountMap[keys[0]] > charCountMap[keys[1]] and charCountMap[keys[1]] ==1:
        if keys[1]-1 == keys[0] or keys[1]-1 == 0:
            return "YES"
        else:
            return "NO"

    return "NO"

