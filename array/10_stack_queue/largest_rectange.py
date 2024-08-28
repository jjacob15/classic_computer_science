# INSIGHT -> area of a histogram. A histogram is bar charts usually representing some distribution. To 
# find the are of a historgram, we add the index and height into a stack for all ascending bars until 
# we find a building/bar thats smaller. Then you extract all bar thats taller that the current one and update
# the its to our current index.
# INSIGHT -> You do this to ensure you get the start for the width from all the buildings taller that this.
 
def largest_rectange(h):
    stack = []
    max_area = 0
    for i, bh in enumerate(h):
        while stack and stack[-1][1] > bh:
            index,height = stack.pop()
            max_area = max(max_area, (i-index)*height)
            i = index
        stack.append((i,bh))

    while stack:
        index,height = stack.pop()
        max_area = max(max_area,(len(h)-index)*height)

    return max_area