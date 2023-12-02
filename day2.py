"""
Author: github.com/MaxWarman
Advent of Code 2023 - Day 2
"""

DAY_NUM = 2

def get_input_lines(input_path):
    input_lines = []
    for line in  open(input_path, "rt"):
        input_lines.append(line.replace("\n", ""))
    return input_lines

def is_game_possible(line):
    max_possible = {"red":12, "green":13, "blue":14}
    fewest_cubes = {"red":0, "green":0, "blue":0}
    rounds = line.split(": ")[1].split(";")
    possible = True
    for round in rounds:
        round = round.strip().split(", ")
        for picked in round:
            picked = picked.split(" ")
            picked[0] = int(picked[0])
            if picked[0] > max_possible[picked[1]] and possible:
                possible = False
            if picked[0] > fewest_cubes[picked[1]]:
                fewest_cubes[picked[1]] = picked[0]        
    mul = 1
    for val in fewest_cubes.values():
        mul *= val
    return (possible, mul)

def solvePartOne(input_lines):
    sum_of_possible = 0
    game_id = 0
    for line in input_lines:
        game_id += 1
        if is_game_possible(line)[0]:
            sum_of_possible += game_id
    
    solution = sum_of_possible
    print(f"Day {DAY_NUM}, part 1 solution: {solution}")

def solvePartTwo(input_lines):
    sum_of_multiples = 0
    for line in input_lines:
        multiple = is_game_possible(line)[1]
        sum_of_multiples += multiple
    
    solution = sum_of_multiples
    print(f"Day {DAY_NUM}, part 2 solution: {solution}")

def main():
    test = False

    if test:
        input_path = f"input/test_input.txt"
    else:
        input_path = f"input/day{DAY_NUM}_input.txt"

    input_lines = get_input_lines(input_path)

    solvePartOne(input_lines)
    solvePartTwo(input_lines) 


if __name__ == "__main__":
    main()