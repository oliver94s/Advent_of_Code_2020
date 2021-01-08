import argparse
import copy
import json
import math


def parse_input(input_file):
    rtn_list = []
    with open(input_file, 'r') as f:
        lines = f.readlines()
            
    for line in lines:
        rtn_list.append(int(line.strip()))
    
    return rtn_list


def problem_1(preamble, nums):
    for idx in range(0, len(nums)):
        target = nums[idx + preamble]
        print(target)
        found = False
        for head in range(idx, idx + preamble - 1):
            if nums[head] > target:
                continue
            print(nums[head])
            for tail in range(head + 1, idx + preamble):
                print(nums[tail])
                if nums[tail] > target:
                    continue
                if nums[head] + nums[tail] == target:
                    found = True
            if found:
                break
        if not found:
            print(target)
            return target


if __name__ == "__main__":
    ap = argparse.ArgumentParser("Day 9: Encoding Error")
    ap.add_argument('input_file', help="txt file containig a bunch of numbers")
    ap.add_argument('nums', help="preamble length")

    args = ap.parse_args()

    cmds = parse_input(args.input_file)
    problem_1(int(args.nums), cmds)
    # problem_2(cmds)
