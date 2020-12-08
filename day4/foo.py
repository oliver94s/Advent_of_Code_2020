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


def problem_2(num_list):
    valid_pass = 0
    req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    
    for entry in passports:
        fields = list(entry.keys())
        if 'cid' in fields:
            fields.remove('cid')
        if len(fields) != len(req_fields):
            continue

        b_year = int(entry['byr'])
        if not (b_year >= 1920 and b_year <= 2002):
            print("birth year: %s" % b_year)
            continue
        
        iyr = int(entry['iyr'])
        if not (iyr >= 2010 and iyr <= 2020):
            print("Issue year: %s" % iyr)
            continue

        eyr = int(entry['eyr'])
        if not (eyr >= 2020 and eyr <= 2030):
            print("expiration year: %s" % eyr)
            continue

        hgt = int(entry['hgt'][:-2])
        unit = entry['hgt'][-2:]
        if unit == 'cm':
            print("height cm: %s" % hgt)
            if not (hgt >= 150 and hgt <= 193):
                print("height cm: %s" % hgt)
                continue
            
        elif unit == 'in':
            print("height in: %s" % hgt)
            if not (hgt >= 59 and hgt <= 76):
                print("height in: %s" % hgt)
                continue
        else:
            continue
            raise ValueError('%s needs to be either in or cm' % hgt)

        hcl = entry['hcl'][1:]
        if len(hcl) != 6:
            print('hair color: %s' % hcl)
            continue
        valid_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        v = True
        for char in hcl:
            if char not in valid_chars:
                v = False
        if not v:
            print('hair color: %s' % hcl)
            continue

        ecl = entry['ecl']
        valid_color = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if ecl not in valid_color:
            print('eye color: %s' % ecl)
            continue

        pid = entry['pid']
        if len(pid) != 9:
            print("passport id: %s" % pid)
            continue
        valid_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        
        v = True
        for char in pid:
            if char not in valid_chars:
                v = False
        if not v:
            print("passport id: %s" % pid)
            continue
        
        valid_pass += 1

    print(valid_pass)
    return valid_pass


if __name__ == "__main__":
    ap = argparse.ArgumentParser("Day 4: Passport Processing")
    ap.add_argument('input_file', help="txt file containig a bunch of numbers")
    
    args = ap.parse_args()

    passports = parse_input(args.input_file)
    problem_1(passports)
    problem_2(passports)