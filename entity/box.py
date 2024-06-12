from draw import Drawer

from .dynamic_entity import DynamicEntity


class Box(DynamicEntity):
    def __init__(self, drawer: Drawer, x: int, y: int, size: int, map) -> None:
        super().__init__(drawer, x, y, size, map)
        self.__color = (150, 100, 0)

    def draw(self) -> None:
        self._drawer.draw_rectangle(self._x, self._y, self._size, self._size, self.__color)

    def move_up(self) -> None:
        new_y = self._y - self._size
        if not self._map.check_collision(self, self._x, new_y, 0):
            return

        self._y = new_y

    def move_left(self) -> None:
        new_x = self._x - self._size
        if not self._map.check_collision(self, new_x, self._y, 1):
            return

        self._x = new_x

    def move_down(self) -> None:
        new_y = self._y + self._size
        if not self._map.check_collision(self, self._x, new_y, 2):
            return

        self._y = new_y

    def move_right(self) -> None:
        new_x = self._x + self._size
        if not self._map.check_collision(self, new_x, self._y, 3):
            return

        self._x = new_x

    def get_pos(self) -> tuple[int, int]:
        return self._x, self._y
