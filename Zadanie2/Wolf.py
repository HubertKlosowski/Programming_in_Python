def calculate_manhattan_distance(sheep, x, y):
    return abs(x - sheep.get_x()) + abs(y - sheep.get_y())


def calculate_euclidean_distance(sheep, x, y):
    return ((x - sheep.get_x()) ** 2 + (y - sheep.get_y()) ** 2) ** 0.5


class Wolf:
    def __init__(self):
        self.__x: float = 0.0
        self.__y: float = 0.0
        self.__direction: str = ""
        self.__speed: int = 1

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

    def choose_direction(self, sheep):
        arr = [calculate_euclidean_distance(sheep, self.__x, self.__y + 1),
               calculate_euclidean_distance(sheep, self.__x + 1, self.__y),
               calculate_euclidean_distance(sheep, self.__x, self.__y - 1),
               calculate_euclidean_distance(sheep, self.__x - 1, self.__y)]
        return arr.index(min(arr))

    def chase_sheep(self, prey):
        moves = {
            0: "up",
            1: "right",
            2: "down",
            3: "left"
        }
        self.run(moves.get(self.choose_direction(prey)))

    def pick_sheep(self, sheeps):
        distances = [calculate_euclidean_distance(sheep, self.__x, self.__y)
                     for sheep in sheeps if sheep.is_alive]
        return distances.index(min(distances))

    def __str__(self):
        return ("Wolf: x=" + str(self.__x) + " y=" + str(self.__y) +
                " direction=" + self.__direction +
                " speed=" + str(self.__speed))
