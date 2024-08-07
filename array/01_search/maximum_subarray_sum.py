# INSIGHT -> you cummulatively add prefixes and you traverse the array. Add them to an array
# when you find the next prefix, check if there is a prefix greater than this in the array, if so, 
# prefix - the greater prefix + m (to avoid negative modulo) % m. This will give you the max modulo for the array combination

def maximumSum(array, m):
    import bisect

    n = len(array)
    prefix = [0] * n
    prefix[0] = array[0] % m
    max_mod_sum = prefix[0]

    # Set to store prefix sums for binary search
    prefix_set = []
    bisect.insort(prefix_set, prefix[0])

    print(prefix)
    for i in range(1, n):
        # Compute prefix sum modulo m
        prefix[i] = (prefix[i-1] + array[i]) % m
        max_mod_sum = max(max_mod_sum, prefix[i])

        # Find the smallest prefix that is greater than prefix[i]
     #    [0,1,2,4,6] and bisect right of 4 is 6
        pos = bisect.bisect_right(prefix_set, prefix[i])
        print("b",pos,i,prefix_set,prefix[i])
        if pos < len(prefix_set):
            # Calculate (prefix[i] - prefix[pos] + m) % m
            mod_sum = (prefix[i] - prefix_set[pos] + m) % m
            max_mod_sum = max(max_mod_sum, mod_sum)
            print("pos", pos, i,mod_sum,max_mod_sum,prefix[i],prefix_set)

        # Insert the current prefix to the set.We are ordering it so that you always get the 
        # next largest modulo from the set
        bisect.insort(prefix_set, prefix[i])
        print("a", prefix_set, prefix[i])

    return max_mod_sum
