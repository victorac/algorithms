from __future__ import annotations
from typing import Any, List, Optional, Union

class ArrayList:
    """Dynamically resizable array"""
    _array:List[Any] 
    _current_size:int
    _total_size:int
    _initial_size:int 

    @property
    def array(self) -> List[Any]:
        return self._array[:self._current_size]

    def __init__(self, array:Optional[List]=[], initial_size = 8):
        if array is None:
            array = []
        self._array = [value for value in array]
        self._current_size = len(self._array)
        if self._current_size < initial_size:
            diff = initial_size - self._current_size
            self._array = self._array + ([None] * diff)
        self._total_size = max(self._current_size, initial_size)
        self._initial_size = self._total_size        

    def add(self, value:Any) -> None:
        if self._current_size + 1 > self._total_size:
            self._array = self._array + [None for _ in range(self._total_size)]
            self._total_size = _total_size * 2
        self._array[self._current_size] = value
        self._current_size += 1

    def __getitem__(self, index:int) -> Any:
        if not isinstance(index, int):
            raise Exception("Index has to be integer value")
        if index < 0:
            raise IndexError("Index must be a positive integer")
        if index >= self._current_size:
            raise IndexError("Index not defined") 
        return self.array[index]

    def __setitem__(self, index:int, value:Any) -> None:
        if not isinstance(index, int):
            raise Exception("Index has to be integer value")
        if index < 0:
            raise IndexError("Index must be a positive integer")
        if index >= self._current_size:
            raise IndexError("Index not defined")
        self._array[index] = value

    def __str__(self) -> str:
        return str(self.array)
    
    def __repr__(self) -> str:
        return repr(self.array)
    
    def __len__(self) -> int:
        return self._current_size

    def __add__(self, other:Union[ArrayList, List]) -> self:
        new_array = type(self)(self.array)
        for value in other:
            new_array.add(value)     
        return new_array
    
    def __eq__(self, other):
        if isinstance(self, type(other)):
            if self._current_size == other._current_size:
                if self.array == other.array:
                    return True
        return False