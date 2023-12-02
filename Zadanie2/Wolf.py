def calculate_manhattan_distance(sheep, x, y):
    return abs(x - sheep.x) + abs(y - sheep.y)


def calculate_euclidean_distance(sheep, x, y):
    return ((x - sheep.x) ** 2 + (y - sheep.y) ** 2) ** 0.5


class Wolf:
    def __init__(self, spawn):
        self.x: float = 0.0
        self.y: float = 0.0
        self.direction: str = ""
        self.speed: int = spawn
        self.smallest_dist: float = 0.0

    def run(self, new_direction):
        if new_direction == "up":
            self.y += self.speed
        elif new_direction == "right":
            self.x += self.speed
        elif new_direction == "down":
            self.y -= self.speed
        elif new_direction == "left":
            self.x -= self.speed
        self.direction = new_direction

    def choose_direction(self, sheep):
        arr = [calculate_euclidean_distance(sheep, self.x, self.y + 1),
               calculate_euclidean_distance(sheep, self.x + 1, self.y),
               calculate_euclidean_distance(sheep, self.x, self.y - 1),
               calculate_euclidean_distance(sheep, self.x - 1, self.y)]
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
        distances = [calculate_euclidean_distance(sheep, self.x, self.y)
                     for sheep in sheeps if sheep.is_alive]
        self.smallest_dist = min(distances)
        return distances.index(min(distances))

    def __str__(self):
        return f"Wolf: x={self.x} y={self.y} direction={self.direction} speed={self.speed}"
