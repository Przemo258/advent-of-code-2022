from __future__ import annotations
from typing import Union


class File:
    name: str
    size: int
    parent: list

    def __init__(self, name: str, size: int, parent=None):
        self.name = name
        self.size = size
        self.parent = parent if parent is not None else []

    def __str__(self):
        return f'File {self.name} with a size of {self.size} with parent directory "{self.parent}"'

    def __add__(self, other: Union[File, int]):
        if type(other) == int:
            return self.size + other
        elif type(other) == File:
            return self.size + other.size
        else:
            return self.size

    def __radd__(self, other):
        if type(other) == int:
            return self.size + other
        elif type(other) == File:
            return self.size + other.size
        else:
            return self.size

    def set_parent(self, directory):
        self.parent = directory
