from dataclasses import dataclass,field
from typing import TypeVar,Generic,List
T = TypeVar('T')


@dataclass
class Stack(Generic[T]):
    _container: List[T] = field(default_factory=list)

    def push(self, item:T)->None:
        self._container.append(item);
    
    def pop(self)->T:
        return self._container.pop();