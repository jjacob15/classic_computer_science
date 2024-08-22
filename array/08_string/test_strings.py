from making_anagrams import make_anagram
from sherlock_validate import sherlock
from special_str_again import special_str_again
from common_child import common_child
from how_many_substrings import how_many_substrings

def test_how_many_substrings():
    # assert how_many_substrings("aabaa",[[1,1],[1,4],[1,1],[1,4],[0,2]]) == [1,8,1,8,5]
    assert how_many_substrings("qqqqqqqqqqzrzrrzrzrrzrrzrzrrzrzrrzttttttttttttttttttttttttttttttttttttttttttttttttttttttqncpqzcxpbwa",
        [[61, 97], [15, 50], [68, 89], [74, 87], [70, 80], [53, 97], [49, 73], [86, 92], [85, 88], [10, 76], [70, 89], [41, 78], [7, 36], [31, 38], [19, 99], [91, 91], [86, 98], [21, 66], [91, 91], [49, 90], [44, 51], [12, 66], [86, 91], [42, 56], [6, 46], [52, 71], [10, 72], [86, 91], [74, 78], [17, 39], [38, 92], [6, 99], [90, 91], [88, 91], [57, 66], [19, 49], [3, 83], [42, 75], [69, 70], [95, 96], [77, 98], [76, 87], [59, 80], [47, 90], [68, 90], [4, 51], [89, 92], [69, 79], [0, 44], [49, 94], [27, 43], [40, 47], [42, 75], [68, 69], [59, 89], [62, 79], [34, 37], [52, 93], [31, 60], [19, 35], [14, 46], [93, 96], [62, 82], [74, 84], [44, 56], [96, 96], [80, 92], [41, 72], [80, 99], [17, 39], [0, 85], [68, 99], [35, 75], [89, 99], [57, 78], [99, 99], [64, 93], [29, 55], [93, 93], [32, 44], [55, 58], [98, 98], [81, 90], [19, 87], [14, 37], [67, 96], [2, 32], [25, 47], [51, 95], [46, 54], [69, 79], [64, 95], [61, 75], [0, 22], [78, 94], [6, 44], [0, 17], [0, 56], [46, 58], [35, 63]]) == [674, 633, 234, 92, 56, 998, 301, 26, 8, 2214, 193, 704, 439, 31, 3251, 1, 87, 1038, 1, 865, 29, 1488, 20, 106, 824, 191, 1956, 20, 11, 256, 1490, 4382, 3, 10, 46, 468, 3244, 562, 2, 3, 240, 67, 232, 950, 257, 1132, 10, 56, 994, 1041, 139, 29, 562, 2, 468, 154, 7, 867, 438, 139, 531, 10, 211, 56, 79, 1, 83, 497, 200, 256, 3659, 506, 821, 64, 232, 1, 441, 354, 1, 81, 7, 1, 49, 2349, 279, 442, 468, 256, 997, 37, 56, 503, 106, 256, 142, 745, 156, 1600, 79, 407]

def test_common_child():
    assert common_child('ABCD','ABDC') == 3
    assert common_child('HARRY','SALLY') == 2
    assert common_child('AA','BB') == 0
    assert common_child('SHINCHAN','NOHARAAA') == 3
    assert common_child('ABCDEF','FBDAMN') == 2

def test_special_str():
    s = "mnonopoo"
    assert special_str_again(len(s),s) == 12

    s = "abcbaba"
    assert special_str_again(len(s),s) == 10

    s = "aaaa"
    assert special_str_again(len(s),s) == 10

    s = "aabaa"
    assert special_str_again(len(s),s) == 9


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