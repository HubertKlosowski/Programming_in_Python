import random


class Sheep:
    def __init__(self, num, spawn, speed):
        self.x: float = random.uniform(-spawn, spawn)
        self.y: float = random.uniform(-spawn, spawn)
        self.direction: str = ""
        self.speed: float = speed
        self.is_alive: bool = True
        self.sheep_id: int = num

    def run(self, new_direction):
        if new_direction == "up":
            self.y += self.speed
        if new_direction == "right":
            self.x += self.speed
        if new_direction == "down":
            self.y -= self.speed
        if new_direction == "left":
            self.x -= self.speed
        self.direction = new_direction

    def get_coordinates(self):
        return [self.x, self.y]

    def __str__(self):
        return f"Sheep: x={self.x} y={self.y} direction={self.direction} speed={self.speed}"
