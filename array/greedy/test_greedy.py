from fractional_knapsack import fractional_knapsack
from min_swap import minimumSwaps,minimumSwaps1
from luck_balance import luckBalance

def test_luck_balance():
    k = 3
    contests = [[5,1],[2 ,1],[1,1],[8,1],[10,0],[5,0]]
    assert luckBalance(k,contests) == 29

def test_min_sor():
    arr =[7,1,3,2,4,5,6]
    assert minimumSwaps1(arr) == 5

def test_min_sor1():
    arr =[8,45,35,84,79,12,74,92,81,82,61,32,36,1,65,44,89,40,28,20,97,90,22,87,48,26,56,18,49,71,23,34,59,54,14,16,19,76,83,95,31,30,69,7,9,60,66,25,52,5,37,27,63,80,24,42,3,50,6,11,64,10,96,47,38,57,2,88,100,4,78,85,21,29,75,94,43,77,33,86,98,68,73,72,13,91,70,41,17,15,67,93,62,39,53,51,55,58,99,46]
    assert minimumSwaps(arr) == 91

def test_fractional_ks():
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    assert fractional_knapsack(values, weights, capacity) == 240.0