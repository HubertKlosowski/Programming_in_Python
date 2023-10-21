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
    num_of_rounds = 100
    switcher = {
        0: "up",
        1: "right",
        2: "down",
        3: "left"
    }
    herd_of_sheeps = [Sheep(switcher.get(random.randint(0, 3)), i) for i in range(5)]
    for sheep in herd_of_sheeps:
        print(sheep.__str__())
    wolf = Wolf()
    print(wolf.__str__())
    num_alive = len(herd_of_sheeps)
    alive_sheeps = [sheep for sheep in herd_of_sheeps if sheep.is_alive]
    for i in range(num_of_rounds):
        directions = [switcher.get(random.randint(0, 3)) for _ in range(len(alive_sheeps))]
        for j, sheep in enumerate(alive_sheeps):
            sheep.run(directions[j])
        prey_index = wolf.pick_sheep(herd_of_sheeps)
        if herd_of_sheeps[prey_index].is_alive:
            wolf.chase_sheep(herd_of_sheeps[prey_index])
        else:
            prey_index = wolf.pick_sheep(herd_of_sheeps)
            alive_sheeps.pop(prey_index)
            num_alive -= 1
        info(herd_of_sheeps, wolf, i, num_alive, prey_index)


main()
