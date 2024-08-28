from largest_rectange import largest_rectange
from min_max_riddle import min_max_riddle

def test_min_max_riddle():
    assert min_max_riddle([6,3,5,1,12]) == [12,3,3,1,1]

    
def test_largest_rectangle():
    assert largest_rectange([3,2,3]) == 6
    assert largest_rectange([1,3,5,9,11]) == 18
    assert largest_rectange([11,11,10,10,10]) == 50
