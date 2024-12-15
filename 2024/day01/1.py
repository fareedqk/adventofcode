import pandas as pd

def total_distance_sorted(file_path):
    df = pd.read_csv(file_path, delim_whitespace=True, header=None, names=["left", "right"])

    left = sorted(df['left'])
    right = sorted(df['right'])

    distance = sum(abs(l - r) for l, r in zip(left, right))
    return distance

file_path = "2024/day01/input.txt"

try:
    distance = total_distance_sorted(file_path)
    print(f"The total distance between the lists is: {distance}")
except Exception as e:
    print(f"An error occurred: {e}")