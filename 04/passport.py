from typing import List

mandatory: List[int] = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def valid(passport: str):
    for x in mandatory:
        if not x in passport:
            return False
    return True


lines: List[str] = open('input.txt', 'r').read().split('\n\n')
print(sum(map(valid,lines)))
