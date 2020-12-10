import argparse
import copy
import math


def parse_input(input_file):
    """
    expected format:
    """
    rtn_list = []
    with open(input_file, 'r') as f:
        group = {}
        people = 0
        for line in f.readlines():
            if line == "\n":
                group["people"] = people
                rtn_list.append(group)
                people = 0
                group = {}
                continue

            ans = line.strip()
            people += 1
            for char in ans:
                if char not in group:
                    group[char] = 1
                else:
                    group[char] += 1
    
    group["people"] = people
    rtn_list.append(group)

    return rtn_list


def problem_1(answers):
    """

    """
    total = 0
    for ans in answers:
        print(ans)
        total += len(ans)
    print(total)
    return total

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

    answers = parse_input(args.input_file)
    # problem_1(answers)
    problem_2(answers)
