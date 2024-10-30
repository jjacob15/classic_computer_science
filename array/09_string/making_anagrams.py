# #populate all chars of a, iterate b and either remove if exists in a or add to another var for b.
#  Sum it up
from collections import defaultdict

def make_anagram(a,b):
    difference = defaultdict(int)
    only_b =0
    for char in a:
        difference[char] +=1 #populate all chars of a
    for char in b:
        if char in difference and difference[char] > 0:
            difference[char] -=1 # if char in b exists , remove that 
        else: 
            only_b +=1 # else add to whats only in b

    totalElementsA = sum(difference.values())
    return totalElementsA + only_b
