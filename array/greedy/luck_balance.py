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
    print(tup)
    win_count = 0
    luck =0
    for item in tup:
        if item[0] < 0 and item[1] ==1 and k > win_count:
            win_count +=1
            luck -= item[0] 
        elif k == 0:
            win_count +=1
            luck -= item[0]
        else:
            luck += item[0]
            
    print(win_count,luck)
    return luck