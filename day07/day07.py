from collections import defaultdict


def parse_grid(lines):
    height = len(lines)
    width = len(lines[0])

    splitters = set()
    start = None

    for y, row in enumerate(lines):
        for x, ch in enumerate(row):
            if ch == "S":
                start = (x, y)
            elif ch == "^":
                splitters.add((x, y))

    if start is None:
        raise ValueError("No start position found")

    return width, height, start, splitters


def part1(lines):
    width, height, (sx, sy), splitters = parse_grid(lines)

    beams = {sx}
    splits = 0

    for y in range(sy + 1, height):
        new_beams = set()

        for x in beams:
            if (x, y) in splitters:
                splits += 1
                if x - 1 >= 0:
                    new_beams.add(x - 1)
                if x + 1 < width:
                    new_beams.add(x + 1)
            else:
                new_beams.add(x)

        beams = new_beams

    return splits


def part2(lines):
    width, height, (sx, sy), splitters = parse_grid(lines)

    counts = {sx: 1}

    for y in range(sy + 1, height):
        new_counts = defaultdict(int)

        for x, ways in counts.items():
            if (x, y) in splitters:
                if x - 1 >= 0:
                    new_counts[x - 1] += ways
                if x + 1 < width:
                    new_counts[x + 1] += ways
            else:
                new_counts[x] += ways

        counts = new_counts

    return sum(counts.values())


def main():
    with open("input07.txt") as f:
        lines = [line.strip() for line in f if line.strip()]

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
