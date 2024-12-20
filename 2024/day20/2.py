from typing import List, Tuple, Dict
import heapq

def read_input(filename: str) -> List[str]:
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]

def find_start_end(grid: List[str]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    start = end = None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'E':
                end = (i, j)
    return start, end

def get_neighbors(pos: Tuple[int, int], grid: List[str], cheating: bool = False) -> List[Tuple[int, int]]:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    neighbors = []
    for dy, dx in directions:
        new_y, new_x = pos[0] + dy, pos[1] + dx
        if (0 <= new_y < len(grid) and
            0 <= new_x < len(grid[0]) and
            (cheating or grid[new_y][new_x] != '#')):
            neighbors.append((new_y, new_x))
    return neighbors

def find_reachable_positions(grid: List[str], start: Tuple[int, int], max_steps: int) -> Dict[Tuple[int, int], int]:
    distances = {start: 0}
    queue = [(0, start)]

    while queue:
        dist, current = heapq.heappop(queue)

        if dist > max_steps:
            continue

        for next_pos in get_neighbors(current, grid, cheating=True):
            new_dist = dist + 1

            if new_dist <= max_steps and (next_pos not in distances or new_dist < distances[next_pos]):
                distances[next_pos] = new_dist
                heapq.heappush(queue, (new_dist, next_pos))

    return distances

def shortest_path(grid: List[str], start: Tuple[int, int], end: Tuple[int, int]) -> Dict[Tuple[int, int], int]:
    distances = {}
    queue = [(0, start)]
    distances[start] = 0

    while queue:
        dist, current = heapq.heappop(queue)

        if dist > distances[current]:
            continue

        for next_pos in get_neighbors(current, grid):
            new_dist = dist + 1

            if next_pos not in distances or new_dist < distances[next_pos]:
                distances[next_pos] = new_dist
                heapq.heappush(queue, (new_dist, next_pos))

    return distances

def find_cheats(grid: List[str], normal_distances: Dict[Tuple[int, int], int],
                start: Tuple[int, int], end: Tuple[int, int]) -> Dict[int, int]:
    MAX_CHEAT_LENGTH = 20
    savings = {}
    height, width = len(grid), len(grid[0])

    for y1 in range(height):
        for x1 in range(width):
            if grid[y1][x1] == '#':
                continue
            pos1 = (y1, x1)
            if pos1 not in normal_distances:
                continue

            reachable = find_reachable_positions(grid, pos1, MAX_CHEAT_LENGTH)

            for pos2, cheat_length in reachable.items():
                if grid[pos2[0]][pos2[1]] == '#':
                    continue

                if pos1 in normal_distances and pos2 in normal_distances:
                    normal_time = normal_distances[end]
                    cheat_time = (normal_distances[pos1] +
                                cheat_length +
                                (normal_distances[end] - normal_distances[pos2]))

                    if cheat_time < normal_time:
                        saved = normal_time - cheat_time
                        savings[saved] = savings.get(saved, 0) + 1

    return savings

def solve(grid: List[str]) -> int:
    start, end = find_start_end(grid)

    grid = [row.replace('S', '.').replace('E', '.') for row in grid]

    normal_distances = shortest_path(grid, start, end)

    savings = find_cheats(grid, normal_distances, start, end)

    return sum(count for saved, count in savings.items() if saved >= 100)

def main():
    grid = read_input('2024/day20/input.txt')
    result = solve(grid)
    print(f"Number of cheats saving at least 100 picoseconds: {result}")

if __name__ == "__main__":
    main()