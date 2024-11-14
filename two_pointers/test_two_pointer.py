from find_sum import find_sum
from remove_duplicate import remove_duplicate 
def test_find_sum1():
    arr = [1,2,3,6,9,10,14,47,87,99]
    target = 57
    assert find_sum(arr,target) == True
    
def test_find_sum2():
    arr = [1,2,3,6,9,10,14,47,87,99]
    target = 58
    assert find_sum(arr,target) == False


def test_remove_dups1():
    arr = [1,2,2,3,6,9,10,10,10,10,14,47,87,99]
    unique = [1,2,3,6,9,10,14,47,87,99]
    assert remove_duplicate(arr) == unique


    