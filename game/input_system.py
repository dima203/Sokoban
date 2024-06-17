import pygame


class InputSystem:
    def __init__(self) -> None:
        self.__keys = {
            pygame.K_UP: 'move_up',
            pygame.K_LEFT: 'move_left',
            pygame.K_DOWN: 'move_down',
            pygame.K_RIGHT: 'move_right',
            pygame.K_ESCAPE: 'close_game'
        }

        self.__callbacks = {
            'move_up': [],
            'move_left': [],
            'move_down': [],
            'move_right': [],
            'close_game': []
        }

    def add_callback(self, action_name: str, callback: callable) -> None:
        if action_name in self.__callbacks:
            self.__callbacks[action_name].append(callback)
        else:
            self.__callbacks[action_name] = [callback]

    def listen_events(self, event: pygame.event.Event) -> None:
        if event.type != pygame.KEYDOWN:
            return

        for key in self.__keys:
            if event.key == key:
                self.__call(key)

    def __call(self, key: int) -> None:
        for callback in self.__callbacks[self.__keys[key]]:
            callback()
