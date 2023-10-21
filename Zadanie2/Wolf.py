import random


class Wolf:
    __x: float = 0
    __y: float = 0
    __direction: str = ""
    __speed: float = 1

    def __init__(self, direction, num_of_sheeps):
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

    def calculate_distance(self, sheep):
        return ((self.__x - sheep.get_x()) ** 2 + (self.__y - sheep.get_y()) ** 2) ** 0.5

    def pick_sheep(self, herd_of_sheeps):
        distances = [0.0 for _ in range(len(herd_of_sheeps))]
        for i, sheep in enumerate(herd_of_sheeps):
            distances[i] = self.calculate_distance(sheep)
        return distances.index(min(distances))

