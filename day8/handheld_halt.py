import argparse
import copy
import json
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


def check(cmd_stack, commands):
    while cmd_stack:
        cmd, ran_cmds, starting = cmd_stack.pop()
        print(ran_cmds, starting)
        print("do stuff %s" % len(commands))
        action = cmd[0]
        if action == 'nop' or action == 'jmp':
            if action == 'nop':
                action = 'jmp'
            else:
                action = 'nop'
            commands[starting][0] = action
            if do_i_end(starting, ran_cmds, commands):
                print("found the problem at %s" % starting)
                return commands

def do_i_end(starting_line, ran_cmds, commands):
    """

    """
    accumulator = 0
    idx = starting_line
    valid = True
    while idx < len(commands):
        cmd = commands[idx]
        
        if idx not in ran_cmds:
            ran_cmds[idx] = 1
        else:
            ran_cmds[idx] += 1
            valid = False
            break

        action = cmd[0]
        value = int(cmd[1])
        if action == 'acc':
            accumulator += value
        
        if action == 'jmp':
            idx += value
        else:
            idx += 1

    # print(accumulator)
    print(json.dumps(ran_cmds, indent=4))
    return valid

def problem_2(commands):
    """

    """
    accumulator = 0
    idx = 0
    ran_cmds = {}
    cmd_stack = []
    while idx < len(commands):
        cmd = commands[idx]
        cmd_stack.append((cmd, copy.copy(ran_cmds), idx))
        
        if idx not in ran_cmds:
            ran_cmds[idx] = 1
        else:
            cmd_stack.pop()
            new_command = check(cmd_stack, commands)
            print(json.dumps(new_command, indent=4))
            print("broken")
            problem_2(new_command)
            break
        

        action = cmd[0]
        value = int(cmd[1])
        if action == 'acc':
            accumulator += value
        
        if action == 'jmp':
            idx += value
        else:
            idx += 1

    print(accumulator)

if __name__ == "__main__":
    ap = argparse.ArgumentParser("Day 6: Custom Customs")
    ap.add_argument('input_file', help="txt file containig a bunch of numbers")
    
    args = ap.parse_args()

    cmds = parse_input(args.input_file)
    problem_1(cmds)
    problem_2(cmds)
