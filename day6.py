"""
Author: github.com/MaxWarman
Advent of Code 2023 - Day 6
"""
from math import sqrt, floor

DAY_NUM = 6

def get_input_lines(input_path):
    input_lines = []
    for line in  open(input_path, "rt"):
        input_lines.append(line.replace("\n", ""))
    return input_lines

def parse_input_str(input_lines):
    times = []
    for time in input_lines[0].split(":")[1].strip().split(" "):
        if time != "":
            times.append(time)
    dists = []
    for dist in input_lines[1].split(":")[1].strip().split(" "):
        if dist != "":
            dists.append(dist)

    return times, dists

def solve_part_one(input_lines):
    times, dists = parse_input_str(input_lines)
    times = [int(time) for time in times]
    dists = [int(dist) for dist in dists]

    possiblities = []
    for i, time in enumerate(times):
        curr_possiblities = 0
        dist = dists[i]
        delta = pow(time, 2) - 4 * dist
        x1 = (time - sqrt(delta)) / 2
        x2 = (time + sqrt(delta)) / 2
        curr_possiblities = floor(x2-x1) + 1
        possiblities.append(curr_possiblities)
    
    mul_of_possiblites = 1
    for val in possiblities:
        mul_of_possiblites *= val

    solution = mul_of_possiblites
    print(f"Day {DAY_NUM}, part 1 solution: {solution}")

def solve_part_two(input_lines):
    time, dist = parse_input_str(input_lines)
    time = int("".join(time))
    dist = int("".join(dist))
    
    possiblities = 0
    delta = pow(time, 2) - 4 * dist
    x1 = (time - sqrt(delta)) / 2
    x2 = (time + sqrt(delta)) / 2
    possiblities = floor(x2-x1) + 1

    solution = possiblities
    print(f"Day {DAY_NUM}, part 2 solution: {solution}")

def main():
    test = False

    if test:
        input_path = f"input/test_input.txt"
    else:
        input_path = f"input/day{DAY_NUM}_input.txt"

    input_lines = get_input_lines(input_path)

    solve_part_one(input_lines)
    solve_part_two(input_lines) 


if __name__ == "__main__":
    main()