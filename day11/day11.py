from functools import lru_cache

with open("input11.txt") as f:
    lines = f.readlines()

def parse_graph(lines):
    graph = {}
    for line in lines:
        line = line.strip()
        if not line:
            continue
        device, outputs = line.split(": ")
        graph[device] = outputs.split()
    return graph

graph = parse_graph(lines)
graph_tuple = {k: tuple(v) for k, v in graph.items()}

@lru_cache(maxsize=None)
def counts_paths(current, target, must_visit, visited_must):
    if current in must_visit:
        visited_must = visited_must | frozenset([current])
    if current == target:
        return 1 if visited_must == must_visit else 0

    if current not in graph_tuple:
        return 0

    total = 0
    for next_device in graph_tuple[current]:
        total += counts_paths(next_device, target, must_visit, visited_must)

    return total

must = frozenset({"dac", "fft"})

print("Part 1:", counts_paths("you", "out", frozenset(), frozenset()))
print("Part 2:", counts_paths("svr", "out", must, frozenset()))