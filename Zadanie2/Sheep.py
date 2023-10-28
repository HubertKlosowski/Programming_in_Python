import random


class Sheep:
    def __init__(self, direction, num, spawn, speed):
        self.__x: float = random.uniform(-spawn, spawn)
        self.__y: float = random.uniform(-spawn, spawn)
        self.__direction: str = direction
        self.__speed: float = speed
        self.is_alive: bool = True
        self.__sheep_id: int = num

    def get_sheep_id(self):
        return self.__sheep_id

    def get_direction(self):
        return self.__direction

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

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
        return ("Sheep nr " + str(self.__sheep_id) +
                ": x=" + str(self.__x) + " y=" + str(self.__y) +
                " direction=" + self.__direction +
                " speed=" + str(self.__speed) +
                " alive=" + str(self.is_alive))
