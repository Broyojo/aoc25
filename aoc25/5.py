import sys


def part1(input: str):
    ranges = []
    ranges_done = False
    fresh = 0
    for line in input.splitlines():
        if not ranges_done:
            if line == "":
                ranges_done = True
            else:
                ranges.append([int(n) for n in line.split("-")])
            continue

        id = int(line)
        for start, end in ranges:
            if start <= id <= end:
                fresh += 1
                break

    return fresh


def part2(input: str):
    ranges = []
    for line in input.splitlines():
        if line == "":
            break
        r = [int(n) for n in line.split("-")]
        ranges.append(r)

    ranges.sort(key=lambda r: r[0])

    fresh = ranges[0][1] - ranges[0][0] + 1
    last_end = ranges[0][1]
    for start, end in ranges[1:]:
        if last_end >= end:
            continue
        if last_end >= start:
            start = last_end + 1
        fresh += end - start + 1
        last_end = end

    return fresh


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
