from collections import defaultdict
from itertools import combinations
from rich import print

def parse_input(file_path):
    graph = defaultdict(set)
    with open(file_path, "r") as file:
        for line in file:
            a, b = line.strip().split("-")
            graph[a].add(b)
            graph[b].add(a)
    return graph

def find_largest_clique(graph):
    nodes = list(graph.keys())
    largest_clique = []

    def is_clique(subset):
        for a, b in combinations(subset, 2):
            if b not in graph[a]:
                return False
        return True

    def backtrack(start, current_clique):
        nonlocal largest_clique
        if len(current_clique) > len(largest_clique):
            largest_clique = current_clique[:]

        for i in range(start, len(nodes)):
            next_node = nodes[i]
            if is_clique(current_clique + [next_node]):
                backtrack(i + 1, current_clique + [next_node])

    backtrack(0, [])
    return largest_clique

def main(file_path):
    graph = parse_input(file_path)
    largest_clique = find_largest_clique(graph)
    password = ",".join(sorted(largest_clique))
    print(f"LAN party password: {password}")

input_file = "2024/day23/input.txt"
main(input_file)
