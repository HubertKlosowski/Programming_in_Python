def calculate_euclidean_distance(sheep, wolf):
    return ((wolf[0] - sheep[0]) ** 2 + (wolf[1] - sheep[1]) ** 2) ** 0.5


def calculate_new_coordinates(w1: list, w2: list) -> list:
    d = calculate_euclidean_distance(w1, w2)
    return [(w1[0] - w2[0]) / d, (w1[1] - w2[1]) / d]


class Wolf:
    def __init__(self, spawn):
        self.x: float = 0.0
        self.y: float = 0.0
        self.speed: int = spawn
        self.smallest_dist: float = 0.0

    def chase_sheep(self, sheeps):
        distances = [calculate_euclidean_distance(sheep.get_coordinates(), [self.x, self.y])
                     for sheep in sheeps if sheep.is_alive]
        self.smallest_dist = min(distances)
        prey = distances.index(min(distances))
        res = calculate_new_coordinates(sheeps[prey].get_coordinates(), [self.x, self.y])
        self.x += res[0]
        self.y += res[1]
        return distances.index(min(distances))

    def __str__(self):
        return f"Wolf: x={self.x} y={self.y} speed={self.speed}"
