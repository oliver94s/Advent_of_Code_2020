import argparse
import copy
import json


def parse_input(input_file):
    """
    expected format:
    """
    parsed = {}
    with open(input_file, 'r') as f:
        for line in f.readlines():
            contain_split = line.split('contain')
            bag = contain_split[0].strip()

            inner_bags = []
            insides = contain_split[1].split(',')
            for inside in insides:
                inside = inside.strip()
                if inside[-1] == '.':
                    inside = inside[:-1]
                inner_bags.append(inside)
            parsed[bag] = inner_bags

    return parsed


def who_can_hold_me(color, bags):
    # print(color)
    if color == "no other bag":
        return []
    
    holder = []
    for bag, inner_bag in bags.items():
        if 'shiny gold bag' in bag:
            continue
        for inner in inner_bag:
            if color in inner:
                holder.append(bag)
    # print(json.dumps(holder, indent=4))
    
    if holder == []:
        return []
    
    x = copy.copy(holder)
    for hold in x:
        holder.extend(who_can_hold_me(hold[:-1], bags))
    
    return holder

def problem_1(bags):
    """
    Trying to find the number of bags that would be able to contain a shiny gold bag
    """
    print(len(bags))
    total_bags = []

    holders = who_can_hold_me("shiny gold bag", bags)
    # print(json.dumps(holders, indent=4))
    total_bags.extend(holders)
    
    total_bags = set(total_bags)
    total_bags = sorted(total_bags)
    print(json.dumps(total_bags, indent=4))
    print(len(total_bags))
    return len(total_bags)


def problem_2(bags):
    



if __name__ == "__main__":
    ap = argparse.ArgumentParser("Day 7: Handy Haversacks")
    ap.add_argument('input_file', help="txt file containig a bunch of numbers")
    
    args = ap.parse_args()

    bags = parse_input(args.input_file)
    problem_1(bags)
    # problem_2(answers)
