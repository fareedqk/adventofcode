import pandas as pd
from collections import Counter

def similarity_score(file_path):
    df = pd.read_csv(file_path, delim_whitespace=True, header=None, names=["left", "right"])

    left = df['left']
    right = df['right']

    right_counts = Counter(right)

    score = sum(num * right_counts[num] for num in left)
    return score

file_path = "2024/day01/input.txt"

try:
    score = similarity_score(file_path)
    print(f"The similarity score between the lists is: {score}")
except Exception as e:
    print(f"An error occurred: {e}")