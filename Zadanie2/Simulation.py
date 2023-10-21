from Sheep import Sheep
import random
from Wolf import Wolf


def info(herd_of_sheeps, wolf, num_of_rounds):
    print("Round: ", num_of_rounds)
    print("Wolf: ", wolf.get_x(), wolf.get_y())
    print("Alive sheeps: ", len([sheep for sheep in herd_of_sheeps if sheep.isAlive]))
    prey = wolf.pick_sheep(herd_of_sheeps)
    if prey.isAlive:
        print("Sheep nr ", prey, " is being chased")
    else:
        print("Sheep nr ", prey, " is eaten")


def main():
    num_of_rounds = 100
    switcher = {
        0: "up",
        1: "right",
        2: "down",
        3: "left"
    }
    herd_of_sheeps = [Sheep(switcher.get(random.randint(0, 3))) for _ in range(15)]
    wolf = Wolf(switcher.get(random.randint(0, 3)), len(herd_of_sheeps))
    print(herd_of_sheeps)
    for i in range(num_of_rounds):
        info(herd_of_sheeps, wolf, i)


main()
