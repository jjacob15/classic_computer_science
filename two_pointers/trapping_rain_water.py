# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9

#INSIGHT -> to find the bounded height we need 3 things. The current, last 2 places in the stack. You break if after you pop the stack to get the last value, as you need the third value
# to compute the bounded height. A water gap only forms with at least 3 positions, current, middle and end positions.

def trapping_raning(height):
    stack = []
    water_trapped = 0
    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()
            if not stack:
                print("breaking")
                break
            distance = i - stack[-1] -1
            print(i,height[i],height[stack[-1]],height[top])
            # Find the bounded height by the smaller of the two boundaries
            bounded_height = min(height[i], height[stack[-1]]) - height[top]
            
            # Calculate the water trapped in this bounded area
            print("water", distance * bounded_height)
            water_trapped += distance * bounded_height

        stack.append(i)
        print("stack",stack)

    print(water_trapped)


trapping_raning([0,1,0,2,1,0,1,3,2,1,2,1])
# trapping_raning([4,2,0,3,2,5])