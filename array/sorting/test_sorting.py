from bubble_sort import bubble_sort
def test_bubble_sort():
    arr =[1,5,2,4,12,4,7,23,4,332]
    bubble_sort(arr)

    assert arr == sorted(arr)
