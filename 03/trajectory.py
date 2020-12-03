from typing import List


def tree(input: str) -> bool:
    return input == "#"


sum: int = 0
for i in range(len(lines)):
    if tree(lines[i][(3 * i) % len(lines[i])]):
        sum +=1

lines: List[str] = [line.rstrip() for line in open('input.txt')]
print(sum)
