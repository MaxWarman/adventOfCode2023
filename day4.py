"""
Author: github.com/MaxWarman
Advent of Code 2023 - Day 4
"""

DAY_NUM = 4

def get_input_lines(input_path):
    input_lines = []
    for line in  open(input_path, "rt"):
        input_lines.append(line.replace("\n", ""))
    return input_lines

def get_numbers(line):
    winning_txt, guessed_txt = line.split(":")[1].strip().split("|")
    winning = []
    guessed = []

    for val in winning_txt.split(" "):
        if val != '':
            winning.append(int(val))
    for val in guessed_txt.split(" "):
        if val != '':
            guessed.append(int(val))
    
    return winning, guessed

def solve_part_one(input_lines):
    score = 0
    for line in input_lines:
        winning, guessed = get_numbers(line)
        matched = 0
        for number in guessed:
            if number in winning:
                print(number)
                matched += 1
        if matched:
            score += 2 ** (matched - 1)
    solution = score
    print(f"Day {DAY_NUM}, part 1 solution: {solution}")

def solve_part_two(input_lines):
    d = {}
    for i in range(len(input_lines)):
        d[i+1] = 1

    for i, line in enumerate(input_lines):
        winning, guessed = get_numbers(line)
        matched = 0
        for number in guessed:
            if number in winning:
                matched += 1
        if matched:
            for j in range(matched):
                d[i+j+2] += d[i+1]

    cards = 0
    for k in d:
        cards += d[k]
    
    solution = cards
    print(f"Day {DAY_NUM}, part 2 solution: {solution}")

def main():
    test = True

    if test:
        input_path = f"input/test_input.txt"
    else:
        input_path = f"input/day{DAY_NUM}_input.txt"

    input_lines = get_input_lines(input_path)

    #solve_part_one(input_lines)
    solve_part_two(input_lines) 


if __name__ == "__main__":
    main()