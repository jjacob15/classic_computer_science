from collections import Counter,defaultdict

def getSubstringsCount(s):
    count = len(s)
    counter = Counter(s)
        
    return len(counter) +  (count * (count -1)//2)
def how_many_substrings(s,queries):
    # Write your code here
    result = []
    for left,right in queries:
        result.append(getSubstringsCount(s[left:right+1]))
        
    return result