from itertools import product

def evaluate_expression(nums, operators):
    result = nums[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += nums[i + 1]
        elif op == '*':
            result *= nums[i + 1]
        elif op == '||':
            result = int(str(result) + str(nums[i + 1]))
    return result

def solve_calibration_with_concat(filename):
    total = 0
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            target, numbers = line.split(':')
            target = int(target)
            nums = list(map(int, numbers.split()))
            
            num_operators = len(nums) - 1
            for operators in product(['+', '*', '||'], repeat=num_operators):
                if evaluate_expression(nums, operators) == target:
                    total += target
                    break  # Only add the target value once
    
    return total

filename = '2024/day07/input.txt'
result = solve_calibration_with_concat(filename)
print(f"The new total calibration result is: {result}")
