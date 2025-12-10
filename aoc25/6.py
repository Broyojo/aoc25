import sys


def part1(input: str):
    problems = []
    for line in input.splitlines():
        terms = line.split()
        if len(problems) == 0:
            for _ in range(len(terms)):
                problems.append([])
        for i in range(len(terms)):
            problems[i].append(terms[i])
    total = 0
    for problem in problems:
        total += eval(problem[-1].join(problem[:-1]))
    return total


def part2(input: str):
    grid = [[c for c in line] for line in input.splitlines()]
    rows, cols = len(grid), len(grid[0])
    problems = [[]]
    for j in range(cols - 1, -1, -1):
        current_num = ""
        for i in range(rows):
            if grid[i][j] in ["+", "*"]:
                problems[-1].append(current_num)
                problems[-1].append(grid[i][j])
                problems.append([])
                break
            else:
                current_num += grid[i][j]
        else:
            problems[-1].append(current_num)
    total = 0
    for problem in problems[:-1]:
        total += eval(
            problem[-1].join(filter(lambda t: len(t.strip()) > 0, problem[:-1]))
        )
    return total


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
