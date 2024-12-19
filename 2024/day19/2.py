from functools import lru_cache
from rich import print

def parse_input(file_path):
    with open(file_path, 'r') as file:
        input_str = file.read()
    sections = input_str.strip().split("\n\n")
    towel_patterns = sections[0].split(", ")
    designs = sections[1].split("\n")
    return towel_patterns, designs

@lru_cache(None)
def count_ways_to_form_design(design, towel_patterns):
    if not design:
        return 1

    ways = 0
    for pattern in towel_patterns:
        if design.startswith(pattern):
            ways += count_ways_to_form_design(design[len(pattern):], towel_patterns)

    return ways

def total_ways_to_form_designs(towel_patterns, designs):
    total_ways = 0
    for design in designs:
        total_ways += count_ways_to_form_design(design, tuple(towel_patterns))
    return total_ways

file_path = "2024/day19/input.txt"
towel_patterns, designs = parse_input(file_path)
result = total_ways_to_form_designs(towel_patterns, designs)
print(f"Total number of ways to form all designs: {result}")
