import argparse
import copy
import math


    
if __name__ == "__main__":
    ap = argparse.ArgumentParser("Day 12")
 
    ap.add_argument("input_file", help='file to be read to answer question')
 
    args = ap.parse_args()
 
    seats = parse_file(args.input_file)
 
    problem_1(seats)
    # problem_2(seats)
 