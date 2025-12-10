import sys


def neighbors(i, j, rows, cols):
    ns = []
    if i > 0:
        ns.append((i - 1, j))
    if j > 0:
        ns.append((i, j - 1))
    if i < rows - 1:
        ns.append((i + 1, j))
    if j < cols - 1:
        ns.append((i, j + 1))
    if i > 0 and j > 0:
        ns.append((i - 1, j - 1))
    if i < rows - 1 and j > 0:
        ns.append((i + 1, j - 1))
    if i < rows - 1 and j < cols - 1:
        ns.append((i + 1, j + 1))
    if i > 0 and j < cols - 1:
        ns.append((i - 1, j + 1))
    return ns


def part1(input: str):
    grid = [[1 if c == "@" else 0 for c in line] for line in input.splitlines()]
    rows, cols = len(grid), len(grid[0])
    accessible_count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                continue
            ns = neighbors(i, j, rows, cols)
            total = sum(grid[ni][nj] for ni, nj in ns)
            if total < 4:
                accessible_count += 1
    return accessible_count


def part2(input: str):
    grid = [[1 if c == "@" else 0 for c in line] for line in input.splitlines()]
    accessible_count = 0
    while True:
        rows, cols = len(grid), len(grid[0])
        remove = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    continue
                ns = neighbors(i, j, rows, cols)
                total = sum(grid[ni][nj] for ni, nj in ns)
                if total < 4:
                    accessible_count += 1
                    remove.append((i, j))
        if len(remove) == 0:
            break
        for i, j in remove:
            grid[i][j] = 0
    return accessible_count


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
