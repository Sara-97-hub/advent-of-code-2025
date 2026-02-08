import re
from itertools import product
import pulp

def parse_line_part1(line):
    pattern = re.search(r"\[(.*?)\]", line).group(1)
    target = [1 if c == "#" else 0 for c in pattern]
    buttons = []
    for b in re.findall(r"\((.*?)\)", line):
        if b:
            buttons.append(list(map(int, b.split(","))))
        else:
            buttons.append([])
    return target, buttons

def parse_line_part2(line):
    target = list(map(int, re.search(r"\{(.*?)\}", line).group(1).split(",")))
    buttons = []
    for b in re.findall(r"\((.*?)\)", line):
        if b:
            buttons.append(list(map(int, b.split(","))))
        else:
            buttons.append([])
    return target, buttons

def solve_machine_part1(target, buttons):
    num_lights = len(target)
    num_buttons = len(buttons)
    best = float("inf")
    for presses in product([0, 1], repeat=num_buttons):
        state = [0] * num_lights
        for press, button in zip(presses, buttons):
            if press == 1:
                for i in button:
                    state[i] ^= 1
        if state == target:
            best = min(best, sum(presses))
    return best

def solve_part1(lines):
    total = 0
    for line in lines:
        target, buttons = parse_line_part1(line)
        total += solve_machine_part1(target, buttons)
    return total

def solve_machine_part2(target, buttons):
    prob = pulp.LpProblem("machine", pulp.LpMinimize)
    x = [pulp.LpVariable(f"x{i}", lowBound=0, cat="Integer") for i in range(len(buttons))]
    prob += pulp.lpSum(x)
    for i in range(len(target)):
        prob += pulp.lpSum(x[j] for j, b in enumerate(buttons) if i in b) == target[i]
    prob.solve(pulp.PULP_CBC_CMD(msg=False))
    return int(pulp.value(prob.objective))

def solve_part2(lines):
    total = 0
    for line in lines:
        target, buttons = parse_line_part2(line)
        total += solve_machine_part2(target, buttons)
    return total

with open("input10.txt") as f:
    lines = [line.strip() for line in f if line.strip()]

print("Part 1:", solve_part1(lines))
print("Part 2:", solve_part2(lines))
