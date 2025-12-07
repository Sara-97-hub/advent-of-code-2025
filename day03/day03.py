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
                tens = int(line[i])
                ones = int(line[j])
                value = tens * 10 + ones
                if value > best:
                    best = value

        total += best

print(total)
