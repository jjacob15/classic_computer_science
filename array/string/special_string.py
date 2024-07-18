from collections import defaultdict
def special_str_count(n,s):
   # Step 1: Create an array to store the count of consecutive characters
    count = []
    i = 0
    
    while i < n:
        char_count = 1
        while i + 1 < n and s[i] == s[i + 1]:
            char_count += 1
            i += 1
        count.append((s[i], char_count))
        i += 1
    
    # Step 2: Count substrings with all same characters
    total_substrings = 0
    for char, char_count in count:
        total_substrings += (char_count * (char_count + 1)) // 2
    
    # Step 3: Count substrings with one different middle character
    print(s)
    print("b",total_substrings,count)
    # print(1,len(count)-1)
    for j in range(1, len(count) - 1):
        if count[j][1] == 1 and count[j - 1][0] == count[j + 1][0]:
            print( min(count[j - 1][1], count[j + 1][1]),count[j - 1][1],count[j + 1][1])
            total_substrings += min(count[j - 1][1], count[j + 1][1])
    
    print("a",total_substrings)
    return total_substrings