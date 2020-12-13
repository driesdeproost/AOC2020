from typing import List, Dict

directionsVectors: Dict[str, tuple] = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}
directions: List[str] = list(directionsVectors.keys())
translations: List[str] = ["F"] + directions
rotations: List[str] = ["L","R"]
startDirection = "E"


def rotate(currentDir: str, rotDir: str, angle: int) -> str:
    sign: int = -1 if rotDir == "L" else 1
    shift = (sign * (angle/90))
    return directions[int((directions.index(currentDir) + shift) % len(directions))]


def translate(pos: tuple, dir: str, amount: int):
    vector: tuple = directionsVectors.get(dir)
    return pos[0] + amount * vector[0], pos[1] + amount * vector[1]


def run(directives: List[tuple]) -> int:
    dir = startDirection
    x = 0
    y = 0
    for (i, j) in directives:
        if i in rotations:
            dir = rotate(dir, i, j)
        elif i in translations:
            (x, y) = translate((x,y), i.replace("F", dir), j)
    return x + y


strings: List[str] = open('input.txt', 'r').readlines()
directives: List[tuple] = [(x[0],int(x[1:])) for x in strings]
print(run(directives))