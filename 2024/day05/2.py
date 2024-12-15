from collections import defaultdict, deque

def parse_input(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]

    # Split the file into rules and updates
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


def reorder_update(update, rules):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    pages_in_update = set(update)

    for X, Y in rules:
        if X in pages_in_update and Y in pages_in_update:
            graph[X].append(Y)
            in_degree[Y] += 1
            if X not in in_degree:
                in_degree[X] = 0

    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_update = []

    while queue:
        node = queue.popleft()
        sorted_update.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_update


def sum_middle_pages_of_corrected_updates(file_path):
    rules, updates = parse_input(file_path)

    total = 0
    for update in updates:
        if not is_update_valid(update, rules):
            corrected_update = reorder_update(update, rules)
            middle_page = corrected_update[len(corrected_update) // 2]
            total += middle_page

    return total


file_path = "2024/day05/input.txt"

result = sum_middle_pages_of_corrected_updates(file_path)

print(f"The sum of middle pages from corrected updates is: {result}")
