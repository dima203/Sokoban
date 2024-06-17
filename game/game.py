import pygame

from draw import PygameDrawer
from entity import Wall, BoxPlace, Box, Player

from .map import Map
from .input_system import InputSystem


class Game:
    __clock: pygame.time.Clock
    __window: pygame.Surface
    __running = False

    def __init__(self) -> None:
        self.__drawer = PygameDrawer()

        self.__map = Map(
            self.__drawer,
            [
                Wall(self.__drawer, 100, 100, 50),
                Wall(self.__drawer, 150, 100, 50),
                Wall(self.__drawer, 200, 100, 50),
                Wall(self.__drawer, 250, 100, 50),
                Wall(self.__drawer, 300, 100, 50),
                Wall(self.__drawer, 100, 150, 50),
                Wall(self.__drawer, 100, 200, 50),
                Wall(self.__drawer, 100, 250, 50),
                Wall(self.__drawer, 100, 300, 50),
                Wall(self.__drawer, 100, 350, 50),
                Wall(self.__drawer, 150, 350, 50),
                Wall(self.__drawer, 200, 350, 50),
                Wall(self.__drawer, 250, 350, 50),
                Wall(self.__drawer, 300, 350, 50),
                Wall(self.__drawer, 300, 150, 50),
                Wall(self.__drawer, 300, 200, 50),
                Wall(self.__drawer, 300, 250, 50),
                Wall(self.__drawer, 300, 300, 50),
                Wall(self.__drawer, 300, 350, 50),
            ],
            [
                BoxPlace(self.__drawer, 150, 150, 50),
                BoxPlace(self.__drawer, 250, 150, 50)
            ]
        )

        self.__input_system = InputSystem()
        self.__player = Player(self.__drawer, 200, 300, 50, self.__map)
        self.__input_system.add_callback('move_up', self.__player.move_up)
        self.__input_system.add_callback('move_left', self.__player.move_left)
        self.__input_system.add_callback('move_down', self.__player.move_down)
        self.__input_system.add_callback('move_right', self.__player.move_right)
        self.__input_system.add_callback('close_game', self.__stop)
        self.__map.add_player(self.__player)
        box1 = Box(self.__drawer, 200, 200, 50, self.__map)
        box2 = Box(self.__drawer, 200, 250, 50, self.__map)
        self.__map.add_boxes([box1, box2])

    def run(self) -> None:
        pygame.init()
        self.__clock = pygame.time.Clock()
        self.__window = pygame.display.set_mode((1280, 720))
        self.__drawer.set_surface(self.__window)
        self.__running = True

        while self.__running:
            for event in pygame.event.get():
                self.__input_system.listen_events(event)

            if self.__map.check_end():
                self.__stop()

            self.__tick()

    def __stop(self) -> None:
        self.__running = False

    def __tick(self) -> None:
        self.__window.fill((0, 0, 0))
        self.__map.redraw()
        pygame.display.flip()
        self.__clock.tick(60)
