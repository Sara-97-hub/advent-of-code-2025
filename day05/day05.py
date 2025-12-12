def read_database(ingredient_file):
    lines = []
    with open(ingredient_file, "r") as f:
        for line in f:
            lines.append(line.strip())

    blank_index = lines.index("")

    range_lines = lines[:blank_index]
    ingredient_lines = lines[blank_index + 1:]

    ranges = []
    for line in range_lines:
        start_str, end_str = line.split("-")
        start = int(start_str)
        end = int(end_str)
        ranges.append((start, end))

    ingredient_ids = []
    for line in ingredient_lines:
        if line != "":
            ingredient_ids.append(int(line))

    return ranges, ingredient_ids


def part1():
    ranges, ingredient_ids = read_database("input05.txt")

    fresh_count = 0

    for ingredient_id in ingredient_ids:
        is_fresh = False

        for start, end in ranges:
            if start <= ingredient_id <= end:
                is_fresh = True
                break

        if is_fresh:
            fresh_count += 1

    return fresh_count


def part2():
    ranges, _ = read_database("input05.txt")

    ranges.sort()

    merged = []
    for start, end in ranges:
        if not merged:
            merged.append([start, end])
        else:
            last_start = merged[-1][0]
            last_end = merged[-1][1]

            if start <= last_end:
                if end > last_end:
                    merged[-1][1] = end
            else:
                merged.append([start, end])

    total_fresh_ids = 0
    for start, end in merged:
        total_fresh_ids += (end - start + 1)

    return total_fresh_ids


if __name__ == "__main__":
    print("Day 5 Part 1:", part1())
    print("Day 5 Part 2:", part2())
