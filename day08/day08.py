from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple


@dataclass(frozen=True)
class Point3D:
    x: int
    y: int
    z: int


class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, a: int) -> int:
        while a != self.parent[a]:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a

    def union(self, a: int, b: int) -> bool:
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False

        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra

        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True

    def component_size(self, a: int) -> int:
        return self.size[self.find(a)]


def parse_input(text: str) -> List[Point3D]:
    points: List[Point3D] = []
    for line in text.strip().splitlines():
        x_str, y_str, z_str = line.strip().split(",")
        points.append(Point3D(int(x_str), int(y_str), int(z_str)))
    return points


def dist2(a: Point3D, b: Point3D) -> int:
    dx = a.x - b.x
    dy = a.y - b.y
    dz = a.z - b.z
    return dx * dx + dy * dy + dz * dz


def all_pairs_sorted(points: List[Point3D]) -> List[Tuple[int, int]]:
    n = len(points)
    pairs_with_d: List[Tuple[int, int, int]] = []
    for i in range(n):
        for j in range(i + 1, n):
            pairs_with_d.append((dist2(points[i], points[j]), i, j))
    pairs_with_d.sort(key=lambda t: t[0])
    return [(i, j) for _, i, j in pairs_with_d]


def part1(points: List[Point3D]) -> int:
    pairs = all_pairs_sorted(points)
    dsu = DSU(len(points))

    for i, j in pairs[:1000]:
        dsu.union(i, j)

    seen_roots = set()
    sizes: List[int] = []
    for idx in range(len(points)):
        r = dsu.find(idx)
        if r not in seen_roots:
            seen_roots.add(r)
            sizes.append(dsu.size[r])

    sizes.sort(reverse=True)
    return sizes[0] * sizes[1] * sizes[2]


def part2(points: List[Point3D]) -> int:
    pairs = all_pairs_sorted(points)
    dsu = DSU(len(points))

    last_i = -1
    last_j = -1

    for i, j in pairs:
        dsu.union(i, j)
        last_i, last_j = i, j
        if dsu.component_size(i) == len(points):
            break

    return points[last_i].x * points[last_j].x


def main() -> None:
    input_path = Path("input08.txt")
    text = input_path.read_text(encoding="utf-8")
    points = parse_input(text)

    ans1 = part1(points)
    ans2 = part2(points)

    print(f"Part 1: {ans1}")
    print(f"Part 2: {ans2}")


if __name__ == "__main__":
    main()
