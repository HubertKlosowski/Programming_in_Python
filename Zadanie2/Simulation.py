from Sheep import Sheep
import random
import json
from Wolf import Wolf, calculate_euclidean_distance
import os
import csv
import argparse
import configparser
import logging


def round_info(sheep: Sheep, wolf: Wolf, round_num: int, alive: int):
    print("-" * 20)
    print("Round: ", round_num)
    print("Wolf: ", format(wolf.get_x(), ".3f"), format(wolf.get_y(), ".3f"))
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
    with open("alive.csv", "a", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([round_num, alive])
    csv_file.close()


def simulation(moves: dict, alive: int, sheeps: list, wolf: Wolf, prey: int, i: int) -> tuple:
    alive_sheeps = [sheep for sheep in sheeps if sheep.is_alive]
    for sheep in alive_sheeps:
        sheep.run(moves.get(random.randint(0, 3)))
        logging.debug("Sheep nr " + str(sheep.get_sheep_id()) + " direction is: " + sheep.get_direction() + ".")
        logging.debug("Sheep nr " + str(sheep.get_sheep_id()) + " moved.")
    logging.info("All alive sheeps moved.")
    if prey == -1:
        try:
            prey = wolf.pick_sheep(alive_sheeps)
            logging.debug("Wolf picked sheep nr " + str(prey) + ".")
            logging.debug("Distance to sheep nr " + str(prey) + " is: " +
                          str(wolf.smallest_dist) + ".")
        except ValueError:
            logging.info("Simulation ended. All sheeps are dead.")
            print("Error! All sheeps are dead!")
            exit(0)
    wolf.chase_sheep(alive_sheeps[prey])
    logging.debug("Wolf direction is: " + wolf.get_direction() + ".")
    logging.debug("Wolf moved.")
    logging.info("Wolf is chasing sheep nr " + str(prey) + ".")
    if calculate_euclidean_distance(alive_sheeps[prey], wolf.get_x(), wolf.get_y()) <= 1:
        wolf.set_x(alive_sheeps[prey].get_x())
        wolf.set_y(alive_sheeps[prey].get_y())
        logging.info("Wolf ate sheep nr " + str(prey) + ".")
        alive_sheeps[prey].is_alive = False
        alive -= 1
        round_info(alive_sheeps[prey], wolf, i, alive)
        prey = -1
    else:
        round_info(alive_sheeps[prey], wolf, i, alive)
    return alive, prey


def check_ini_file(config: configparser.ConfigParser):
    if not os.path.exists("config.ini"):
        raise FileNotFoundError("Config file not found!")
    config.read("config.ini")
    if not config.has_section("Sheep"):
        raise configparser.NoSectionError("Sheep")
    if not config.has_section("Wolf"):
        raise configparser.NoSectionError("Wolf")
    if not config.has_option("Sheep", "InitPosLimit"):
        raise configparser.NoOptionError("InitPosLimit", "Sheep")
    if not config.has_option("Sheep", "MoveDist"):
        raise configparser.NoOptionError("MoveDist", "Sheep")
    if not config.has_option("Wolf", "MoveDist"):
        raise configparser.NoOptionError("MoveDist", "Wolf")
    info = [float(config["Sheep"]["InitPosLimit"]),
            float(config["Sheep"]["MoveDist"]),
            float(config["Wolf"]["MoveDist"])]
    if any(el < 0 for el in info) < 0:
        raise ValueError("Error! Values must be positive!")
    if not all(isinstance(el, float) for el in info):
        raise TypeError("Error! Wrong type of values!")
    return info


def main():
    if os.path.exists("pos.json"):
        with open("pos.json", "w") as file:
            json.dump([], file)
    if os.path.exists("alive.csv"):
        with open("alive.csv", "w") as file:
            file.truncate()
    if os.path.exists("chase.log"):
        with open("chase.log", "w") as file:
            file.truncate()
    parser = argparse.ArgumentParser()
    config = configparser.ConfigParser()
    (parser.add_argument
     ("-c", "--config", type=str, default="config.ini", help="Config file for sheep and wolf settings"))
    parser.add_argument("-l", "--log", type=str, default="chase.log", help="Log file")
    parser.add_argument("-r", "--rounds", type=int, default=50, help="Number of rounds")
    parser.add_argument("-s", "--sheep", type=int, default=15, help="Number of sheeps")
    parser.add_argument("-w", "--wait", action="store_true", help="Press key to pause simulation")
    args = parser.parse_args()
    num_of_rounds: int = args.rounds
    moves = {
        0: "up",
        1: "right",
        2: "down",
        3: "left"
    }
    info = check_ini_file(config)
    logging.basicConfig(filename="chase.log", level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")
    logging.debug("Config file values loaded." + str(info))
    sheeps: list = []
    for i in range(args.sheep):
        sheeps.append(Sheep(i, spawn=info[0], speed=info[1]))
        logging.debug("Initial position of sheep nr " + str(i) + " determined.")
    logging.info("Initial position of sheeps determined.")
    wolf = Wolf(info[2])
    alive, prey = len(sheeps), -1
    for i in range(num_of_rounds):
        logging.info("New rounded started. Round nr " + str(i))
        alive, prey = simulation(moves, alive, sheeps, wolf, prey, i)
        save_to_json(sheeps, wolf, i)
        logging.debug("Data saved to pos.json file.")
        save_to_csv(i, alive)
        logging.debug("Data saved to alive.csv file.")
        logging.info("Round nr " + str(i) + " ended. Number of alive sheeps: " + str(alive) + ".")
        if args.wait:
            input("Press Enter to continue...")
    logging.info("Simulation ended. Number of rounds reached limit.")
    logging.shutdown()


main()
