import argparse
import copy
import math


def parse_input(input_file):
    """
    expected format:
    """
    rtn_list = []
    with open(input_file, 'r') as f:
        for line in f.readlines():
            group = {}
            if line == "\n":
                continue
            for char in line:
                group[char] = 0
            rtn_list.append(list(group.keys()))
    return rtn_list


def problem_1(seating):
    """

    """
    valid_pass = 0

    highest = 0

    row_max = 127
    col_max = 7

    for seat in seating:
        lower = 0
        upper = row_max
        for pos in seat[:-3]:
            if pos == "B":
                lower = math.ceil(upper - ((upper - lower) / 2))
            elif pos == "F":
                upper = int((upper + lower) / 2)
            else:
                raise ValueError("%s uhh should not be here" % pos)
        row = upper

        lower = 0
        upper = col_max
        for pos in seat[-3:]:
            if pos == "R":
                lower = math.ceil(upper - ((upper - lower) / 2))
            elif pos == "L":
                upper = int((upper + lower) / 2)
            else:
                raise ValueError("%s uhh should not be here" % pos)
        col = upper

        id = row * 8 + col
        if highest < id:
            highest = id
    print(highest)
    return valid_pass

def problem_2(seating):
    """

    """
    valid_pass = 0

    highest = 0

    row_max = 127
    col_max = 7
    taken_seats = []
    for seat in seating:
        lower = 0
        upper = row_max
        for pos in seat[:-3]:
            if pos == "B":
                lower = math.ceil(upper - ((upper - lower) / 2))
            elif pos == "F":
                upper = int((upper + lower) / 2)
            else:
                raise ValueError("%s uhh should not be here" % pos)
        row = upper

        lower = 0
        upper = col_max
        for pos in seat[-3:]:
            if pos == "R":
                lower = math.ceil(upper - ((upper - lower) / 2))
            elif pos == "L":
                upper = int((upper + lower) / 2)
            else:
                raise ValueError("%s uhh should not be here" % pos)
        col = upper

        id = row * 8 + col
        taken_seats.append(id)

    taken_seats.sort()
    
    y = [str(x) for x in taken_seats]
    print("\n".join(y))

    for idx in range(0, len(taken_seats)-1):
        if taken_seats[idx] <= 7:
            continue
        if taken_seats[idx] + 2 == taken_seats[idx+1]:
            print(taken_seats[idx])

    return valid_pass


if __name__ == "__main__":
    ap = argparse.ArgumentParser("Day 6: Custom Customs")
    ap.add_argument('input_file', help="txt file containig a bunch of numbers")
    
    args = ap.parse_args()

    answers = parse_input(args.input_file)
    problem_1(answers)
    # problem_2(answers)
