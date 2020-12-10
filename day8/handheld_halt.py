import argparse
import copy
import math


def parse_input(input_file):
    rtn_list = []
    with open(input_file, 'r') as f:
        lines = f.readlines()
            
    for line in lines:
        space_split = line.split(" ")
        rtn_list.append(space_split)
    
    return rtn_list


def problem_1(commands):
    """

    """
    accumulator = 0
    idx = 0
    cmds = {}
    while idx <= len(commands):
        if idx not in cmds:
            cmds[idx] = 1
        else:
            cmds[idx] += 1
            break
        cmd = commands[idx]
        action = cmd[0]
        value = int(cmd[1])
        if action == 'acc':
            accumulator += value
        
        if action == 'jmp':
            idx += value
        else:
            idx += 1

    print(accumulator)



def problem_2(answers):
    """

    """
    total = 0
    for ans in answers:
        print(ans)
        people = ans['people']
        valid = True
        count = 0
        for letter, val in ans.items():
            if letter == "people":
                continue

            if val == people:
                count += 1

        print(count)
        total += count

    print(total)
    return total

if __name__ == "__main__":
    ap = argparse.ArgumentParser("Day 6: Custom Customs")
    ap.add_argument('input_file', help="txt file containig a bunch of numbers")
    
    args = ap.parse_args()

    cmds = parse_input(args.input_file)
    problem_1(cmds)
    # problem_2(answers)
