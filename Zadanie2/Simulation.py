from Sheep import Sheep
import random
import json
from Wolf import Wolf


def info(herd_of_sheeps, wolf, num_of_rounds):
    print("Round: ", num_of_rounds)
    print("Wolf: ", round(wolf.get_x(), 3), round(wolf.get_y(), 3))
    print("Alive sheeps: ", len([sheep for sheep in herd_of_sheeps if sheep.is_alive]))
    prey_index = wolf.pick_sheep(herd_of_sheeps)
    if herd_of_sheeps[prey_index].is_alive:
        print("Sheep nr ", prey_index, " is being chased")
    else:
        print("Sheep nr ", prey_index, " is eaten")


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
    for i in range(num_of_rounds):
        directions = [switcher.get(random.randint(0, 3)) for _ in range(len(herd_of_sheeps))]
        for j, sheep in enumerate(herd_of_sheeps):
            sheep.run(directions[j])
        prey_index = wolf.pick_sheep(herd_of_sheeps)
        if herd_of_sheeps[prey_index].is_alive:
            wolf.chase_sheep(herd_of_sheeps[prey_index])
        # info(herd_of_sheeps, wolf, i)
        print(wolf.toString())
        print(herd_of_sheeps[prey_index].toString())


main()
