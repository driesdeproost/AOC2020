import copy
from typing import List

min_amount_contiguous: int = 2

def check(toCheck: List[int], start: int = 25):
    for x in range(start, len(toCheck)):
        result: List[int] = two_elements_summing_to(sorted(toCheck[x-start:x]),toCheck[x])
        if (len(result) == 0):
            return toCheck[x]

def two_elements_summing_to(sorted_list : List[int], total: int) -> List[int]:
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

def grow(low: int, high: int) -> tuple:
    return (low, high + 1)

def shrink(low: int, high: int) -> tuple:
    if (high - low <= min_amount_contiguous):
        return (low + 1, high +1)
    return (low +1, high)

def contiguous(lst: List[int], target):
    index_low_inc = 0
    index_high_exc = min_amount_contiguous
    while index_high_exc < len(lst):
        excerpt: List[int] = lst[index_low_inc:index_high_exc]
        summation = sum(excerpt)
        if target == summation:
            return sorted(excerpt)[0] + sorted(excerpt)[-1]
        if target < summation:
            (index_low_inc, index_high_exc) = shrink(index_low_inc, index_high_exc)
        else:
            (index_low_inc, index_high_exc) = grow(index_low_inc, index_high_exc)

    return "not found"


strings: List[str] = open('input.txt', 'r').readlines()
ints: List[int] = [int(x) for x in strings]
erroneous: int = check(ints)
print(contiguous(ints, erroneous))
