from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from merge_sort import bottom_up_merge_sort,merge_sort_count
from quick_sort import quick_sort
from bribe import minimumBribes
from fraud_activity import fraud

sorted = [1, 2, 4, 4, 4, 5, 7, 12, 22, 23, 32, 332]

def test_merge_sort_count():
    assert merge_sort_count([1, 1, 1, 2, 2]) ==0
    assert merge_sort_count([2, 1, 3, 1, 2]) ==4
    assert merge_sort_count([1, 5, 3, 7]) ==1
    assert merge_sort_count([7, 5, 3, 1]) == 6


def test_fraud_activity():
    assert fraud([2, 3, 4, 2, 3, 6, 8, 4, 5],5) == 2

def test_bribe():
    assert minimumBribes([2,1,5,3,4]) == 3

def test_bribe1():
    assert minimumBribes([5,1, 2, 3, 7, 8, 6, 4]) == "Too chaotic"

def test_bribe2():
    assert minimumBribes([1, 2, 5, 3, 4, 7, 8, 6]) == 4

def test_bubble_sort():
    arr =[32,22,1,5,2,4,12,4,7,23,4,332]
    bubble_sort(arr)

    assert arr == sorted

def test_selection_sort():
    arr =[32,22,1,5,2,4,12,4,7,23,4,332]
    selection_sort(arr)

    assert arr == sorted

def test_insertion_sort():
    arr =[32,22,1,5,2,4,12,4,7,23,4,332]
    insertion_sort(arr)

    assert arr == sorted

def test_merge_sort():
    arr =[32,22,1,5,2,4,12,4,7,23,4,332]
    merge_sort(arr)
    assert arr == sorted
    
    arr2 = [7, 5, 3, 1]
    merge_sort(arr2)
    assert arr2 == [1,3,5,7]

    
def test_bottom_upmerge_sort():
    arr =[32,22,1,5,2,4,12,4,7,23,4,332]
    bottom_up_merge_sort(arr)

    assert arr == sorted

    

def test_quick_sort():
    arr =[32,22,1,5,2,4,12,4,7,23,4,332]
    quick_sort(arr)

    assert arr == sorted
