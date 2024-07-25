from binary_search import binary_search


def test_binary_search():
    assert binary_search([1, 3, 5, 7, 8, 12, 15, 23, 43], 5) == 2
    assert binary_search([1, 3, 5, 7, 8, 12, 15, 23, 43], 4) == -1
    assert binary_search([1, 3, 5, 7, 8, 12, 15, 23, 43, 56, 68, 87], 56) == 9
    assert binary_search([1, 3, 5, 7, 8, 12, 15, 23, 43, 56, 68, 87], 87) == 11
    assert binary_search([1, 3, 5, 7, 8, 12, 15, 23, 43, 56, 68, 87], 1) == 0
    assert binary_search([1, 3, 5, 7, 8, 12, 15, 23, 43, 56, 68, 87], 86) == -1
