from typing import List

def can_construct(target:str,wordbank:List[str],memo=None):
    if memo is None:
        memo = {}
    if target in memo: return target
    if target == "": return [[]]
    
    result = []
    # print(f"creating new result arry for target {target}")
    for word in wordbank:
        if target[:len(word)] == word:
            suffix = target[len(word):]
            suffix_ways = can_construct(suffix,  wordbank)
            # and the next three lines gets called iteratively with updated suffix_ways 
            # from bottom up 
            # print("-----")
            # print("ways b",suffix_ways)
            for suffix_way in suffix_ways:
                suffix_way.insert(0,word)
                # print("sw",suffix_way)
                # print("result b",result)
                result.append(suffix_way)
            
    #         print("ways a",suffix_ways)
    #         print("result a",result)
    # print("returning result",result)
    memo[target] = result
    return result

def can_construct_tab(target,wordbank):
    dp =[None for _ in range(len(target)+1)]
    dp[0]=[[]]

    for char_idx in range(len(target)):
        for word in wordbank:
            if word[0] == target[char_idx]:
                if dp[char_idx] is not None:
                    for item in dp[char_idx]:
                        copy_of = [*item] 
                        copy_of.append(word)
                        if len(dp) > len(word)+char_idx:
                            if dp[len(word)+char_idx] is None:
                                dp[len(word)+char_idx] = []
                            dp[len(word)+char_idx].append(copy_of)
                            # print(char_idx,dp)
    return dp[len(target)]













# def can_construct_tab(target,wordbank):
#     dp = [None for _ in range(len(target)+1)]
#     dp[0] = [[]]

#     for char_idx in range(len(target)):
#         for word in wordbank:
#             if word[0] == target[char_idx]:
#                 if dp[char_idx] is not None:
#                     for arr in dp[char_idx]:
#                         copy_of = [*arr]
#                         copy_of.append(word)
#                         if len(dp) > len(word)+char_idx:
#                             if dp[len(word)+char_idx] is None:
#                                 dp[len(word)+char_idx] = []
#                             dp[len(word)+char_idx].append(copy_of)

#     # print(dp)
#     return dp[len(target)]