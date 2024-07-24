def luckBalance(k, contests):
    tup = []
    important_count = 0
    for c in contests:
        tup.append((c[0],c[1]))
        if c[1] ==1:
            important_count +=1
    if k ==0:
        return sum([item[0] for item in tup])
            
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