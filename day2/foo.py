import argparse



def parse_input(input_file):
    """
    expected format:
    8-16 h: wqhjvhlgwtsgvlpf
    """
    num_list = []
    with open(input_file, 'r') as f:
        for line in f.readlines():
            split_space = line.split(' ')
            d = {
                "lower": int(split_space[0].split('-')[0]),
                "upper": int(split_space[0].split('-')[1]),
                "letter": split_space[1].split(':')[0],
                "pw": split_space[2]
            }
            num_list.append(d)

    return num_list


def problem_1(num_list):
    valid_pass = 0
    
    for entry in num_list:
        letter_count = entry["pw"].count(entry["letter"])
        if letter_count >= entry["lower"] and letter_count <= entry['upper']:
            valid_pass += 1
    print(valid_pass)
    return valid_pass


def problem_2(num_list):
    valid_pass = 0
    
    for entry in num_list:
        first = entry['pw'][entry["lower"]-1]
        second = entry['pw'][entry["upper"]-1]

        if (first == entry['letter']) != (second == entry['letter']):
            valid_pass += 1

    print(valid_pass)
    return valid_pass



if __name__ == "__main__":
    ap = argparse.ArgumentParser("Taking in numbers to add to 2020")
    ap.add_argument('input_file', help="txt file containig a bunch of numbers")
    
    args = ap.parse_args()

    num_list = parse_input(args.input_file)
    problem_1(num_list)
    problem_2(num_list)