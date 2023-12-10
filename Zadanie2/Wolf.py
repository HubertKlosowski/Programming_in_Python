import math


def calculate_euclidean_distance(sheep, x, y):
    return ((x - sheep.x) ** 2 + (y - sheep.y) ** 2) ** 0.5


def calculate_new_coordinates(w1: list, w2: list) -> list:
    num = (w1[0] - w2[0]) / (w1[1] - w2[1])
    return [w2[0] + math.cos(math.atan(num)), w2[1] + math.sin(math.atan(num))]


class Wolf:
    def __init__(self, spawn):
        self.x: float = 0.0
        self.y: float = 0.0
        self.speed: int = spawn
        self.smallest_dist: float = 0.0

    def chase_sheep(self, sheeps):
        distances = [calculate_euclidean_distance(sheep, self.x, self.y)
                     for sheep in sheeps if sheep.is_alive]
        self.smallest_dist = min(distances)
        prey = distances.index(min(distances))
        res = calculate_new_coordinates(sheeps[prey].get_coordinates(), [self.x, self.y])
        self.x, self.y = res[0], res[1]
        return distances.index(min(distances))

    def __str__(self):
        return f"Wolf: x={self.x} y={self.y} speed={self.speed}"
