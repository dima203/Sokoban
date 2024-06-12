import pygame

from .drawer import Drawer


class PygameDrawer(Drawer):
    __surface: pygame.Surface

    def set_surface(self, surface: pygame.Surface) -> None:
        self.__surface = surface

    def draw_rectangle(self, x: int, y: int, width: int, height: int,
                       color: tuple[int, int, int] = (255, 255, 255)) -> None:
        pygame.draw.rect(self.__surface, color, (x, y, width, height))

    def draw_circle(self, x: int, y: int, radius: int, color: tuple[int, int, int] = (255, 255, 255)) -> None:
        pygame.draw.circle(self.__surface, color, (x, y), radius)

    def draw_line(self, x1: int, y1: int, x2: int, y2: int) -> None:
        pass
