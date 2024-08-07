from collections import Counter

# merge(reverse(A),suffle(A)) -> Find A
# INSIGHT -> there reverse should be there somewhere so start from tail to the head.
 
# The idea here is you could have a string abcd that has been reversed and shuffled and then merged. You need to find the lexically smallest string.
# As it is reversed, you are going to look backwards.
# We keep a final frequency map that lists of the characters of A. Which is half of the count from the string.
# we then iterate until we have a solution with the len of (s)//2
# the plan is going backwards and keeping a track of the min character. 
# as we go back we reduce the left_freq and break when the left freq of that char is less that the string freq. THIS INDICATES THE BREAK FROM THE A TO THE SECOND A
# We take the min, add it to the solution, and repeat from where that min value was picked.
# we also need to ensure that we don't add the next char position of duplicates.


def reverse_shuffle_merge(s):

    freq = {key: value//2 for key, value in Counter(s).items()}
    solution = []
    n = len(s)

    while len(solution) < n//2:
        left_freq = Counter(s)
        min_char = "~"
        next_char = {}

        for index in range(len(s)-1,-1,-1):
            char = s[index]
            if char not in next_char and freq[char] > 0:
                next_char[char] = index
                min_char = min(min_char,char)
            
            left_freq[char] -=1
            if left_freq[char] < freq[char]:
                break

        solution.append(min_char)
        freq[min_char] -= 1
        s = s[:next_char[min_char]]


    return "".join(solution)
























    # # find character frequencies in the desired string A
    # freq = {key: val // 2 for key, val in Counter(s).items()}

    # # repeat gready approach until solution is complete
    # solution = []
    # print(freq)
    # n = len(s)
    # while len(solution) < n // 2:
    #     left_freq = Counter(s)
    #     next_char = {}
    #     min_char = '~'
    #     print("left_freq",left_freq)
    #     # search original string S backwards
    #     for index in range(len(s)-1, -1, -1):
    #         char = s[index]
    #         print("h",index,char,next_char,min_char,left_freq)
    #         # it is possible to take this char as the next one
    #         if char not in next_char and freq[char] > 0:
    #             next_char[char] = index
    #             min_char = min(min_char, char)
    #         # there's not enough letters available to the left
    #         left_freq[char] -= 1
    #         if left_freq[char] < freq[char]:
    #             print("breaking")
    #             break
    #     # add minimal char as the next one (greedy)
    #     solution += min_char
    #     freq[min_char] -= 1
    #     s = s[0:next_char[min_char]]
    #     print("min_char",solution,s,freq,next_char)

    # print("s","".join(solution))
    # return "".join(solution)