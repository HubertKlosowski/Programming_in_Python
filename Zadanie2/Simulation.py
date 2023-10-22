from Sheep import Sheep
import random
import json
from Wolf import Wolf, calculate_manhattan_distance


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


def herd_info(herd_of_sheeps):
    for sheep in herd_of_sheeps:
        print(sheep.__str__())


def main():
    num_of_rounds = 100
    switcher = {
        0: "up",
        1: "right",
        2: "down",
        3: "left"
    }
    herd_of_sheeps = [Sheep(switcher.get(random.randint(0, 3)), i) for i in range(15)]
    dead_sheeps = []
    wolf = Wolf()
    num_alive = len(herd_of_sheeps)
    prey_index = -1
    choose = 1
    if choose == 1:
        for i in range(num_of_rounds):
            directions = [switcher.get(random.randint(0, 3)) for _ in range(num_alive)]
            herd_info(herd_of_sheeps)
            for j, sheep in enumerate(herd_of_sheeps):
                if sheep.is_alive:
                    sheep.run(directions[j])
            if prey_index == -1:
                prey_index = wolf.pick_sheep(herd_of_sheeps)
            wolf.chase_sheep(herd_of_sheeps[prey_index])
            if calculate_manhattan_distance(herd_of_sheeps[prey_index], wolf.get_x(), wolf.get_y()) <= 1:
                herd_of_sheeps[prey_index].is_alive = False
                dead_sheeps.append(herd_of_sheeps[prey_index])
                herd_of_sheeps.remove(herd_of_sheeps[prey_index])
                prey_index = -1
                num_alive -= 1
            # info(herd_of_sheeps, wolf, i, num_alive, prey_index)
    else:
        while num_alive != 0:
            directions = [switcher.get(random.randint(0, 3)) for _ in range(num_alive)]
            for j, sheep in enumerate(herd_of_sheeps):
                if sheep.is_alive:
                    sheep.run(directions[j])
            if prey_index == -1:
                prey_index = wolf.pick_sheep(herd_of_sheeps)
            wolf.chase_sheep(herd_of_sheeps[prey_index])
            if calculate_manhattan_distance(herd_of_sheeps[prey_index], wolf.get_x(), wolf.get_y()) <= 1:
                herd_of_sheeps[prey_index].is_alive = False
                dead_sheeps.append(herd_of_sheeps[prey_index])
                herd_of_sheeps.remove(herd_of_sheeps[prey_index])
                prey_index = -1
                num_alive -= 1
            # info(herd_of_sheeps, wolf, i, num_alive, prey_index)


main()
