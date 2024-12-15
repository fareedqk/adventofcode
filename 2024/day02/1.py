def is_safe_report(levels):
    differences = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]

    if not all(1 <= abs(diff) <= 3 for diff in differences):
        return False
    if all(diff > 0 for diff in differences) or all(diff < 0 for diff in differences):
        return True

    return False


def count_safe_reports(file_path):
    safe_count = 0

    with open(file_path, 'r') as file:
        for line in file:
            levels = list(map(int, line.strip().split()))
            
            if is_safe_report(levels):
                safe_count += 1

    return safe_count

file_path = "2024/day02/input.txt"

try:
    safe_reports = count_safe_reports(file_path)
    print(f"The number of safe reports is: {safe_reports}")
except Exception as e:
    print(f"An error occurred: {e}")