# 1035. Uncrossed Lines
# Medium
# You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.

# We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:

# nums1[i] == nums2[j], and
# the line we draw does not intersect any other connecting (non-horizontal) line.
# Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).

# Return the maximum number of connecting lines we can draw in this way.

# Input: nums1 = [1,4,2], nums2 = [1,2,4]
# Output: 2
# Explanation: We can draw 2 uncrossed lines as in the diagram.
# We cannot draw 3 uncrossed lines, because the line from nums1[1] = 4 to nums2[2] = 4 will intersect the line from nums1[2]=2 to nums2[1]=2.

#INSIGHT -> samme a longest subsequence

#     1 2 4
#     0 0 0
# 1 0 1 1 1
# 4 0 1 1 2
# 2 0 1 2 2


from typing import List


def maxUncrossedLines(nums1: List[int], nums2: List[int]) -> int:
    dp = [[0]*(len(nums2)+1) for _ in range(len(nums1)+1)]

    # print(dp)
    max_j = 0
    total =0
    for i in range(1, len(nums1)+1):
        for j in range(1, len(nums2)+1):
            if nums1[i-1] == nums2[j-1]:
               dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    for row in dp:
        print(row)
    print(total)

# maxUncrossedLines([1, 4,2],[1,2,4]) #2
# maxUncrossedLines([2,5,1,2,5],[10,5,2,1,5,2]) #2
maxUncrossedLines([1,1,2,1,2],[1,3,2,3,1]) #3
# maxUncrossedLines([1,3,7,1,7,5],[1,9,2,5,1]) #2