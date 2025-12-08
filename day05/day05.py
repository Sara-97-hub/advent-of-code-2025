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


def main():
    ranges,ingredient_ids = read_database("input05.txt")

    fresh_count = 0

    for ingredient_id in ingredient_ids:
        is_fresh = False

        for start, end in ranges:
            if start <= ingredient_id <= end:
                is_fresh = True
                break

        if is_fresh:
            fresh_count += 1

    print(fresh_count)


if __name__ == "__main__":
    main()
