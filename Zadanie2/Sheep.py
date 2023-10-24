import random


class Sheep:
    def __init__(self, direction, num):
        self.__x: float = random.uniform(-10, 10)
        self.__y: float = random.uniform(-10, 10)
        self.__direction: str = direction
        self.__speed: float = 0.5
        self.is_alive: bool = True
        self.__number_of_sheep: int = num

    def get_number_of_sheep(self):
        return self.__number_of_sheep

    def get_direction(self):
        return self.__direction

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def run(self, new_direction):
        if new_direction == "up":
            self.__y += self.__speed
        elif new_direction == "right":
            self.__x += self.__speed
        elif new_direction == "down":
            self.__y -= self.__speed
        elif new_direction == "left":
            self.__x -= self.__speed
        self.__direction = new_direction

    def __str__(self):
        return ("Sheep nr " + str(self.__number_of_sheep) +
                ": x=" + str(self.__x) + " y=" + str(self.__y) +
                " direction=" + self.__direction +
                " speed=" + str(self.__speed) +
                " alive=" + str(self.is_alive))
