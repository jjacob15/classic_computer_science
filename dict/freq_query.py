from collections import defaultdict
def freqQuery(queries):
    db = defaultdict(int)
    freq = defaultdict(int)
    result = []
    for instruction,val in queries:
        if instruction == 1:
            if db[val] > 0:
                freq[db[val]] -=1 # reduce previous freq
            db[val] +=1
            freq[db[val]] +=1 # increase current freq
        elif instruction ==2:
            if db[val] > 0: 
                freq[db[val]] -=1 # reduce previous freq
                db[val] -=1
                if db[val] > 0:
                    freq[db[val]] +=1 # increase current freq if its greater than zero
        elif instruction ==3:
            result.append(1 if freq[val] > 0 else 0)
    return result