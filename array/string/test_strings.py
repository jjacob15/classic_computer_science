from making_anagrams import make_anagram
from sherlock_validate import sherlock
from special_string import special_str_count

def test_special_str():
    s = "mnonopoo"
    assert special_str_count(len(s),s) == 12

    s = "abcbaba"
    assert special_str_count(len(s),s) == 10

    s = "aaaa"
    assert special_str_count(len(s),s) == 10

    s = "aabaa"
    assert special_str_count(len(s),s) == 9


def test_make_anagrams():
    b = "fcrxzwscanmligyxyvym"
    a = "jxwtrhvujlmrpdoqbisbwhmgpmeoke"
    assert make_anagram(a,b) == 30
def test_sherlock():
    a = "abcdefghhgfedecba"
    assert sherlock(a) == "YES"
    a  = "aabbcd"
    assert sherlock(a) == "NO"

    a  = "aaabbcc"
    assert sherlock(a) == "YES"

    a  = "aabbc"
    assert sherlock(a) == "YES"

    a  = "abcdeff"
    assert sherlock(a) == "YES"

    a  = "aaaabbcc"
    assert sherlock(a) == "NO"