from sherlock_anagram import sherlock
from counting_triplets import counting_triplets
from freq_query import freqQuery

def test_sherlock1():
    assert sherlock("abba") == 4
    assert sherlock("abcd") == 0
    assert sherlock("ifailuhkqq") == 3
    assert sherlock("kkkk") == 10

def test_sherlock():
    assert counting_triplets([1,3,9,9,27,81],3) == 6
    assert counting_triplets([1, 5, 5, 25, 125],5) == 4

def test_freqQuery():
    assert freqQuery([(1, 1),(2,2),(3,2),(1,1),(1,1),(2,1),(3,2)]) == [0,1]
    assert freqQuery([(1,5),(1,6),(3,2),(1,10),(1,10),(1,6),(2,5),(3,2)]) == [0,1]
    assert freqQuery([(1,5),(1,6),(3,2),(1,10),(1,10),(1,6),(2,5),(3,2)]) == [0,1]