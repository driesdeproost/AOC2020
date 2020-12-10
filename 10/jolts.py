from typing import List

strings: List[str] = open('input.txt', 'r').readlines()
ints: List[int] = sorted([int(x) for x in strings])
diffs: List[int] = [ints[x+1] - ints[x] for x in range(len(ints)-1)]
diffs = [ints[0]] + diffs + [3]
print(diffs.count(1)*(diffs.count(3)))