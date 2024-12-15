from collections import deque

def calculate_trailhead_scores(topographic_map):
    # Parse the input map
    rows = len(topographic_map)
    cols = len(topographic_map[0])
    
    def bfs(trailhead):
        queue = deque([trailhead])
        visited = set([trailhead])
        reachable_nines = set()
        
        while queue:
            x, y = queue.popleft()
            
            # Check if it's a peak (height 9)
            if topographic_map[x][y] == 9:
                reachable_nines.add((x, y))
            
            # Explore neighbors
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:  # Inside the map
                    if (nx, ny) not in visited and topographic_map[nx][ny] == topographic_map[x][y] + 1:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
        
        return len(reachable_nines)
    
    total_score = 0
    
    # Identify all trailheads and calculate their scores
    for i in range(rows):
        for j in range(cols):
            if topographic_map[i][j] == 0:  # It's a trailhead
                total_score += bfs((i, j))
    
    return total_score

def read_map_from_file(file_path):
    with open(file_path, 'r') as file:
        # Convert each line of the file to a list of integers
        topographic_map = [list(map(int, line.strip())) for line in file]
    return topographic_map

# File path to the input file
file_path = '2024/day10/input.txt'

# Read the map from the file and calculate the scores
topographic_map = read_map_from_file(file_path)
print(calculate_trailhead_scores(topographic_map))
