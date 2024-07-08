from kadane import max_subarray_sum
from can_sum import can_sum,can_sum_tab
from how_sum import how_sum,how_sum_tab,how_sum_tab_all
from best_sum import best_sum
from can_construct import can_construct,can_construct_tab
from climbing_stairs import climbing_stairs,climbing_stairs_count,climbing_stairs_tabluation
from fib import fib;
from grid_traveler import grid_traveler

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

def test_can_construct2():
    result = can_construct_tab("abcdef", ["ab", "abc", "cd", "def", "abcd","ef","c"])
    assert len(result) == 4
    
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
   