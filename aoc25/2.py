import sys


def part1(input: str):
    def invalid(s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        return s[: len(s) // 2] == s[len(s) // 2 :]

    ranges = input.split(",")
    total = 0
    for r in ranges:
        start, end = r.split("-")
        for i in range(int(start), int(end) + 1):
            if invalid(str(i)):
                total += i
    return total


def part2(input: str):
    def invalid(s: str) -> bool:
        for window in range(1, len(s) // 2 + 1):
            if len(s) % window != 0:
                continue
            current = s[:window]
            for i in range(window, len(s) - window + 1, window):
                block = s[i : i + window]
                if block != current:
                    break
            else:
                return True  # all matched
        return False

    ranges = input.split(",")
    total = 0
    for r in ranges:
        start, end = r.split("-")
        for i in range(int(start), int(end) + 1):
            if invalid(str(i)):
                total += i
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
