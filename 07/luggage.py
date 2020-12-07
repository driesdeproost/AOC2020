import re
from typing import List

myBag: str = "shiny gold"

# (outerbag, {innerbag, amount})
def toTuple(s: str) -> (str, {str, int}):
    s: str = re.sub(" bag(s)?(\.\n)?","",s)
    (name, content) = s.split(" contain ")
    content: List[str] = content.split(", ")
    return name, {y: int(x) for (x,y) in [c.split(" ",1) for c in filter(lambda x: "no other" not in x, content)]}

def heldBy(bag: str, rules: dict) -> List[str]:
    return [x for x in rules.keys() if bag in rules.get(x).keys()]

def heldByIter(bag: str, rules: dict):
    checked: List[str] = []
    toCheck: List[str] = [bag]
    while len(toCheck) > 0:
        checking: str = toCheck.pop()
        result: List[str] = heldBy(checking, rules)
        for x in result:
            if x not in checked:
                toCheck.append(x)
        checked.append(checking)
    checked.remove(bag)
    return checked

groups: List[str] = open('input.txt', 'r').readlines()
a = [toTuple(s) for s in groups]
rules = {x[0]: x[1] for x in a} # as dict
print(len(heldByIter(myBag, rules)))
