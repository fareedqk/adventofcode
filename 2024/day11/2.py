from collections import Counter

def evolve_stones_optimized(initial_stones, blinks):
    # Use a Counter to track the number of each type of stone
    stone_counts = Counter(initial_stones)
    
    for _ in range(blinks):
        next_stone_counts = Counter()
        for stone, count in stone_counts.items():
            if stone == 0:
                next_stone_counts[1] += count  # 0 becomes 1
            elif len(str(stone)) % 2 == 0:  # Even number of digits
                mid = len(str(stone)) // 2
                left = int(str(stone)[:mid])
                right = int(str(stone)[mid:])
                next_stone_counts[left] += count
                next_stone_counts[right] += count
            else:
                next_stone_counts[stone * 2024] += count  # Multiply by 2024
        stone_counts = next_stone_counts  # Update stone counts for the next blink
    
    # Return the total number of stones
    return sum(stone_counts.values())

def read_stones_from_file(file_path):
    with open(file_path, 'r') as file:
        # Read all lines and convert to a list of integers
        stones = list(map(int, file.read().strip().split()))
    return stones

# File path to the input file
file_path = 'day11/input.txt'

# Read the initial stones from the file
initial_stones = read_stones_from_file(file_path)

# Number of blinks for part two
blinks = 75

# Calculate the number of stones after 75 blinks
result = evolve_stones_optimized(initial_stones, blinks)
print(f"Number of stones after {blinks} blinks: {result}")
