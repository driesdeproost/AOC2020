import re
from typing import List, Callable


class Constraint:
    name: str
    pred: Callable[[str], bool]

    def __init__(self, name, pred):
        self.name = name
        self.pred = pred


def hgt(s: str) -> bool:
    unit: str = s[-2:]
    val: str = s[:-2]
    if unit == "cm":
        return 150 <= int(val) <= 193
    if unit == "in":
        return 59 <= int(val) <= 76
    return False


hcl_re = re.compile(r'\A#\w{6}\Z')
pid_re = re.compile(r'\A\d{9}\Z')

byrCon = Constraint("byr", lambda s: 1920 <= int(s) <= 2002)
iyrCon = Constraint("iyr", lambda s: 2010 <= int(s) <= 2020)
eyrCon = Constraint("eyr", lambda s: 2020 <= int(s) <= 2030)
hgtCon = Constraint("hgt", hgt)
hclCon = Constraint("hcl", lambda s: re.match(hcl_re, s))
eclCon = Constraint("ecl", lambda s: s in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
pidCon = Constraint("pid", lambda s: re.match(pid_re, s))

mandatory: List[Constraint] = {byrCon, iyrCon, eyrCon, hgtCon, hclCon, eclCon, pidCon}


def debug(key: str, d: dict, valid: bool) -> None:
    if valid:
        print(key + " valid: " + d.get(key))
    else:
        print(key + " not valid: " + d.get(key))


def valid(passport: dict) -> bool:
    print("---")
    for x in mandatory:
        if x.name not in passport.keys():
            print(x.name + " not found in " + str.join(",", passport.keys()))
            return False
        if not x.pred(passport.get(x.name)):
            debug(x.name, passport, False)
            return False
        debug(x.name, passport, True)
    return True


def notEmpty(s: str) -> bool:
    return s != ''


def toDict(a: str) -> dict:
    dictionary: dict = {}
    concatenated: str = a.replace("\n", " ")
    splitBySpace: List[str] = filter(notEmpty, concatenated.split(" "))
    for elem in splitBySpace:
        entry = elem.split(":")
        dictionary[entry[0]] = entry[1]
    return dictionary


lines: List[str] = open('input.txt', 'r').read().split('\n\n')
props: dict = map(toDict, lines)
count: int = sum(map(valid, props))
print("---")
print("amount of valid passports: " + str(count))
