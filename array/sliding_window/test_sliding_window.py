from max_sum_subarr import max_sum_subarr
from longest_substring import longest_unique_substring

def test_max_sum_subarr():
    arr = [2,1,5,1,3,2,8,1,0]
    max_size = 3
    assert max_sum_subarr(arr,max_size) == 13

def test_max_longest_unique_substring():
    s = "abcabcbefgb"
    assert longest_unique_substring(s) == 5

def test_max_longest_unique_substring1():
    s = "abcabcbe"
    assert longest_unique_substring(s) == 3

def test_max_longest_unique_substring1():
    s = "abcdefghijklm"
    assert longest_unique_substring(s) == 13
