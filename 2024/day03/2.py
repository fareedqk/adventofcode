import re

def extract_and_sum_multiplications_from_file(file_path):
    mul_pattern = r"mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    
    with open(file_path, 'r') as file:
        content = file.read()
    
    tokens = re.split(r"(\bdo\(\)|\bdon't\(\)|mul\(\d{1,3},\d{1,3}\))", content)

    multiplications_enabled = True
    total = 0

    for token in tokens:
        token = token.strip()  # Remove whitespace
        if not token:
            continue
        
        if re.fullmatch(do_pattern, token):
            multiplications_enabled = True
        elif re.fullmatch(dont_pattern, token):
            multiplications_enabled = False
        elif multiplications_enabled:
            match = re.fullmatch(mul_pattern, token)
            if match:
                x, y = map(int, match.groups())
                total += x * y

    return total


input_file = "2024/day03/input.txt"

result = extract_and_sum_multiplications_from_file(input_file)

print(f"The sum of all enabled multiplications is: {result}")
