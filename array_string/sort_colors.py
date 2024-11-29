# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.
# using Dutch National flag algorithm specifically for sorting 3 elements
# use 3 pointers 
def sortColors(nums):
    low = current = 0
    high = len(nums)-1
    while current <=high:
        if nums[current] == 0:
            nums[low],nums[current] = nums[current],nums[low]
            low +=1
            current +=1
        elif nums[current] == 2:
            nums[high],nums[current] = nums[current],nums[high]
            high -=1
        else:
            current+=1
    print(nums)
sortColors([2,0,2,1,1,0])