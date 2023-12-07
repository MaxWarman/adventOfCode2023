"""
Author: github.com/MaxWarman
Advent of Code 2023 - Day 3
"""
import math

DAY_NUM = 3

class Number:
    def __init__(self, num_txt, row, start_col):
        self.val = int(num_txt)
        self.coords = [(row, start_col + i) for i in range(len(num_txt))]
    
    def __str__(self):
        return f"{self.val}: {self.coords}"

class Character:
    def __init__(self, txt, row, col):
        self.coords = (row, col)
        self.val = txt
    def __str__(self):
        return f"{self.val}: {self.coords}"

def get_input_lines(input_path):
    input_lines = []
    for line in  open(input_path, "rt"):
        input_lines.append(line.replace("\n", ""))
    return input_lines

def get_numbers_and_chars(input_lines):
    numbers = []
    chars = []
    digits = [str(i) for i in range(10)]
    for row, line in enumerate(input_lines):
        is_numeric = False
        start_col = 0
        num = ""
        for col, char in enumerate(line):
            if char in digits:
                if is_numeric == False:
                    start_col = col
                is_numeric = True
                
            else:
                is_numeric = False
            
            if is_numeric:
                num += char
            
            if (is_numeric == False or col == len(line) - 1) and num != "":
                numbers.append(Number(num, row, start_col))
                num = ""

    for row, line in enumerate(input_lines):
        for col, char in enumerate(line):
            if char not in ["."] + digits:
                chars.append(Character(char, row, col))

    return numbers, chars

def is_number_adjecent(number, char):
    for num_coord in number.coords:
        if math.sqrt(pow(num_coord[0] - char.coords[0], 2) + pow(num_coord[1] - char.coords[1], 2)) < 2:
            return True
    return False

def solve_part_one(input_lines):
    numbers, chars = get_numbers_and_chars(input_lines)
    adjecent_numbers = []

    for char in chars:
        for number in numbers:
            if is_number_adjecent(number, char) and number not in adjecent_numbers:
                adjecent_numbers.append(number)

    solution = sum([number.val for number in adjecent_numbers])
    print(f"Day {DAY_NUM}, part 1 solution: {solution}")

def solve_part_two(input_lines):
    numbers, chars = get_numbers_and_chars(input_lines)
    adjecent_numbers = {}
    sum_of_gears = 0

    for char in chars:
        for number in numbers:
            if is_number_adjecent(number, char):
                if char not in adjecent_numbers:
                    adjecent_numbers[char] = [number]
                else:
                    adjecent_numbers[char].append(number)

    for k in adjecent_numbers:
        if len(adjecent_numbers[k]) == 2 and k.val == "*":
            sum_of_gears += adjecent_numbers[k][0].val * adjecent_numbers[k][1].val

    solution = sum_of_gears
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