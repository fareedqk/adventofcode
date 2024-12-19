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
def can_form_design(design, towel_patterns):
    if not design:
        return True

    for pattern in towel_patterns:
        if design.startswith(pattern):
            if can_form_design(design[len(pattern):], towel_patterns):
                return True

    return False

def count_possible_designs(towel_patterns, designs):
    possible_count = 0
    for design in designs:
        if can_form_design(design, tuple(towel_patterns)):
            possible_count += 1
    return possible_count

file_path = "2024/day19/input.txt"
towel_patterns, designs = parse_input(file_path)
result = count_possible_designs(towel_patterns, designs)
print(f"Number of possible designs: {result}")
