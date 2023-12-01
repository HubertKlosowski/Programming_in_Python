import random


class Sheep:
    def __init__(self, num, spawn, speed):
        self.__x: float = random.uniform(-spawn, spawn)
        self.__y: float = random.uniform(-spawn, spawn)
        self.__direction: str = ""
        self.__speed: float = speed
        self.is_alive: bool = True
        self.__sheep_id: int = num

    @property
    def sheep_id(self):
        return self.__sheep_id

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def direction(self):
        return self.__direction

    def run(self, new_direction):
        if new_direction == "up":
            self.__y += self.__speed
        if new_direction == "right":
            self.__x += self.__speed
        if new_direction == "down":
            self.__y -= self.__speed
        if new_direction == "left":
            self.__x -= self.__speed
        self.__direction = new_direction

    def __str__(self):
        return f"Sheep: x={self.__x} y={self.__y} direction={self.__direction} speed={self.__speed}"
