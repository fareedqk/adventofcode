def find_x_mas_occurrences(grid):
    rows, cols = len(grid), len(grid[0])
    x_mas_count = 0
    
    def check_direction(r, c, dr, dc, word, backwards=False):
        if backwards:
            word = word[::-1]
        
        for i, letter in enumerate(word):
            curr_r, curr_c = r + i*dr, c + i*dc
            if (not (0 <= curr_r < rows and 0 <= curr_c < cols) or 
                grid[curr_r][curr_c] != letter):
                return False
        return True
    
    directions = [
        (1, 0),   # down
        (-1, 0),  # up
        (0, 1),   # right
        (0, -1),  # left
        (1, 1),   # down-right
        (1, -1),  # down-left
        (-1, 1),  # up-right
        (-1, -1)  # up-left
    ]
    
    for r in range(rows):
        for c in range(cols):
            for i, (dr1, dc1) in enumerate(directions):
                for j, (dr2, dc2) in enumerate(directions):
                    if i == j:
                        continue
                    
                    for back1 in [False, True]:
                        for back2 in [False, True]:
                            if check_direction(r, c, dr1, dc1, "MAS", back1):
                                if check_direction(r, c, dr2, dc2, "MAS", back2):
                                    x_mas_count += 1
    
    return x_mas_count // 2

with open('2024/day04/input.txt', 'r') as file:
    grid = [line.strip() for line in file]

occurrences = find_x_mas_occurrences(grid)
print(f"Total X-MAS occurrences: {occurrences}")