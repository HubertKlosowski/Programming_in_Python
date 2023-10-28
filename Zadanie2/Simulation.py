from Sheep import Sheep
import random
import json
from Wolf import Wolf, calculate_euclidean_distance
import os
import csv
import argparse
import configparser


def info(sheep: Sheep, wolf: Wolf, round_num: int, alive: int):
    print("-" * 20)
    print("Round: ", round_num)
    print("Wolf: ", format(wolf.get_x(), '.3f'), format(wolf.get_y(), '.3f'))
    print("Alive sheeps: ", alive)
    if sheep.is_alive:
        print("Sheep nr", sheep.get_sheep_id(), "is being chased")
    else:
        print("Sheep nr", sheep.get_sheep_id(), "is eaten")


def save_to_json(sheeps: list, wolf: Wolf, round_num: int):
    round_data = {
        "round_no": round_num,
        "wolf_pos": {
            "x": round(wolf.get_x(), 3),
            "y": round(wolf.get_y(), 3)
        },
        "sheep_pos": [(round(s.get_x(), 3), round(s.get_y(), 3)) if s.is_alive else None for s in sheeps]
    }
    try:
        with open("pos.json", "r") as json_file:
            sim_data = json.load(json_file)
    except FileNotFoundError:
        sim_data = []
    sim_data.append(round_data)
    with open("pos.json", "w") as json_file:
        json.dump(sim_data, json_file, indent=2)
    json_file.close()


def save_to_csv(round_num: int, alive: int):
    with open("alive.csv", "a", newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([round_num, alive])
    csv_file.close()


def simulation(alive: int, sheeps: list, wolf: Wolf, prey: int, i: int) -> tuple:
    alive_sheeps = [sheep for sheep in sheeps if sheep.is_alive]
    if prey == -1:
        try:
            prey = wolf.pick_sheep(alive_sheeps)
        except ValueError:
            print("Error! All sheeps are dead!")
            exit(0)
    wolf.chase_sheep(alive_sheeps[prey])
    if calculate_euclidean_distance(alive_sheeps[prey], wolf.get_x(), wolf.get_y()) <= 1:
        alive_sheeps[prey].is_alive = False
        alive -= 1
        info(alive_sheeps[prey], wolf, i, alive)
        prey = -1
    else:
        info(alive_sheeps[prey], wolf, i, alive)
    return alive, prey


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--rounds", type=int, default=50, help="Number of rounds")
    parser.add_argument("-s", "--sheep", type=int, default=15, help="Number of sheeps")
    parser.add_argument("-w", "--wait", action="store_true", help="Press key to pause simulation")
    args = parser.parse_args()
    if os.path.exists("pos.json"):
        with open("pos.json", "w") as file:
            json.dump([], file)
    if os.path.exists("alive.csv"):
        with open("alive.csv", "w") as file:
            file.truncate()
    num_of_rounds: int = args.rounds
    moves = {
        0: "up",
        1: "right",
        2: "down",
        3: "left"
    }
    sheeps: list = [Sheep(moves.get(random.randint(0, 3)), i) for i in range(args.sheep)]
    wolf = Wolf()
    alive, prey = len(sheeps), -1
    for i in range(num_of_rounds):
        alive, prey = simulation(alive, sheeps, wolf, prey, i)
        save_to_json(sheeps, wolf, i)
        save_to_csv(i, alive)
        if args.wait:
            input("Press any key to continue...")


main()
