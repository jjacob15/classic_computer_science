# OBJECTIVE -> given 3 arrays, you need to return tuples with a <= b >= c.
# Eg [3,5,7], [3,6] and  [4,6,9] will result combos are
# (3,6,4), (3,6,6), (5,6,4), (5,6,6)


def triplets(a, b, c):
    a = sorted(set(a))
    b = sorted(set(b))
    c = sorted(set(c))

    def find_less_than_arr(arr, target):
        print(arr,target)
        l, r = 0, len(arr)
        while l < r:
            mid = (l+r)//2
            if target >= arr[mid]:
                l = mid + 1
            else:
                r = mid
        print(l, r, mid,target)
        return l

    total = 0
    
    for b_item in b:
        less_than_a = find_less_than_arr(a, b_item)
        print("------", less_than_a)
        less_than_c = find_less_than_arr(c, b_item)
        print("------", less_than_c)
        print(b_item, less_than_a, less_than_c)

        total += less_than_a * less_than_c

    return total


a = (1, 3, 5, 7)
b = (5, 7, 9)
c = (7, 9, 11, 13)
print("ans",triplets(a, b,c))