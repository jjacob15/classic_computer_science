def majority_element(nums):
    def majority_element_rec(lo, hi):
        # Base case: the only element in an array of size 1 is the majority
        if lo == hi:
            return nums[lo]

        # Recursively find the majority elements in the left and right halves
        mid = (hi - lo) // 2 + lo
        left = majority_element_rec(lo, mid)
        right = majority_element_rec(mid + 1, hi)

        # If the two halves agree on the majority element, return it
        if left == right:
            return left

        # Otherwise, count each element and return the winner
        left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
        print("left count",left_count,left)
        right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)
        print("right count", right_count, right)

        return left if left_count > right_count else right

    return majority_element_rec(0, len(nums) - 1)

# Example usage
nums = [3, 3, 9, 2, 9, 9, 2, 9, 9]
print("Majority element:", majority_element(nums))  # Output: 4
