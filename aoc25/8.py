import sys
from copy import deepcopy
from math import prod

import numpy as np

sys.setrecursionlimit(1000000)

CONNECT_COUNT = 1000


def part1(input: str):
    points = []
    for line in input.splitlines():
        x, y, z = line.split(",")
        points.append([int(x), int(y), int(z)])
    points = np.array(points)
    # d(a,b) = forall i,j : ||a_i - b_j||
    distances = np.sqrt(
        np.sum((points[:, None, ...] - points[None, ...]) ** 2, axis=-1)
    )
    distances = np.tril(distances)
    distances[distances == 0] = float("inf")

    indices = np.argsort(distances, axis=None)
    rows, cols = np.unravel_index(indices, distances.shape)
    pairs = list(zip(rows, cols))

    circuits = set()

    # get top links
    adj_list: dict[np.int64, set[np.int64]] = {}
    count = 0
    for a, b in pairs:
        if count >= CONNECT_COUNT:
            if a not in adj_list:
                circuits.add((a,))
            if b not in adj_list:
                circuits.add((b,))
            continue
        if a not in adj_list:
            adj_list[a] = set()
        if b not in adj_list:
            adj_list[b] = set()
        if b in adj_list[a]:
            continue
        if a in adj_list[b]:
            continue
        count += 1
        adj_list[a].add(b)
        adj_list[b].add(a)

    def dfs(node, visited):
        if node in visited:
            return 0
        if node not in adj_list:
            return 1
        total = 1
        visited.add(node)
        for child in adj_list[node]:
            total += dfs(child, visited)
        return total

    visited = set()
    for k, v in adj_list.items():
        if k not in visited:
            visited_copy = deepcopy(visited)
            dfs(k, visited)
            diff = visited.difference(visited_copy)
            circuits.add(tuple(diff))

    circuits = list(sorted(list(circuits), key=lambda c: len(c), reverse=True))

    return prod(len(c) for c in circuits[:3])


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.components -= 1
        return True

    def __repr__(self):
        return f"parent={self.parent}, size={self.size}, components={self.components}"


def part2(input: str):
    points = []
    for line in input.splitlines():
        x, y, z = line.split(",")
        points.append([int(x), int(y), int(z)])
    points = np.array(points)
    # d(a,b) = forall i,j : ||a_i - b_j||
    distances = np.sqrt(
        np.sum((points[:, None, ...] - points[None, ...]) ** 2, axis=-1)
    )
    distances = np.tril(distances)
    distances[distances == 0] = float("inf")

    indices = np.argsort(distances, axis=None)
    rows, cols = np.unravel_index(indices, distances.shape)
    pairs = list(zip(rows, cols))

    n = len(points)
    dsu = DSU(n)
    for a, b in pairs:
        dsu.union(a, b)
        if dsu.components == 1:
            return points[a][0] * points[b][0]


def main():
    if len(sys.argv) < 2:
        print("error: need to give puzzle input")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        input = f.read()

    print("part1:", part1(input))
    print("part2:", part2(input))


if __name__ == "__main__":
    main()
