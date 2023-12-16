"""
Author: github.com/MaxWarman
Advent of Code 2023 - Day 5
"""

DAY_NUM = 5
test = False

class Map:
    def __init__(self):
        self.map = []
    
    def update(self, arr):
        self.map.append(tuple(arr))


def find_mapping(s, m):
    for mapping in m.map:
        if s >= mapping[1] and s <= mapping[1] + mapping[2]:
            return mapping[0] + (s - mapping[1])
    return s

def parse_input(input_lines):
    seeds = [int(seed) for seed in input_lines[0].replace("seeds: ", "").split(" ")]

    maps = []
    is_map = False
    
    for line in input_lines[2:]:
        if "map" in line:
            is_map = True
            maps.append(Map())
            continue
        if "" == line:
            is_map = False
            continue
        
        if is_map:
            maps[-1].update([int(value) for value in line.split(" ")])

    return seeds, maps

def get_input_lines(input_path):
    input_lines = []
    for line in  open(input_path, "rt"):
        input_lines.append(line.replace("\n", ""))
    return input_lines

def solve_part_one(input_lines):
    seeds, maps = parse_input(input_lines)
    
    locations = []

    for seed in seeds:
        s = seed
        for map in maps:
            s = find_mapping(s, map)
        locations.append(s)
    
    solution = min(locations)
    print(f"Day {DAY_NUM}, part 1 solution: {solution}")

def solve_part_two(input_lines):
    seeds_tmp, maps = parse_input(input_lines)
    
    seeds = []
    for i in range(0, len(seeds_tmp), 2):
        seeds.append(tuple([seeds_tmp[i], seeds_tmp[i+1]]))

    locations = []

    for seed_range in seeds:
        for i in range(seed_range[1]):
            s = seed_range[0] + i
            for map in maps:
                s = find_mapping(s, map)
            locations.append(s)
    
    solution = min(locations)
    print(f"Day {DAY_NUM}, part 2 solution: {solution}")

def main():

    if test:
        input_path = f"input/test_input.txt"
    else:
        input_path = f"input/day{DAY_NUM}_input.txt"

    input_lines = get_input_lines(input_path)

    solve_part_one(input_lines)
    solve_part_two(input_lines) 


if __name__ == "__main__":
    main()