import string
from typing import List


def count(input: str) -> int:
    newlines: int = input.count("\n")
    return sum([input.count(char) == newlines +1 for char in string.ascii_lowercase])


groups: List[str] = open('input.txt', 'r').read().split('\n\n')
groups[-1] = groups[-1][:-1]  # strip last newline
print(sum([count(s) for s in groups]))
