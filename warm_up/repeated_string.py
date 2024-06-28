def repeatedString(s, n):
    # Write your code here
    count = s.count("a")
    portions = n//len(s)
    portionCount = (portions * count)
    remaingEnd = n - (portions * len(s))
    if remaingEnd == 0: return portionCount
    remainingCount = s[:remaingEnd].count("a")
    return portionCount + remainingCount
    

print(repeatedString('aba',10))  
print(repeatedString('abab',10))  
print(repeatedString('abab',11))  
print(repeatedString('aba',9))  
print(repeatedString('a',1000))
print(repeatedString('gfcaaaecbg',547602)) ## 164280