import argparse
import copy
import json
import math


def parse_file(input_file):
    nav = []
    
    with open(input_file, 'r') as f:
        for line in f.readlines():
           nav.append(line.strip()) 

    return nav

N = 0
E = 1
S = 2
W = 3

def turn(starting_dir, action, value):
    rotation = value / 90
    if action == "L":
        starting_dir -= rotation
    elif action == "R":
        starting_dir += rotation
    else:
        raise ValueError("invalid navigation: %s" % action)
    
    starting_dir %= 4
    return starting_dir


class Boat(object):
    def __init__(self, start_dir):
        self.dir = start_dir
        self.total_distance = {
            "N": 0,
            "E": 0,
            "S": 0,
            "W": 0
        }

        self.translation = {
            N: "N",
            E: "E",
            S: "S",
            W: "W"
        }
    
    def take_instruction(self, action, value):
        if action in self.total_distance:
            self.total_distance[action] += value
        elif action == "F":
            self.total_distance[self.translation[self.dir]] += value
        else:
            self.dir = turn(self.dir, action, value)


    def move(self, instructions):
        for instruction in instructions:
            action = instruction[0]
            value = int(instruction[1:])
            self.take_instruction(action, value)

    def waypoint_move(self, waypoint, action, value):
        if action != "F":
            raise ValueError("only accepting F as valid actions here")
        for key, val in waypoint.pos.items():
            if val:
                self.total_distance[key] += val * value

    def calc_manhattan_distance(self):
        n_s = abs(self.total_distance["N"] - self.total_distance["S"])
        e_w = abs(self.total_distance["E"] - self.total_distance["W"])

        print('Total Distance: %s' % (n_s + e_w))


def normalize_position(pos):
    new_pos = {
        "N": 0,
        "E": 0,
        "S": 0,
        "W": 0
    }
    n = pos["N"] - pos["S"]
    if n:
        new_pos["N"] = n
    else:
        new_pos["S"] = abs(n)
    
    e = pos["E"] - pos["W"]
    if e:
        new_pos["E"] = e
    else:
        new_pos["W"] = abs(e)

    return new_pos


class Waypoint(object):
    def __init__(self, starting_x, starting_y):
        self.pos = {
            "N": starting_y,
            "E": starting_x,
            "S": 0,
            "W": 0
        }
        self.pos = normalize_position(self.pos)
        self.int_to_str = {
            N: "N",
            E: "E",
            S: "S",
            W: "W"
        }

        self.str_to_int = {
            "N": N,
            "E": E,
            "S": S,
            "W": W
        }


    def clear_pos(self):
        self.pos = {
            "N": 0,
            "E": 0,
            "S": 0,
            "W": 0
        }

    def rotate(self, action, value):
        positions = []
        for key, val in self.pos.items():
            if val:
                positions.append(key)
        
        exchanges = []
        for pos in positions:
            int_dir = self.str_to_int[pos]
            new_dir = turn(int_dir, action, value)
            exchanges.append((self.int_to_str[new_dir], self.pos[pos]))
        
        self.clear_pos()
        
        for exchange in exchanges:
            self.pos[exchange[0]] = exchange[1]

    def take_instruction(self, action, value):
        if action in self.pos:
            self.pos[action] += value
            self.pos = normalize_position(self.pos)
        else:
            self.rotate(action, value)


def problem_1(instructions):
    boat = Boat(E)
    boat.move(instructions)
    boat.calc_manhattan_distance()
    print(json.dumps(boat.total_distance, indent=4))

def problem_2(instructions):
    boat = Boat(E)
    waypoint = Waypoint(10, 1)

    for instruction in instructions:
        action = instruction[0]
        value = int(instruction[1:])

        if action == "F":
            boat.waypoint_move(waypoint, action, value)
        else:
            waypoint.take_instruction(action, value)
            print(waypoint.pos)
    
    boat.calc_manhattan_distance()

if __name__ == "__main__":
    ap = argparse.ArgumentParser("Day 12")
 
    ap.add_argument("input_file", help='file to be read to answer question')
 
    args = ap.parse_args()
 
    instructions = parse_file(args.input_file)
 
    # problem_1(instructions)
    problem_2(instructions)
 