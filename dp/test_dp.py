from array_string.kadane_max_subarray import max_subarray_sum
from can_sum import can_sum,can_sum_tab
from how_sum import how_sum,how_sum_tab,how_sum_tab_all
from best_sum import best_sum
from can_construct import can_construct,can_construct_tab
from climbing_stairs import climbing_stairs,climbing_stairs_count,climbing_stairs_tabluation
from fib import fib;
from grid_traveler import grid_traveler
from min_cost import min_cost
from knap_sack import knapsack
from max_array_sum import max_arr_sum
from abbreviation import abb


def test_abb():
    assert abb("AbcDE","ABDE") == "YES"
    assert abb("AbcDE","AFDE") == "NO"
    assert abb("AbCdE","AFE") == "NO"
    assert abb("beFgH","EFG") == "NO"
    assert abb("beFgH","EFH") == "YES"
    assert abb("Pi","P") == "YES"
    assert abb("AfPZN","APZNC") == "NO"
    assert abb("LDJAN","LJJM") == "NO"
    assert abb("UMKFW","UMKFW") == "YES"
    assert abb("sYOCa","YOCN") == "NO"
    



def test_max_arr_sum():
    assert max_arr_sum([-2,1,3,-4,5]) == 8
    assert max_arr_sum([3,7,4,6,5]) == 13
    assert max_arr_sum([2,1,5,8,4]) == 11
    assert max_arr_sum([3, 5, -7, 8, 10]) == 15

def test_knap_sack():
    values = [60, 100, 120]
    weights = [4, 3, 2]
    W = 15
    assert knapsack(values,weights,W) == 280    


def test_min_cost():
    grid = [[0 for i in range(3)] for j in range(3)]
    grid[0][0] = 4
    grid[0][1] = 9
    grid[0][2] = 7
    grid[1][0] = 3
    grid[1][1] = 8
    grid[1][2] = 5
    grid[2][0] = 1
    grid[2][1] = 2
    grid[2][2] = 6
    assert min_cost(grid) == 16

def test_max_subarray_sum():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert max_subarray_sum(nums) == 6


def test_can_sum():
    assert can_sum(7, [5, 3, 4]) == True


def test_can_sum1():
    assert can_sum(300, [14, 7]) == False


def test_can_sum_tab():
    assert can_sum_tab(7, [5, 3, 4]) == True


def test_can_sum1_tab():
    assert can_sum_tab(300, [14, 7]) == False


def test_how_sum():
    assert how_sum(7, [2, 4],) == None


def test_how_sum1():
    assert how_sum(7, [3, 4]) == [4, 3]


def test_how_sum2():
    assert how_sum(8, [2, 3, 5]) == [2, 2, 2, 2]


def test_how_sum3():
    assert how_sum(300, [7, 14]) == None

def test_how_sum_tab():
    assert how_sum_tab(7, [2, 4]) == None


def test_how_sum_tab1():
    assert how_sum_tab(7, [3, 4]) == [4, 3]

def test_how_sum_tab2():
    assert how_sum_tab(8, [2, 3, 5]) == [2, 2, 2, 2]


def test_how_sum_tab3():
    assert how_sum_tab(300, [7, 14]) == None

def test_how_sum_tab_all():
    assert len(how_sum_tab_all(8, [2, 3, 5])) == 6   


def test_best_sum():
    assert best_sum(8, [2, 3, 5]) == [5, 3]


def test_can_construct():
    result = can_construct("purple", ["purp", "p", "ur", "le", "purpl"])
    assert len(result) == 2
    assert result[0] == ["purp", "le"]
    assert result[1] == ["p", "ur","p","le"]

def test_can_construct1():
    result = can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd","ef","c"])
    assert len(result) == 4

# def test_can_construct2():
#     result = can_construct_tab("abcdef", ["ab", "abc", "cd", "def", "abcd","ef","c"])
#     assert len(result) == 4
    
def test_can_construct3():
    result = can_construct_tab("purple", ["purp", "p", "ur", "le", "purpl"])
    assert len(result) == 2

def test_climbing_stairs():
    result = climbing_stairs(5)

    assert len(result) == 8
   
def test_climbing_stairs1():
    result = climbing_stairs_count(5)
    assert result == 8

def test_climbing_stairs2():
    result = climbing_stairs_tabluation(5)
    assert result == 8

def test_fib():
    assert fib(6) == 8
   

def test_grid_traveler():
    assert grid_traveler(3,3) == 6

# def test_grid_traveler2():
#     assert grid_traveler(18,18) == 2333606220
   