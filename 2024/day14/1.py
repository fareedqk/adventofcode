def parse_input(file_path):
    """Parses the input file to extract robot positions and velocities."""
    robots = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            p = tuple(map(int, parts[0][2:].split(',')))  # Extract position
            v = tuple(map(int, parts[1][2:].split(',')))  # Extract velocity
            robots.append((p, v))
    return robots

def simulate_robots(robots, width, height, seconds):
    """Simulates the motion of robots over time in a wrapping grid."""
    grid = [[0] * width for _ in range(height)]

    for (p, v) in robots:
        # Compute final position after `seconds`, handling negative wrapping
        x = ((p[0] + v[0] * seconds) % width + width) % width
        y = ((p[1] + v[1] * seconds) % height + height) % height
        grid[y][x] += 1  # Increment the robot count at this position

    return grid

def count_quadrants(grid):
    """Counts the number of robots in each quadrant of the grid."""
    height, width = len(grid), len(grid[0])
    mid_y, mid_x = height // 2, width // 2

    quadrants = [0, 0, 0, 0]  # Top-left, Top-right, Bottom-left, Bottom-right

    for y in range(height):
        for x in range(width):
            count = grid[y][x]
            if count > 0:
                # Exclude robots on middle lines
                if y == mid_y or x == mid_x:
                    continue
                if y < mid_y and x < mid_x:
                    quadrants[0] += count  # Top-left
                elif y < mid_y and x >= mid_x:
                    quadrants[1] += count  # Top-right
                elif y >= mid_y and x < mid_x:
                    quadrants[2] += count  # Bottom-left
                elif y >= mid_y and x >= mid_x:
                    quadrants[3] += count  # Bottom-right

    return quadrants

def compute_safety_factor(quadrants):
    """Computes the safety factor by multiplying the counts in all four quadrants."""
    factor = 1
    for count in quadrants:
        factor *= count
    return factor

# Example usage
if __name__ == "__main__":
    input_file = "day14/input.txt"  # Replace with your input file path
    width, height = 101, 103  # Grid dimensions
    seconds = 100  # Time to simulate

    # Parse input
    robots = parse_input(input_file)

    # Simulate robot motion
    grid = simulate_robots(robots, width, height, seconds)

    # Count robots in quadrants
    quadrants = count_quadrants(grid)

    # Compute safety factor
    safety_factor = compute_safety_factor(quadrants)

    print(f"Quadrants: {quadrants}")
    print(f"Safety Factor: {safety_factor}")
