from abc import ABC, abstractmethod

from draw import Drawer


class Entity(ABC):
    def __init__(self, drawer: Drawer, x: int, y: int, size: int) -> None:
        self._drawer = drawer
        self._x = x
        self._y = y
        self._size = size

    @abstractmethod
    def draw(self) -> None: ...
    @abstractmethod
    def get_pos(self) -> tuple[int, int]: ...
