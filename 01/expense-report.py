from typing import List

target: int = 2020
lines: List[int] = list(map(int, open('input.txt', 'r').readlines()))
sorted_input: List[int] = sorted(lines)


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

    raise Exception("no solution found")


result = two_elements_summing_to(sorted_input, target)
print(result[0] * result[1])


