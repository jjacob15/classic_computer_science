def palindrome_partitioning(s):
    result = []
    n = len(s)
    def isPalindrome(s):
        return s== s[::-1]

    def backtrack(start,combination):
        if start == len(s):
            result.append(combination[:])
            return
        for end in range(start+1,len(s)+1):
            substring = s[start:end]
            print(substring)
            # if isPalindrome(substring):
            combination.append(substring)
            backtrack(end,combination)
            combination.pop()
    backtrack(0,[])
    print(result)
    return result

palindrome_partitioning("aab")