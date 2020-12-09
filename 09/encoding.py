import copy
from typing import List

def check(toCheck: List[int], start: int = 25):
    for x in range(start, len(toCheck)):
        print(toCheck[x - start:x])
        result: List[int] = two_elements_summing_to(sorted(toCheck[x-start:x]),toCheck[x])
        if (len(result) == 0):
            return toCheck[x]

def two_elements_summing_to(sorted_list : List[int], total: int) -> List[int]:
    print(sorted_list)
    index_low: int = 0
    index_high: int = len(sorted_list) - 1

    for x in range(index_high):
        low: int = sorted_list[index_low]
        high: int = sorted_list[index_high]
        add: int = low + high
        if add == total:
            return [low, high]
        if add > total:
            index_high -= 1
        else:
            index_low += 1
    return []

strings: List[str] = open('input.txt', 'r').readlines()
ints: List[int] = [int(x) for x in strings]
print(check(ints))
