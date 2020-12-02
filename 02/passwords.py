from typing import List, Iterator


class PasswordRestriction:
  text: str = ""
  min: int = 0
  max: int = 0


class PasswordCheck:
    restriction: PasswordRestriction = None
    password: str


def parseLine(lst: List[str]) -> PasswordCheck:
    check = PasswordCheck()
    restr = PasswordRestriction()
    minmax = lst[0].split("-")
    restr.min = int(minmax[0])
    restr.max = int(minmax[1])
    restr.text = lst[1][:-1]
    check.restriction = restr
    check.password = lst[2]
    return check


def valid(check: PasswordCheck) -> bool:
    count: int = check.password.count(check.restriction.text)
    return check.restriction.max >= count >= check.restriction.min


lines: List[str]
with open("input.txt") as f:
    lines = f.read().splitlines()

splitBySpace: List[List[str]] = [x.split(" ") for x in lines]
parsed: Iterator[PasswordCheck] = map(parseLine, splitBySpace)
ok: Iterator[PasswordCheck] = filter(valid, parsed)
print(len(list(ok)))
