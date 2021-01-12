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


def is_valid(jolts, highest_jolts=None):
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


def is_valid_2(jolts, highest_jolts=None):
    if max(jolts) + 3 != highest_jolts and highest_jolts is not None:
        return False

    for idx in range(len(jolts)-1):
        if jolts[idx+1] - jolts[idx] > 3:
            return False
    return True


def find_candidates_2(jolts):
    candidates = []

    for idx in range(len(jolts)-1):
        if jolts[idx+1] - jolts[idx] < 3:
            candidates.append(jolts[idx+1])

    return candidates


def do_stuff_2(jolts, candidates, high):
    global count
    jolts_copy = copy.copy(jolts)
    can_copy = copy.copy(candidates)

    for candidate in candidates:
        jolts_copy.remove(candidate)
        
        if is_valid_2(jolts_copy, high):
            # print(jolts_copy[0:3], len(jolts_copy))
            can_copy.remove(candidate)
            count += 1
            do_stuff_2(jolts_copy, can_copy, high)
        jolts_copy = copy.copy(jolts)


def split_candidate(jolts):
    candidates = []
    candidate = []
    prev_jolt = 0
    sub = 0
    restart = False
    for jolt in jolts:
        if restart:
            sub = jolt
            restart = 0
        jolt -= sub
        candidate.append(jolt)
        if jolt - prev_jolt > 2:
            candidates.append(candidate)
            candidate = []
            # print(jolt + sub)
            restart = True

        prev_jolt = jolt
    print(candidates)
    return candidates



def problem_2(jolts):
    global count
    jolts.sort()
    jolts.insert(0,0)
    things = split_candidate(jolts)
    product = 1
    for thing in things:
        highest = max(thing) + 3
        candidates = find_candidates(thing)
        do_stuff_2(thing, candidates, highest)
        product *= count
        print(count)
        count = 1
        
    print(product)



    # with open("foo.txt", 'w') as f:
    #     for jolt in jolts:
    #         f.write(str(jolt) + '\n')
    # highest_jolts = max(jolts) + 3
    # print(len(jolts))
    # # print(highest_jolts)
    # # print(jolts)
    # candidates = find_candidates(jolts)
    # print(candidates, len(candidates))
    # do_stuff(jolts, candidates, highest_jolts)
    # print("total: %s" % count)


if __name__ == "__main__":
    ap = argparse.ArgumentParser("Day 10: Adapter Array")
    ap.add_argument('input_file', help="txt file containig a bunch of numbers")

    args = ap.parse_args()

    jolts = parse_input(args.input_file)
    # problem_1(int(args.nums), jolts)
    problem_2(jolts)
