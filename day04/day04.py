k = 12

def max_joltage(line, k):
    line = line.strip()
    digits = [int(c) for c in line]
    drop = len(digits) - k
    stack = []

    for d in digits:
        while drop > 0 and stack and stack[-1] < d:
            stack.pop()
            drop -= 1
        stack.append(d)

    stack = stack[:k]
    result = int("".join(str(d) for d in stack))
    return result

total = 0

with open("input04.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        total += max_joltage(line, k)

print(total)

