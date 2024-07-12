from sherlock_anagram import sherlock

def test_sherlock():
    assert sherlock("abba") == 4
    assert sherlock("abcd") == 0
    assert sherlock("ifailuhkqq") == 3
    assert sherlock("kkkk") == 10