from abc import ABC, abstractmethod

from draw import Drawer

from .entity import Entity


class DynamicEntity(Entity, ABC):
    def __init__(self, drawer: Drawer, x: int, y: int, size: int, map) -> None:
        super().__init__(drawer, x, y, size)
        self._map = map

    @abstractmethod
    def move_up(self) -> None: ...
    @abstractmethod
    def move_left(self) -> None: ...
    @abstractmethod
    def move_down(self) -> None: ...
    @abstractmethod
    def move_right(self) -> None: ...
