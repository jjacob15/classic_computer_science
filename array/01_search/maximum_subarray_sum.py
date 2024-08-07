def maximumSum(array,m):
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
        print("b",prefix_set)
        max_mod_sum = max(max_mod_sum, prefix[i])

        # Find the smallest prefix that is greater than prefix[i]
        pos = bisect.bisect_right(prefix_set, prefix[i])
        if pos < len(prefix_set):
            # Calculate (prefix[i] - prefix[pos] + m) % m
            mod_sum = (prefix[i] - prefix_set[pos] + m) % m
            max_mod_sum = max(max_mod_sum, mod_sum)

        # Insert the current prefix to the set
        bisect.insort(prefix_set, prefix[i])
        print("a",prefix_set)

    return max_mod_sum