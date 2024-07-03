from typing import List

def can_construct(target:str,wordbank:List[str],memo=None):
    if memo is None:
        memo = {}
    if target in memo: return target
    if target == "": return [[]]
    
    result = []
    print(f"creating new result arry for target {target}")
    for word in wordbank:
        if target[:len(word)] == word:
            suffix = target[len(word):]
            suffix_ways = can_construct(suffix,  wordbank)
            # and the next three lines gets called iteratively with updated suffix_ways 
            # from bottom up 
            # print("-----")
            print("ways b",suffix_ways)
            for suffix_way in suffix_ways:
                suffix_way.insert(0,word)
                print("sw",suffix_way)
                print("result b",result)
                result.append(suffix_way)
            
            print("ways a",suffix_ways)
            print("result a",result)
    print("returning result",result)
    memo[target] = result
    return result
