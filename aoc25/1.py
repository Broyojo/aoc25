import sys


def part1(input: list[str]) -> int:
    dial = 50
    count = 0
    for line in input:
        dir = 1 if line[0] == "R" else -1
        num = int(line[1:])
        dial = (dial + dir * num) % 100
        if dial == 0:
            count += 1
    return count


def part2(input: list[str]) -> int:
    dial = 50
    count = 0
    for line in input:
        dir = 1 if line[0] == "R" else -1
        num = int(line[1:])
        for _ in range(num):
            dial = (dial + dir) % 100
            if dial == 0:
                count += 1
    return count


def main():
    if len(sys.argv) < 2:
        print("error: need to give puzzle input")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        input = f.readlines()

    print("part1:", part1(input))
    print("part2:", part2(input))


if __name__ == "__main__":
    main()
