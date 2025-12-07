def count_rolls(grid, r, c):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for rr in range(r - 1, r + 2):
        for cc in range(c - 1, c + 2):

            if rr == r and cc == c:
                continue

            if rr < 0 or rr >= rows or cc < 0 or cc >= cols:
                continue

            if grid[rr][cc] == '@':
                count += 1
    
    return count


grid = []
for line in open('input05.txt'):
    grid.append(list(line.strip()))

total_rolls = 0

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == '@':
            if count_rolls(grid, r, c) < 4:
                total_rolls += 1

print(total_rolls)
