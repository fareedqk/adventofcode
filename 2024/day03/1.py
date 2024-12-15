import re

def extract_and_sum_multiplications_from_file(file_path):
    pattern = r"mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)"
    
    total = 0

    try:
        with open(file_path, 'r') as file:
            for line in file:
                matches = re.findall(pattern, line)
                for x, y in matches:
                    total += int(x) * int(y)

    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return total

input_file = "2024/day03/input.txt"

result = extract_and_sum_multiplications_from_file(input_file)

print(f"The sum of all valid multiplications is: {result}")
