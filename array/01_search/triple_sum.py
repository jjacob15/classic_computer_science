# INSIGHT
# PERMUTATION -> is the arrangment of items in a specific order. If you want to arrage 3 books on a shelf 
# The first position -> you have 3 books to choose
# The second book -> you have 2 books to choose
# The third book -> you have 1 book to choose. So the permutation is 3x2x1 = 6

# COMBINATION -> Suppose you want to combine two groups and find the total combinations, you multiply the count of each
# Group A(A1,A2,A3)
# Group B(B1,B2,B3,B4) -> total combinations is 3x4 =12 

# OBJECTIVE -> given 3 arrays, you need to return tuples with a <= b >= c. 
# Eg [3,5,7], [3,6] and  [4,6,9] will result combos are 
# (3,6,4), (3,6,6), (5,6,4), (5,6,6)
# you return 4
#INSIGHT -> use set to remove duplicates
#INSIGHT -> avoid using loops to find values less than a target in a sorted array. You could use binary search
# with the condition that the value at mid should be less than or equal to the target.
#INSIGHT -> if you have sorted arrays, use binary search to find one item or all index of an item

def triplets(a,b,c):
    a = sorted(set(a))
    b = sorted(set(b))
    c = sorted(set(c))

    def find_nums_less_than_in(target, arr):
        l, r = 0, len(arr)
        while l < r:
            m = len(l+r)//2
            if arr[m] <= target:
                l = m + 1
            else:
                r = m
        return l


    total = 0
    for bval in b:
        less_a = find_nums_less_than_in(bval, a)
        less_c = find_nums_less_than_in(bval, c)

        total += less_a * less_c

    return total