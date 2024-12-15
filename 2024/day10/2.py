from functools import lru_cache

def calculate_trailhead_ratings(topographic_map):
    rows = len(topographic_map)
    cols = len(topographic_map[0])
    
    @lru_cache(None)  # Memoize the result of the recursive function
    def count_paths(x, y):
        if topographic_map[x][y] == 9:  # Base case: reached a peak
            return 1
        
        paths = 0
        # Explore neighbors
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:  # Inside the map
                if topographic_map[nx][ny] == topographic_map[x][y] + 1:  # Valid path
                    paths += count_paths(nx, ny)
        
        return paths

    total_rating = 0
    
    # Identify all trailheads and calculate their ratings
    for i in range(rows):
        for j in range(cols):
            if topographic_map[i][j] == 0:  # It's a trailhead
                total_rating += count_paths(i, j)
    
    return total_rating

def read_map_from_file(file_path):
    with open(file_path, 'r') as file:
        # Convert each line of the file to a list of integers
        topographic_map = [list(map(int, line.strip())) for line in file]
    return topographic_map

# File path to the input file
file_path = '2024/day10/input.txt'

# Read the map from the file and calculate the ratings
topographic_map = read_map_from_file(file_path)
print(calculate_trailhead_ratings(topographic_map))
