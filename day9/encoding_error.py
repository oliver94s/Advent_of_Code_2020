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

def find_invalid(preamble, nums):
    for idx in range(0, len(nums)):
        target = nums[idx + preamble]
        found = False
        for head in range(idx, idx + preamble - 1):
            if nums[head] > target:
                continue
        
            for tail in range(head + 1, idx + preamble):
                if nums[tail] > target:
                    continue
                if nums[head] + nums[tail] == target:
                    found = True
            if found:
                break
        
        if not found:
            print(target)
            return target


def problem_1(preamble, nums):
    print(find_invalid(preamble, nums))


def problem_2(preamble, nums):
    invalid = find_invalid(preamble, nums)

    
    for head in range(0, len(nums)):
        if nums[head] >= invalid:
            continue
        stuff = [nums[head]]

        for tail in range(head + 1, len(nums)):
            stuff.append(nums[tail])

            x = sum(stuff)

            if x == invalid:
                print('match')
                print(stuff)
                print(min(stuff) + max(stuff))
            elif x > invalid:
                break


if __name__ == "__main__":
    ap = argparse.ArgumentParser("Day 9: Encoding Error")
    ap.add_argument('input_file', help="txt file containig a bunch of numbers")
    ap.add_argument('nums', help="preamble length")

    args = ap.parse_args()

    cmds = parse_input(args.input_file)
    # problem_1(int(args.nums), cmds)
    problem_2(int(args.nums), cmds)
