def main():
    count_zero = 0
    position = 50

    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0]
            value = int(line[1:])

            if direction == "R":
                position = (position + value) % 100
            else:
                position = (position - value) % 100

            if position == 0:
                count_zero += 1

    print("Password:", count_zero)


if __name__ == "__main__":
    main()


