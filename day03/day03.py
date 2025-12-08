def part1():
    total = 0
    with open("input03.txt") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            best = 0
            n = len(line)
            for i in range(n):
                for j in range(i + 1, n):
                    value = int(line[i]) * 10 + int(line[j])
                    if value > best:
                        best = value

            total += best
    return total


def max_joltage(line, k):
    digits = [int(c) for c in line]
    drop = len(digits) - k
    stack = []
    for d in digits:
        while drop > 0 and stack and stack[-1] < d:
            stack.pop()
            drop -= 1
        stack.append(d)
    stack = stack[:k]
    return int("".join(str(d) for d in stack))


def part2():
    total = 0
    k = 12
    with open("input03.txt") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            total += max_joltage(line, k)
    return total


if __name__ == "__main__":
    print("Day 3 Part 1:", part1())
    print("Day 3 Part 2:", part2())
