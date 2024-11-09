from typing import TypeVar, List, Generic


T = TypeVar('T')


class InitMetrics(Generic[T]):
    
    def __init__(self):
        self.elements: List[T] = []


    def add_t(self, element: T):
        self.elements.append(element)
    
    
    
    def __iter__(self):
        return iter(self.elements)

    