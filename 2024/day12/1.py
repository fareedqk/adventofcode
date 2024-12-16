from typing import List, Dict, Set, Tuple

def find_regions(grid: List[List[str]]) -> Dict[str, List[Dict]]:
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    regions = {}

    def get_neighbors(r: int, c: int) -> List[Tuple[int, int]]:
        return [
            (r+1, c), (r-1, c), 
            (r, c+1), (r, c-1)
        ]

    def is_valid(r: int, c: int) -> bool:
        return 0 <= r < rows and 0 <= c < cols

    def count_sides(region_plots: Set[Tuple[int, int]]) -> int:
        sides = 0
        for r, c in region_plots:
            for nr, nc in get_neighbors(r, c):
                if not is_valid(nr, nc) or (nr, nc) not in region_plots:
                    sides += 1
        return sides

    def flood_fill(r: int, c: int, plant_type: str) -> Set[Tuple[int, int]]:
        if not is_valid(r, c) or visited[r][c] or grid[r][c] != plant_type:
            return set()

        region = {(r, c)}
        visited[r][c] = True

        for nr, nc in get_neighbors(r, c):
            if is_valid(nr, nc) and grid[nr][nc] == plant_type and not visited[nr][nc]:
                sub_region = flood_fill(nr, nc, plant_type)
                region.update(sub_region)

        return region

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                plant_type = grid[r][c]
                region_plots = flood_fill(r, c, plant_type)
                
                if region_plots:
                    sides = count_sides(region_plots)
                    
                    if plant_type not in regions:
                        regions[plant_type] = []
                    
                    regions[plant_type].append({
                        'area': len(region_plots),
                        'sides': sides
                    })

    return regions

def calculate_total_fence_price(regions: Dict[str, List[Dict]]) -> int:
    total_price = 0
    for plant_type, plant_regions in regions.items():
        for region in plant_regions:
            total_price += region['area'] * region['sides']
    return total_price

def solve(filename: str) -> int:
    with open(filename, 'r') as f:
        grid = [list(line.strip()) for line in f]
    
    regions = find_regions(grid)
    
    for plant_type, plant_regions in regions.items():
        print(f"Plant Type {plant_type}:")
        for region in plant_regions:
            print(f"  Area: {region['area']}, Sides: {region['sides']}, Price: {region['area'] * region['sides']}")
    
    return calculate_total_fence_price(regions)

# Solve the problem
print("Total Fence Price:", solve('day12/input.txt'))