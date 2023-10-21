from Sheep import Sheep
import random
import json
from Wolf import Wolf


def info(herd_of_sheeps, wolf, num_of_rounds, num_alive, prey_index):
    print("------------------------------------")
    print("Round: ", num_of_rounds)
    print("Wolf: ", round(wolf.get_x(), 3), round(wolf.get_y(), 3))
    print("Alive sheeps: ", num_alive)
    if herd_of_sheeps[prey_index].is_alive:
        print("Sheep nr ", prey_index, " is being chased")
    else:
        print("Sheep nr ", prey_index, " is eaten")
    print("------------------------------------")


def main():
    num_of_rounds = 10
    switcher = {
        0: "up",
        1: "right",
        2: "down",
        3: "left"
    }
    herd_of_sheeps = [Sheep(switcher.get(random.randint(0, 3)), i) for i in range(5)]
    wolf = Wolf()
    num_alive = len(herd_of_sheeps)
    alive_sheeps = herd_of_sheeps
    for i in range(num_of_rounds):
        directions = [switcher.get(random.randint(0, 3)) for _ in range(num_alive)]
        for j, sheep in enumerate(alive_sheeps):
            sheep.run(directions[j])
        prey_index = wolf.pick_sheep(alive_sheeps)
        wolf.chase_sheep(alive_sheeps[prey_index])
        print(wolf.__str__())
        print(alive_sheeps[prey_index].__str__())
        print()


main()
