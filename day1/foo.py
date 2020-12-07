import argparse



def parse_input(input_file):
    num_list = []
    with open(input_file, 'r') as f:
        for line in f.readlines():
            num_list.append(int(line))
    return num_list


def do_work(num_list):
    num_list.sort()

    for x in range(len(num_list)):
        for y in range(x + 1, len(num_list)):
            for z in range(y + 1, len(num_list)):
                num1 = num_list[x]
                num2 = num_list[y]
                num3 = num_list[z]
                if num1 + num2 + num3 == 2020:
                    product = num1 * num2 * num3
                    print(product)
                    return  product


if __name__ == "__main__":
    ap = argparse.ArgumentParser("Taking in numbers to add to 2020")
    ap.add_argument('input_file', help="txt file containig a bunch of numbers")
    
    args = ap.parse_args()

    num_list = parse_input(args.input_file)
    do_work(num_list)