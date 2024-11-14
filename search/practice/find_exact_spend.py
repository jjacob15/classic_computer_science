from collections import defaultdict
def whatFlavors(cost, money):
    change_count = defaultdict(list)
    for i, c in enumerate(cost):
        change_count[c].append(i+1)
    
    for change,pos in change_count.items():
        remaining = money - change
        if len(pos) == 1 and remaining in change_count:
            return [pos[0],change_count[remaining][0]]
        elif len(pos) == 2 and  change * 2 == money:
            return pos



print(whatFlavors([2,1,3,5,6],5)) # [1,3]
print(whatFlavors([2,1,3,5,2],4)) # [1,5]