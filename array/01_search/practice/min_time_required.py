# if you are given an array [2,3,2] as machines, that means each machine takes that many days to produce 
# one item. The idea is to find the maximum number of days to produce the desired goal of items. 




def min_time_required(machines, goal):
    l, r = 1, max(machines)*goal

    def numberOfItemsProducedByDays(machines,day):
        itemsProduced = 0
        for machine in machines:
            itemsProduced += day//machine
        return itemsProduced
    
    print(l,r)
    while l<r:
        day = (l+r)//2
        items = numberOfItemsProducedByDays(machines, day)
        print(items,day)
        if items < goal:
            l = day 
        elif items > goal:
            r = day - 1
        else:
            return day
        
    return -1


print(min_time_required([2,3,2],10) == 8)
print(min_time_required([1,3,4],10) == 7)