def evolve_stones(initial_stones, blinks):
    stones = initial_stones[:]
    
    for _ in range(blinks):
        next_stones = []
        for stone in stones:
            if stone == 0:
                next_stones.append(1)
            elif len(str(stone)) % 2 == 0:  # Even number of digits
                mid = len(str(stone)) // 2
                left = int(str(stone)[:mid])
                right = int(str(stone)[mid:])
                next_stones.extend([left, right])
            else:
                next_stones.append(stone * 2024)
        stones = next_stones
    
    return len(stones)

def read_stones_from_file(file_path):
    with open(file_path, 'r') as file:
        # Read all lines and convert to a list of integers
        stones = list(map(int, file.read().strip().split()))
    return stones

# File path to the input file
file_path = 'day11/input.txt'

# Read the initial stones from the file
initial_stones = read_stones_from_file(file_path)

# Number of blinks
blinks = 25

# Calculate the number of stones after the given blinks
result = evolve_stones(initial_stones, blinks)
print(f"Number of stones after {blinks} blinks: {result}")
