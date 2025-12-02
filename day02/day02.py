def is_invalid_id(num: int) -> bool:
    s = str(num)
    if len(s) % 2 != 0:
        return False
    half = len(s) // 2
    return s[:half] == s[half:]


def main():
    total = 0

    with open("input02.txt", "r") as f:
        data = f.read().strip()

    ranges = data.split(",")

    for r in ranges:
        start, end = map(int, r.split("-"))

        for n in range(start, end + 1):
            if is_invalid_id(n):
                total += n

    print("Result (sum of invalid IDs):", total)


if __name__ == "__main__":
    main()
