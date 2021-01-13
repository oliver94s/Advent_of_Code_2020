import argparse
import copy
import math


"""
. = floor
L = empty seat
# = occupied seat

Rules:
Adjacent = any seat around including diagonal
Rules apply to all seats simultaniously 
if seat == L and left_seat != # and right_seat != #:
    seat = #
if seat == # and 4 or more seats adjacent to it are occupied:
    seat = L
"""


ADJACENT_COUNT = 5
FLOOR = "."


def parse_file(input_file):
    seats = []
    row = []
    with open(input_file, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            for spot in line:
                row.append(spot)
            seats.append(row)
            row = []
    
    for row in seats:
        row_str = ""
        for col in row:
            row_str += col + " "
        
        print(row_str)    
    
    return seats
 
OUT_OF_BOUNDS = "out of bounds"

def get_seat(seats, row, col):
    if row >= 0 and row < len(seats):
        if col >= 0 and col < len(seats[0]):
            return seats[row][col]
    return OUT_OF_BOUNDS
    
 
def change_seats(seats):
    new_seats = copy.deepcopy(seats)
    
    for row in range(len(seats)):
        for col in range(len(seats[row])):
            curr_seat = seats[row][col]
            seat_status = curr_seat
 
            left_spot = col - 1
            right_spot = col + 1
            up_spot = row - 1
            down_spot = row + 1
 
            left_seat = get_seat(seats, row, left_spot)
            right_seat = get_seat(seats, row, right_spot)
            up_seat = get_seat(seats, up_spot, col)
            down_seat = get_seat(seats, down_spot, col)
            up_left_seat = get_seat(seats, up_spot, left_spot)
            up_right_seat = get_seat(seats, up_spot, right_spot)
            down_left_seat = get_seat(seats, down_spot, left_spot)
            down_right_seat = get_seat(seats, down_spot, right_spot)
 
            if curr_seat == "L":
                adjacent = [left_seat, right_seat, up_seat, down_seat, up_left_seat, up_right_seat, down_left_seat, down_right_seat]
                taken_count = adjacent.count("#")
                if taken_count == 0:
                    seat_status = "#"
 
            if curr_seat == "#":
                adjacent = [left_seat, right_seat, up_seat, down_seat, up_left_seat, up_right_seat, down_left_seat, down_right_seat]
                taken_count = adjacent.count("#")
 
                if taken_count >= ADJACENT_COUNT:
                    seat_status = "L"
 
            new_seats[row][col] = seat_status
 
    if new_seats == seats:
        # things have stabilized
        return new_seats
 
    # print('')
    # for row in new_seats:
    #     row_str = ""
    #     for col in row:
    #         row_str += col + " "
        
    #     print(row_str)
    
    # return new_seats
    return change_seats(new_seats)
 
def problem_1(seats):
    count = 0
    round1 = change_seats(seats)
    for row in round1:
        count += row.count("#")
 
    print(count)
 

def down_left(seats, row, col):
    row += 1
    col -= 1
    seat = get_seat(seats, row, col)
    
    if seat != FLOOR:
        return seat
    else:
        return down_left(seats, row, col)
    
def down_right(seats, row, col):
    row += 1
    col += 1
    seat = get_seat(seats, row, col)
    
    if seat != FLOOR:
        return seat
    else:
        return down_right(seats, row, col)

def down(seats, row, col):
    row += 1
    seat = get_seat(seats, row, col)
    
    if seat != FLOOR:
        return seat
    else:
        return down(seats, row, col)

def up_left(seats, row, col):
    row -= 1
    col -= 1
    seat = get_seat(seats, row, col)
    
    if seat != FLOOR:
        return seat
    else:
        return up_left(seats, row, col)
    
def up_right(seats, row, col):
    row -= 1
    col += 1
    seat = get_seat(seats, row, col)
    
    if seat != FLOOR:
        return seat
    else:
        return up_right(seats, row, col)

def up(seats, row, col):
    row -= 1
    seat = get_seat(seats, row, col)
    
    if seat != FLOOR:
        return seat
    else:
        return up(seats, row, col)

def left(seats, row, col):
    col -= 1
    seat = get_seat(seats, row, col)
    if seat != FLOOR:
        return seat
    else:
        return left(seats, row, col)

def right(seats, row, col):
    col += 1
    seat = get_seat(seats, row, col)
    
    if seat != FLOOR:
        return seat
    else:
        return right(seats, row, col)

# represented with the number pad
DOWN_LEFT = 1
DOWN = 2
DOWN_RIGHT = 3
LEFT = 4
RIGHT = 6
UP_LEFT = 7
UP = 8
UP_RIGHT = 9


direction = {
    DOWN_LEFT : down_left,
    DOWN : down,
    DOWN_RIGHT : down_right,
    LEFT : left, 
    RIGHT : right,
    UP_LEFT : up_left,
    UP : up,
    UP_RIGHT : up_right
}


def look(seat, row, col, dir):
    return direction[dir](seat, row, col)


def change_seats_2(seats):
    new_seats = copy.deepcopy(seats)
    
    for row in range(len(seats)):
        for col in range(len(seats[row])):
            curr_seat = seats[row][col]
            seat_status = curr_seat

            left_seat = look(seats, row, col, LEFT)
            right_seat = look(seats, row, col, RIGHT)
            up_seat = look(seats, row, col, UP)
            down_seat = look(seats, row, col, DOWN)
            up_left_seat = look(seats, row, col, UP_LEFT)
            up_right_seat = look(seats, row, col, UP_RIGHT)
            down_left_seat = look(seats, row, col, DOWN_LEFT)
            down_right_seat = look(seats, row, col, DOWN_RIGHT)
            
            adjacent = [left_seat, right_seat, up_seat, down_seat, up_left_seat, up_right_seat, down_left_seat, down_right_seat]
            taken_count = adjacent.count("#")
            
            if curr_seat == "L":
                # if row == 0 and col == 2:
                #     print("row: %s\tcol: %s" % (row, col))
                #     print(adjacent)
                if taken_count == 0:
                    seat_status = "#"
 
            if curr_seat == "#":
                # if row == 0 and col == 2:
                #     print("row: %s\tcol: %s" % (row, col))
                #     print(adjacent)

                if taken_count >= ADJACENT_COUNT:
                    seat_status = "L"
 
            new_seats[row][col] = seat_status
         
    if new_seats == seats:
        # things have stabilized
        return new_seats
 
    # print('')
    # for row in new_seats:
    #     row_str = ""
    #     for col in row:
    #         row_str += col + " "
        
    #     print(row_str)
    
    # return new_seats
    return change_seats_2(new_seats)


def problem_2(seats):
    print('hello')
    count = 0
    round1 = change_seats_2(seats)
    # round2 = change_seats_2(round1)
    for row in round1:
        count += row.count("#")
 
    print(count)

    
if __name__ == "__main__":
    ap = argparse.ArgumentParser("Day 11")
 
    ap.add_argument("input_file", help='file to be read to answer question')
 
    args = ap.parse_args()
 
    seats = parse_file(args.input_file)
 
    # problem_1(seats)
    problem_2(seats)
 