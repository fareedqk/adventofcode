from itertools import combinations
from rich import print

def read_connections(filename):
    with open(filename) as f:
        connections = f.read().strip().split()
    return connections

def build_graph(connections):
    graph = {}
    for connection in connections:
        a, b = connection.split('-')
        if a not in graph:
            graph[a] = set()
        if b not in graph:
            graph[b] = set()
        graph[a].add(b)
        graph[b].add(a)
    return graph

def find_connected_triples(graph):
    computers = list(graph.keys())
    triples = []
    
    for a, b, c in combinations(computers, 3):
        # check if each computer is connected to both others
        if (b in graph[a] and c in graph[a] and 
            a in graph[b] and c in graph[b] and
            a in graph[c] and b in graph[c]):
            triples.append(tuple(sorted([a, b, c])))
    
    return triples

def count_triples_with_t(triples):
    return sum(1 for triple in triples if any(comp.startswith('t') for comp in triple))

def solve_lan_party(filename):
    connections = read_connections(filename)
    
    graph = build_graph(connections)
    
    triples = find_connected_triples(graph)
    
    result = count_triples_with_t(triples)
    
    return result

result = solve_lan_party('2024/day23/input.txt')
print(f"Number of triples containing a computer starting with 't': {result}")