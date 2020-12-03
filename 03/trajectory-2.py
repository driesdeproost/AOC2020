import math
from typing import List


def tree(input: str) -> bool:
    return input == "#"


def treeCount(yShift: int, xShift: int) -> bool:
    sum: int = 0
    for i in range(math.ceil(len(lines) / xShift)):
        if (tree(lines[i*xShift][(i*yShift) % len(lines[0])])):
            sum += 1
    return sum

lines: List[str] = [line.rstrip() for line in open('input.txt')]
print(treeCount(1, 1) * treeCount(3, 1) * treeCount(5, 1) * treeCount(7, 1) * treeCount(1, 2))
