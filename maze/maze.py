from enum import Enum
from typing import List, NamedTuple, Callable, Optional
import random
from math import sqrt

class Cell(str, Enum):
    EMPTY = " "
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"


class MazeLocation(NamedTuple):
    row: int
    column: int    