# Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. 
# Given a string, find the number of pairs of substrings of the string that are anagrams of each other.

#INSIGHT -> ANAGRAMS, YOU CAN SORT THE TEXT TO SEE IF TWO STRINGS ARE ANAGRAMS.
#INSIGHT -> first count the number of anagram pairs. Then use count * (count - 1) //2. This is simlar to 
# the counting substring of similar characters but not using the single values so instead of  + we use a -

from collections import defaultdict
# def sherlock(s):
#     anagrams = defaultdict(int)
#     n = len(s)

#     cur_size = 1
#     while cur_size <= n-1:
#         for i in range(n):
#             val = "".join(sorted(s[i:i+cur_size]))
#             for j in range(i+1, n):
#                 substr =s[j:j+cur_size]
#                 if len(substr) != cur_size: continue 
#                 ordered = "".join(sorted(s[j:j+cur_size]))
#                 if val == ordered:
#                     anagrams[ordered]+=1
#         cur_size +=1

#     return sum([v for v in anagrams.values()])


def sherlock(s):
    result =0
    anagrams = defaultdict(int)
    n = len(s)
    # Iterate over all possible substrings
    for length in range(1, n):
        # Generate all substrings of current length
        for start in range(n - length + 1):
            substr = ''.join(sorted(s[start:start + length]))
            # print(start,substr)
            anagrams[substr] += 1

    # print("anagrams",anagrams)
    for key,count in anagrams.items():
        # print(key,count,count * (count - 1) // 2)
        result += count * (count - 1) // 2 # INSIGHT COMPLETE this is combination shortcut
    return result

