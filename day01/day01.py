def main():
    count_zero_part1 = 0
    count_zero_part2 = 0
    position = 50

    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0]
            value = int(line[1:])

            for _ in range(value):
                if direction == "R":
                    position = (position + 1) % 100
                else:
                    position = (position - 1) % 100

                if position == 0:
                    count_zero_part2 += 1

            if position == 0:
                count_zero_part1 += 1

    print("Part 1 password:", count_zero_part1)
    print("Part 2 password:", count_zero_part2)


if __name__ == "__main__":
    main()
