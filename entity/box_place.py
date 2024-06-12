from .static_entity import StaticEntity


class BoxPlace(StaticEntity):
    __color = (150, 0, 255)

    def draw(self) -> None:
        self._drawer.draw_circle(self._x + self._size // 2, self._y + self._size // 2, self._size // 4, self.__color)

    def get_pos(self) -> tuple[int, int]:
        return self._x, self._y
