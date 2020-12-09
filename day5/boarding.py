import argparse
import copy


def parse_input(input_file):
    """
    expected format:
    8-16 h: wqhjvhlgwtsgvlpf
    """
    rtn_list = []
    with open(input_file, 'r') as f:
        passport = {}
        for line in f.readlines():
            if line == "\n":
                rtn_list.append(copy.copy(passport))
                passport = {}
                continue

            split_spaces = line.split(' ')

            for space in split_spaces:
                k, v = space.split(':')
                passport[k] = v.strip()

    return rtn_list


def problem_1(passports):
    """

    """
    valid_pass = 0
    req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    
    for entry in passports:
        fields = list(entry.keys())
        if 'cid' in fields:
            fields.remove('cid')
        if len(fields) == len(req_fields):
            valid_pass += 1

    print(valid_pass)
    return valid_pass


if __name__ == "__main__":
    ap = argparse.ArgumentParser("Day 5: Binary Boarding")
    ap.add_argument('input_file', help="txt file containig a bunch of numbers")
    
    args = ap.parse_args()

    passports = parse_input(args.input_file)
    problem_1(passports)
