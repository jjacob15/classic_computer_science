# if you are given an array [2,3,2] as machines, that means each machine takes that many days to produce 
# one item. The idea is to find the maximum number of days to produce the desired goal of items. 
# INSIGHT -> have a method to compute the items produce for a particular number of days. days//machine gives that number. 
# Then we use binary search between 1 and max(machine)* days to find the when we can reach the goal. Break the 
# condition when the items produced < goal.

def min_time_required(machines, goal):
    l, r = 1, max(machines)*goal

    def num_of_items_produced(day):
        items = 0
        for machine in machines:
            items += day // machine
        return items

    while l < r:
        m = (l+r)//2
        if num_of_items_produced(m) < goal:
            l = m+1
        else:
            r = m

    return l
