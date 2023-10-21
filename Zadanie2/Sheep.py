import random


class Sheep:
    __x: float = random.uniform(-10, 10)
    __y: float = random.uniform(-10, 10)
    __direction: str = ""
    __speed: float = 0.5
    isAlive: bool = True

    def __init__(self, direction):
        self.__direction = direction

    def get_direction(self):
        return self.__direction

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def run(self):
        if self.__direction == "up":
            self.__y += self.__speed
        elif self.__direction == "right":
            self.__x += self.__speed
        elif self.__direction == "down":
            self.__y -= self.__speed
        elif self.__direction == "left":
            self.__x -= self.__speed
