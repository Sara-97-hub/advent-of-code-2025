def is_invalid_id(num: int) -> bool:
    s = str(num)
    L = len(s)
    for size in range(1, L // 2 + 1):
        if L % size != 0:
            continue
        pattern = s[:size]
        repeats = L // size
        if repeats < 2:
            continue
        if pattern * repeats == s:
            return True
    return False


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
