# Simple Traveling Salesman Problem using all routes

import itertools

def tsp(cities, distance):
    shortest_distance = float('inf')
    best_path = []
    for perm in itertools.permutations(cities):
        total = 0
        for i in range(len(perm) - 1):
            total += distance[perm[i]][perm[i+1]]
        total += distance[perm[-1]][perm[0]]  # return to start
        if total < shortest_distance:
            shortest_distance = total
            best_path = perm
    return best_path, shortest_distance

cities = ["A", "B", "C"]
dist = {
    "A": {"A":0,"B":10,"C":15},
    "B": {"A":10,"B":0,"C":20},
    "C": {"A":15,"B":20,"C":0}
}

path, total = tsp(cities, dist)
print("Best Path:", path)
print("Shortest Distance:", total)
