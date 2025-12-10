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
    # do reverse cumulative max
    total = 0
    for line in input.splitlines():
        batteries = [int(c) for c in line]
        digits = []
        last_digit_index = -1

        for _ in range(12):
            max_batt, max_index = 0, 0
            for i in range(
                last_digit_index + 1,
                len(batteries) - (12 - len(digits)) + 1,
            ):
                if batteries[i] > max_batt:
                    max_batt = batteries[i]
                    max_index = i
            digits.append(max_batt)
            last_digit_index = max_index
        total += sum(10**i * d for d, i in zip(digits, range(len(digits) - 1, -1, -1)))
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
