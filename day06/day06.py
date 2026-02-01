from math import prod


def read_grid(filename):
    with open(filename, "r") as f:
        lines = [line.rstrip("\n") for line in f]

    max_width = 0
    for line in lines:
        if len(line) > max_width:
            max_width = len(line)

    grid = []
    for line in lines:
        grid.append(line.ljust(max_width, " "))

    height = len(grid)

    segments = []

    col = 0
    while col < max_width:
        is_empty = True
        for row in range(height):
            if grid[row][col] != " ":
                is_empty = False
                break

        if is_empty:
            col += 1
            continue

        start = col

        while col < max_width:
            is_empty = True
            for row in range(height):
                if grid[row][col] != " ":
                    is_empty = False
                    break
            if is_empty:
                break
            col += 1

        end = col - 1
        segments.append((start, end))

    return grid, segments


def part1():
    grid, segments = read_grid("input06.txt")
    height = len(grid)

    total = 0

    for left, right in segments:
        operator = "*"
        for i in range(left, right + 1):
            if grid[height - 1][i] == "+":
                operator = "+"
                break

        numbers = []

        for row in range(height - 1):
            text = grid[row][left:right + 1].strip()
            if text != "":
                numbers.append(int(text))

        if operator == "+":
            result = 0
            for n in numbers:
                result += n
        else:
            result = 1
            for n in numbers:
                result *= n

        total += result

    return total


def part2():
    grid, segments = read_grid("input06.txt")
    height = len(grid)

    total = 0

    for left, right in segments:
        operator = "*"
        for i in range(left, right + 1):
            if grid[height - 1][i] == "+":
                operator = "+"
                break

        numbers = []

        col = right
        while col >= left:
            digits = ""
            for row in range(height - 1):
                ch = grid[row][col]
                if ch.isdigit():
                    digits += ch

            if digits != "":
                numbers.append(int(digits))

            col -= 1

        if operator == "+":
            result = 0
            for n in numbers:
                result += n
        else:
            result = 1
            for n in numbers:
                result *= n

        total += result

    return total


if __name__ == "__main__":
    print("Day 6 Part 1:", part1())
    print("Day 6 Part 2:", part2())
