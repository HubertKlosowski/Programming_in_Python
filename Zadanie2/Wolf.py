class Wolf:
    __x: float = 0
    __y: float = 0
    __direction: str = ""
    __speed: float = 1

    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__direction = ""

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

    def chase_sheep(self, prey):
        if abs(self.__x - prey.get_x()) < 1 and abs(self.__y - prey.get_y()) < 1:
            prey.is_alive = False
        switcher = {
            0: "up",
            1: "right",
            2: "down",
            3: "left"
        }
        if self.__x < prey.get_x():
            self.run(switcher.get(1))
        elif self.__x > prey.get_x():
            self.run(switcher.get(3))
        elif self.__y < prey.get_y():
            self.run(switcher.get(0))
        elif self.__y > prey.get_y():
            self.run(switcher.get(2))

    def calculate_distance(self, sheep):
        return ((self.__x - sheep.get_x()) ** 2 + (self.__y - sheep.get_y()) ** 2) ** 0.5

    def pick_sheep(self, herd_of_sheeps):
        distances = [0.0 for _ in range(len(herd_of_sheeps))]
        for i, sheep in enumerate(herd_of_sheeps):
            distances[i] = self.calculate_distance(sheep)
        return distances.index(min(distances))

    def toString(self):
        return ("Wolf: x=" + str(self.__x) + " y=" + str(self.__y) +
                " direction=" + self.__direction +
                " speed=" + str(self.__speed))

