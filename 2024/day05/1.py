def parse_input(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]

    separator = next(i for i, line in enumerate(lines) if ',' in line)
    rules = [tuple(map(int, line.split('|'))) for line in lines[:separator]]
    updates = [list(map(int, line.split(','))) for line in lines[separator:]]

    return rules, updates


def is_update_valid(update, rules):
    index_map = {page: i for i, page in enumerate(update)}

    for X, Y in rules:
        if X in index_map and Y in index_map:
            if index_map[X] > index_map[Y]:
                return False

    return True


def find_middle_page(update):
    return update[len(update) // 2]


def sum_middle_pages_of_valid_updates(file_path):
    rules, updates = parse_input(file_path)

    total = 0
    for update in updates:
        if is_update_valid(update, rules):
            total += find_middle_page(update)

    return total


file_path = "2024/day05/input.txt"

result = sum_middle_pages_of_valid_updates(file_path)

print(f"The sum of middle pages from valid updates is: {result}")
