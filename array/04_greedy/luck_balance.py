#the goal was to only win whats necessary so you don't lose your luck
# balance. So created a tuple array and got the imp count
# sorted by asc luck value so you can reduce only the ones with
# with the least luck value.

def luckBalance(k, contests):
    tup = []
    important_count = 0
    for c in contests:
        tup.append((c[0],c[1]))
        if c[1] ==1:
            important_count +=1
            
    tup.sort(key=lambda x: x[0])
    luck =0
    win_count = 0
    to_win = important_count - k
    for item in tup:
        if win_count < to_win and item[1] == 1:
            win_count +=1
            luck -= item[0] 
        else:
            luck += item[0]
    return luck