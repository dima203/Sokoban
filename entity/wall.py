from draw import Drawer

from .static_entity import StaticEntity


class Wall(StaticEntity):
    def draw(self) -> None:
        self._drawer.draw_rectangle(self._x, self._y, self._size, self._size)

    def get_pos(self) -> tuple[int, int]:
        return self._x, self._y
