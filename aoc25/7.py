import sys
from functools import lru_cache


def part1(input: str):
    grid = [[c for c in line] for line in input.splitlines()]
    split_count = 0

    def search(i, j):
        nonlocal grid, split_count
        if i == len(grid):
            return

        if grid[i][j] == "^":
            split_count += 1
            if j > 0:
                search(i, j - 1)  # left
            if j < len(grid[0]) - 1:
                search(i, j + 1)  # right
        elif grid[i][j] == "|":
            return
        else:
            grid[i][j] = "|"
            search(i + 1, j)

    start = (0, grid[0].index("S"))
    search(*start)

    return split_count


def part2(input: str):
    grid = [[c for c in line] for line in input.splitlines()]

    @lru_cache(maxsize=None)
    def search(i, j):
        nonlocal grid
        if i == len(grid):
            return 0
        if grid[i][j] == "^":
            total = 1
            if j > 0:
                total += search(i, j - 1)  # left
            if j < len(grid[0]) - 1:
                total += search(i, j + 1)  # right
            return total
        grid[i][j] = "|"
        return search(i + 1, j)

    start = (0, grid[0].index("S"))
    split_count = search(*start) + 1
    # for row in grid:
    #     print(row)

    return split_count


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
