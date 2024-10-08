from binary_search import binary_search
from min_time_required import min_time_required
from maximum_subarray_sum import maximumSum
from making_candies import minimumPasses
from swap_nodes import swap_nodes

def test_swap_nodes():
    # result =  swap_nodes([[2, 3], [-1, -1], [-1, -1]],[1, 1])
    # assert result[0] == [3,1,2]
    # assert result[1] == [2,1,3]

    result =  swap_nodes([[2, 3], [4, -1], [5, -1],[6, -1],[7, 8],[-1, 9],[-1, -1],[10, 11],[-1, -1],[-1, -1],[-1, -1]],[2,4])
    assert result[0] == [2,9,6,4,1,3,7,5,11,8,10]
    assert result[1] == [2,6,9,4,1,3,7,5,10,8,11]



def test_compute_candies_on_pass():
    assert minimumPasses(1,2,1,60) == 4
    # assert minimumPasses(3,1,2,12) == 3
    # assert minimumPasses(1,1,1_000_000_000_000,1_000_000_000_000) == 1_000_000_000_000
    # assert minimumPasses(1,10,1_00,10) == 1
    # assert minimumPasses(1,100,10_000_000_000,1_000_000_000_000) == 617737754

def test_maximum_sum():
    # assert maximumSum([1,2,3],2) == 1
    assert maximumSum([3,3,9,9,5],7) == 6
    # assert maximumSum([2,2,3,2,2,3,2,2,3],7) == 5

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
