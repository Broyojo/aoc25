import sys


def part1(input: str):
    total = 0
    for line in input.splitlines():
        # max always must be first battery (unless it is the last one in the list)
        batteries = [int(c) for c in line]

        first_batt, first_index = 0, 0
        for i in range(len(batteries) - 1):
            if batteries[i] > first_batt:
                first_batt = batteries[i]
                first_index = i

        second_batt = 0
        for i in range(first_index + 1, len(batteries)):
            if batteries[i] > second_batt:
                second_batt = batteries[i]

        total += first_batt * 10 + second_batt

    return total


def part2(input: str):
    pass


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
