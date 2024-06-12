from entity import DynamicEntity, Player, Box, BoxPlace
from draw import Drawer


class Map:
    __player: Player

    def __init__(self, drawer: Drawer, walls: list, box_places: list) -> None:
        self.__drawer = drawer
        self.__walls = walls
        self.__box_places = box_places
        self.__boxes = []

    def add_player(self, player: Player) -> None:
        self.__player = player

    def add_boxes(self, boxes) -> None:
        self.__boxes.extend(boxes)

    def redraw(self) -> None:
        for wall in self.__walls:
            wall.draw()

        for box_place in self.__box_places:
            box_place.draw()

        for box in self.__boxes:
            box.draw()

        self.__player.draw()

    def check_collision(self, entity: DynamicEntity, new_x: int, new_y: int, direction: int) -> bool:
        if isinstance(entity, Player):
            for wall in self.__walls:
                if wall.get_pos() == (new_x, new_y):
                    return False
            for box in self.__boxes:
                if (box_pos := box.get_pos()) == (new_x, new_y):
                    match direction:
                        case 0:
                            box.move_up()
                        case 1:
                            box.move_left()
                        case 2:
                            box.move_down()
                        case 3:
                            box.move_right()
                    if box.get_pos() != box_pos:
                        return True
                    else:
                        return False

        elif isinstance(entity, Box):
            for wall in self.__walls:
                if wall.get_pos() == (new_x, new_y):
                    return False
        return True

    def check_end(self) -> bool:
        return all(self.__check_box_place_active(box_place) for box_place in self.__box_places)

    def __check_box_place_active(self, box_place: BoxPlace) -> bool:
        for box in self.__boxes:
            if box.get_pos() == box_place.get_pos():
                return True

        return False
