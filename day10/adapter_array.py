import argparse
import copy
import json
import math


count = 1

def parse_input(input_file):
    rtn_list = []
    with open(input_file, 'r') as f:
        lines = f.readlines()
            
    for line in lines:
        rtn_list.append(int(line.strip()))
    
    return rtn_list


def is_valid(jolts, highest_jolts):
    # if max(jolts) + 3 != highest_jolts:
    #     # print(max(jolts) + 3)
    #     return False

    prev_jolt = 0

    for jolt in jolts:
        if jolt - prev_jolt > 3:
            return False
        prev_jolt = jolt

    return True


def find_candidates(jolts):
    candidates = []
    prev_jolt = 0
    for jolt in jolts[:-1]:
        if jolt - prev_jolt < 3:
            candidates.append(jolt)
        prev_jolt = jolt

    return candidates


def do_stuff(jolts, candidates, highest_jolts):
    global count
    jolts_copy = copy.copy(jolts)
    can_copy = copy.copy(candidates)

    for candidate in candidates:
        jolts_copy.remove(candidate)
        
        if is_valid(jolts_copy, highest_jolts):
            # print(jolts_copy[0:3], len(jolts_copy))
            can_copy.remove(candidate)
            count += 1
            do_stuff(jolts_copy, can_copy, highest_jolts)
        jolts_copy = copy.copy(jolts)



def problem_2(jolts):
    global count
    jolts.sort()
    with open("foo.txt", 'w') as f:
        for jolt in jolts:
            f.write(str(jolt) + '\n')
    highest_jolts = max(jolts) + 3
    print(len(jolts))
    # print(highest_jolts)
    # print(jolts)
    candidates = find_candidates(jolts)
    print(candidates, len(candidates))
    do_stuff(jolts, candidates, highest_jolts)
    print("total: %s" % count)


if __name__ == "__main__":
    ap = argparse.ArgumentParser("Day 10: Adapter Array")
    ap.add_argument('input_file', help="txt file containig a bunch of numbers")

    args = ap.parse_args()

    jolts = parse_input(args.input_file)
    # problem_1(int(args.nums), jolts)
    problem_2(jolts)
