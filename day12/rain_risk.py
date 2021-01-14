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
    
    def turn(self, action, value):
        rotation = value / 90
        if action == "L":
            self.dir -= rotation
        elif action == "R":
            self.dir += rotation
        else:
            raise ValueError("invalid navigation: %s" % action)
        
        self.dir %= 4

    def move(self, instructions):
        for instruction in instructions:
            action = instruction[0]
            value = int(instruction[1:])
            
            if action in self.total_distance:
                self.total_distance[action] += value
            elif action == "F":
                self.total_distance[self.translation[self.dir]] += value
            else:
                self.turn(action, value)

    def calc_manhattan_distance(self):
        n_s = abs(self.total_distance["N"] - self.total_distance["S"])
        e_w = abs(self.total_distance["E"] - self.total_distance["W"])

        print('Total Distance: %s' % (n_s + e_w))


def problem_1(instructions):
    boat = Boat(E)
    boat.move(instructions)
    boat.calc_manhattan_distance()
    print(json.dumps(boat.total_distance, indent=4))

if __name__ == "__main__":
    ap = argparse.ArgumentParser("Day 12")
 
    ap.add_argument("input_file", help='file to be read to answer question')
 
    args = ap.parse_args()
 
    instructions = parse_file(args.input_file)
 
    problem_1(instructions)
    # problem_2(instructions)
 