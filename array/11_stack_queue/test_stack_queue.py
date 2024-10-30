from largest_rectange import largest_rectange
from min_max_riddle import min_max_riddle
from castle_on_the_grid import castle_on_the_grid

def test_min_max_riddle():
    assert min_max_riddle([6,3,5,1,12]) == [12,3,3,1,1]

    
def test_largest_rectangle():
    assert largest_rectange([3,2,3]) == 6
    assert largest_rectange([1,3,5,9,11]) == 18
    assert largest_rectange([11,11,10,10,10]) == 50


def test_castle_on_the_grid():
    grid = [
    ".X.",
    ".X.",
    "..."
]
    assert castle_on_the_grid(grid,0,0,0,2) == 3
    grid = [
        ".X..XX...X",
        "X.........",
        ".X.......X",
        "..........",
        "........X.",
        ".X...XXX..",
        ".....X..XX",
        ".....X.X..",
        "..........",
        ".....X..XX",
        ]
    assert castle_on_the_grid(grid,9,1,9,6) == 3