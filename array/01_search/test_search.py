from binary_search import binary_search
from min_time_required import min_time_required
from maximum_subarray_sum import maximumSum

def test_maximum_sum():
    assert maximumSum([1,2,3],2) == 1
    assert maximumSum([3,3,9,9,5],7) == 6

def test_min_time_required():
    assert min_time_required([2,3,2],10) == 8
    assert min_time_required([1,3,4],10) == 7

def test_binary_search():
    assert binary_search([1, 3, 5, 7, 8, 12, 15, 23, 43], 5) == 2
    assert binary_search([1, 3, 5, 7, 8, 12, 15, 23, 43], 4) == -1
    assert binary_search([1, 3, 5, 7, 8, 12, 15, 23, 43, 56, 68, 87], 56) == 9
    assert binary_search([1, 3, 5, 7, 8, 12, 15, 23, 43, 56, 68, 87], 87) == 11
    assert binary_search([1, 3, 5, 7, 8, 12, 15, 23, 43, 56, 68, 87], 1) == 0
    assert binary_search([1, 3, 5, 7, 8, 12, 15, 23, 43, 56, 68, 87], 86) == -1
