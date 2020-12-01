import bisect
import operator
from functools import reduce
from typing import List

target: int = 2020
lines: List[int] = list(map(int, open('input.txt', 'r').readlines()))


def two_elements_summing_to(sorted_list : List[int], total: int) -> List[int]:
    index_low: int = 0
    index_high: int = len(sorted_list) - 1

    for x in range(index_high - 1):
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


def three_elements_summing_to(sorted_list : List[int], total: int) -> List[int]:
    cutoff: int = total/3
    left: List[int] = sorted_list[:bisect.bisect_left(sorted_list, cutoff)]
    for x in left:
        right: List[int] = sorted_list[bisect.bisect_left(sorted_list, x):]
        right.remove(x) # there is probably a better way to do this
        result: List[int] = two_elements_summing_to(right, total - x)
        if result:
            result.append(x)
            return result
    raise Exception("no solution found")



def n_elements_summing_to(sorted_list : List[int], total: int, number_elements: int) -> List[int]:
    raise Exception("This is left as an exercise to the reader")


sorted_input: List[int] = sorted(lines)
result = three_elements_summing_to(sorted_input, target)
print(result)
print(reduce(operator.mul, result))


