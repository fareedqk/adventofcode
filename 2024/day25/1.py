from rich import print

def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip().split('\n\n')

def parse_schematic(schematic):
    lines = schematic.split('\n')
    is_lock = lines[0][0] == '#'
    heights = []
    for col in range(len(lines[0])):
        height = 0
        if is_lock:
            for row in range(len(lines)):
                if lines[row][col] == '#':
                    height += 1
                else:
                    break
        else:
            for row in range(len(lines) - 1, -1, -1):
                if lines[row][col] == '#':
                    height += 1
                else:
                    break
        heights.append(height)
    return heights, is_lock

def count_compatible_pairs(schematics):
    locks = []
    keys = []
    for schematic in schematics:
        heights, is_lock = parse_schematic(schematic)
        if is_lock:
            locks.append(heights)
        else:
            keys.append(heights)
    
    total_rows = len(schematics[0].split('\n'))
    compatible_pairs = 0
    
    for lock in locks:
        for key in keys:
            if all(lock[col] + key[col] <= total_rows for col in range(len(lock))):
                compatible_pairs += 1
    
    return compatible_pairs

if __name__ == "__main__":
    schematics = read_input('2024/day25/input.txt')
    result = count_compatible_pairs(schematics)
    print(result)
