#ANOTHER INSIGHT FOR ANAGRAMS, YOU CAN SORT THE TEXT TO SEE IF TWO STRINGS ARE ANAGRAMS.

from collections import defaultdict
def sherlock(s):
    anagrams = defaultdict(int)
    n = len(s)

    cur_size = 1
    while cur_size <= n-1:
        for i in range(n):
            val = "".join(sorted(s[i:i+cur_size]))
            for j in range(i+1, n):
                substr =s[j:j+cur_size]
                if len(substr) != cur_size: continue 
                ordered = "".join(sorted(s[j:j+cur_size]))
                if val == ordered:
                    anagrams[ordered]+=1
        cur_size +=1

    return sum([v for v in anagrams.values()])


def sherlock_old(s):
    result =0
    anagrams = defaultdict(int)
    n = len(s)
    # Iterate over all possible substrings
    for length in range(1, n):
        # Generate all substrings of current length
        for start in range(n - length + 1):
            substr = ''.join(sorted(s[start:start + length]))
            print(start,substr)
            anagrams[substr] += 1

    print(anagrams)
    for count in anagrams.values():
        print(count,count * (count - 1) // 2)
        result += count * (count - 1) // 2 # this is to 
    return result

