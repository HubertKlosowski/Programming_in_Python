from Sheep import Sheep
import random
import json
from Wolf import Wolf, calculate_manhattan_distance
import os


def info(herd_of_sheeps: list, wolf: Wolf, num_of_rounds: int, num_alive: int, prey_index: int):
    print("------------------------------------")
    print("Round: ", num_of_rounds)
    print("Wolf: ", round(wolf.get_x(), 3), round(wolf.get_y(), 3))
    print("Alive sheeps: ", num_alive)
    if herd_of_sheeps[prey_index].is_alive:
        print("Sheep nr ", prey_index, " is being chased")
    else:
        print("Sheep nr ", prey_index, " is eaten")


def concat_sheeps(alive: list, dead: list) -> list:
    res: list = alive + dead
    res.sort(key=lambda sheep: sheep.get_number_of_sheep())
    return res


def round_to_json(all_sh: list, wolf: Wolf, num_of_rounds: int) -> dict:
    round_data = {
        "round_no": num_of_rounds,
        "wolf_pos": {
            "x": round(wolf.get_x(), 3),
            "y": round(wolf.get_y(), 3)
        },
        "sheep_pos": [(round(s.get_x(), 3), round(s.get_y(), 3)) if s.is_alive else None for s in all_sh]
    }
    return round_data


def save_to_json(rounds_data: list):
    if os.path.exists("pos.json"):
        print("xd")
    with open("pos.json", "a") as save_simulations:
        json.dump(rounds_data, save_simulations)


def simulation(switch: dict, alive: int, a_sh: list, wolf: Wolf, prey: int, i: int, d_sh: list, rounds: list) -> tuple:
    directions: list = [switch.get(random.randint(0, 3)) for _ in range(alive)]
    for j, sheep in enumerate(a_sh):
        if sheep.is_alive:
            sheep.run(directions[j])
    if prey == -1:
        prey = wolf.pick_sheep(a_sh)
    info(a_sh, wolf, i, alive, prey)
    wolf.chase_sheep(a_sh[prey])
    if calculate_manhattan_distance(a_sh[prey], wolf.get_x(), wolf.get_y()) <= 1:
        a_sh[prey].is_alive = False
        d_sh.append(a_sh[prey])
        a_sh.remove(a_sh[prey])
        prey = -1
        alive -= 1
    rounds.append(round_to_json(concat_sheeps(a_sh, d_sh), wolf, i))
    return alive, prey


def main():
    num_of_rounds: int = 10
    switch = {
        0: "up",
        1: "right",
        2: "down",
        3: "left"
    }
    herd_of_sheeps: list = [Sheep(switch.get(random.randint(0, 3)), i) for i in range(15)]
    rounds, dead_sheeps = [], []
    wolf = Wolf()
    num_alive, prey_index, choose = len(herd_of_sheeps), -1, 1
    if choose == 1:
        for i in range(num_of_rounds):
            num_alive, prey_index = (
                simulation(switch, num_alive, herd_of_sheeps, wolf, prey_index, i, dead_sheeps, rounds))
    else:
        num_of_rounds: int = 0
        while num_alive != 0:
            num_alive, prey_index = (
                simulation(switch, num_alive, herd_of_sheeps, wolf, prey_index, num_of_rounds, dead_sheeps, rounds))
            num_of_rounds += 1
    save_to_json(rounds)


main()
