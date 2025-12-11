import sys


def part1(input: str):
    points = []
    for line in input.splitlines():
        i, j = line.split(",")
        points.append((int(i), int(j)))
    max_area = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            a, b = points[i], points[j]
            area = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
            max_area = max(max_area, area)
    return max_area


def part2(input: str):
    points = []
    for line in input.splitlines():
        i, j = line.split(",")
        points.append((int(i), int(j)))

    def search_corner(i, j, corner):
        for point in points:
            # exactly on corner
            if point == (i, j):
                return True

            match corner:
                case "UL":
                    # i,j-k || i-k,j
                    if point[0] == i and point[1] < j or point[0] < i and point[1] == j:
                        return True
                case "UR":
                    # i-k,j || i,j+k
                    if point[0] < i and point[1] == j or point[0] == i and point[1] > j:
                        return True
                case "LL":
                    # i,j-k || i+k,j
                    if point[0] == i and point[1] < j or point[0] > i and point[1] == j:
                        return True
                case "LR":
                    # i,j+k || i+k,j
                    if point[0] == i and point[1] > j or point[0] > i and point[1] == j:
                        return True

        return False

    max_area = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            a, b = points[i], points[j]

            if a[0] > b[0] and a[1] < b[1]:
                # lower left, upper right
                if not search_corner(b[0], a[1], "UL") or not search_corner(
                    a[0], b[1], "LR"
                ):
                    continue
            elif a[0] < b[0] and a[1] < b[1]:
                # upper left, lower right
                if not search_corner(b[0], a[1], "LL") or not search_corner(
                    a[0], b[1], "UR"
                ):
                    continue
            elif a[0] < b[0] and a[1] > b[1]:
                # upper right, lower left
                if not search_corner(a[0], b[1], "UL") or not search_corner(
                    b[0], a[1], "LR"
                ):
                    continue
            elif a[0] > b[0] and a[1] > b[1]:
                # lower right, upper left
                if not search_corner(a[0], b[1], "LL") or not search_corner(
                    b[0], a[1], "UR"
                ):
                    continue

            area = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
            max_area = max(max_area, area)

    return max_area


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
