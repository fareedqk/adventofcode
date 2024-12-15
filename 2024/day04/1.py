def count_word_occurrences_from_file(file_path, word):
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]

    rows = len(grid)
    cols = len(grid[0])
    word_length = len(word)
    directions = [
        (0, 1),   # Right
        (0, -1),  # Left
        (1, 0),   # Down
        (-1, 0),  # Up
        (1, 1),   # Diagonal Down-Right
        (1, -1),  # Diagonal Down-Left
        (-1, 1),  # Diagonal Up-Right
        (-1, -1)  # Diagonal Up-Left
    ]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def find_word_from(x, y, dx, dy):
        for i in range(word_length):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    count = 0
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if find_word_from(x, y, dx, dy):
                    count += 1

    return count


file_path = "2024/day04/input.txt"
word = "XMAS"

result = count_word_occurrences_from_file(file_path, word)

print(f"The word '{word}' occurs {result} times in the grid.")
