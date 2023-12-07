"""
Author: github.com/MaxWarman
Advent of Code 2023 - Day 1
"""

DAY_NUM = 1

def get_input_lines(input_path):
    input_lines = []

    for line in open(input_path, "rt"):
        input_lines.append(line.replace("\n", ""))

    return input_lines

def find_first_and_last_digit_pt1(line):
    digits = [str(i) for i in range(1, 10)]
    first = ""
    last = ""
    for char in line:
        if char in digits:
            if first == "":
                first = char
            else:
                last = char
    return [first, last if last != "" else first]

def find_first_and_last_digit_pt2(line):
    digits = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    first = ""
    last = ""
    for i, char in enumerate(line):
        found_char = ""
        if char in digits.values():
            found_char = char
        else:
            digit_found = False
            for j in range(2,5):
                if digit_found:
                    break
                
                last_chars = line[i-j:i] + char
                for digit_txt in digits:
                    if len(digit_txt) != len(last_chars):
                        continue

                    if digit_txt in last_chars:
                        found_char = digits[digit_txt]
                        digit_found = True
                        break

        if found_char != "" and first == "":
            first = found_char
        elif found_char != "":
            last = found_char

    return [first, last if last != "" else first]

def solve_part_one(input_lines):
    solution_numbers = []
    for line in input_lines:
        digits = find_first_and_last_digit_pt1(line)
        solution_numbers.append(int("".join(digits)))

    solution = sum(solution_numbers)
    print(f"Day {DAY_NUM}, part 1 solution: {solution}")

def solve_part_two(input_lines):
    solution_numbers = []
    for line in input_lines:
        digits = find_first_and_last_digit_pt2(line)
        solution_numbers.append(int("".join(digits)))
    
    solution = sum(solution_numbers)
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