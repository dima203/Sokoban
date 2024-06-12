from abc import ABC, abstractmethod


class Drawer(ABC):
    @abstractmethod
    def set_surface(self, surface) -> None: ...

    @abstractmethod
    def draw_rectangle(self, x: int, y: int, width: int, height: int,
                       color: tuple[int, int, int] = (255, 255, 255)) -> None: ...

    @abstractmethod
    def draw_circle(self, x: int, y: int, radius: int, color: tuple[int, int, int] = (255, 255, 255)) -> None: ...

    @abstractmethod
    def draw_line(self, x1: int, y1: int, x2: int, y2: int) -> None: ...
