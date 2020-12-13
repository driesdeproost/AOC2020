from typing import List, Dict

directionsVectors: Dict[str, tuple] = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}
directions: List[str] = list(directionsVectors.keys())
translations: List[str] = ["F"]
rotations: List[str] = ["L","R"]
startDirection = "E"

# Clockwise: 0 -1
#            1  0
#
def rotate(x: int, y: int, rotDir: str, angle: int) -> tuple:
    for i in range(int(angle/90)):
        if (rotDir == "R"):
            (x, y) = rotateOnceCW((x, y))
        else:
            (x, y) = rotateOnceCCW((x, y))
    return (x ,y)

def rotateOnceCW(pos: tuple):
    return pos[1], -pos[0]
def rotateOnceCCW(pos: tuple):
    return -pos[1], pos[0]

def translate(pos: tuple, dir: str, amount: int):
    vector: tuple = directionsVectors.get(dir)
    return pos[0] + amount * vector[0], pos[1] + amount * vector[1]


def run(directives: List[tuple]) -> int:
    dir = startDirection
    xBoat = 0
    yBoat = 0
    xWayPointRelative = -1
    yWayPointRelative = 10
    for (i, j) in directives:
        if i in translations:
            (xBoat, yBoat) = (xBoat+j*xWayPointRelative, yBoat+j*yWayPointRelative)
        elif i in rotations:
            xWayPointRelative, yWayPointRelative = rotate(xWayPointRelative, yWayPointRelative, i, j)
        elif i in directions:
            (xWayPointRelative, yWayPointRelative) = translate((xWayPointRelative,yWayPointRelative), i, j)
    return abs(xBoat) + abs(yBoat)


strings: List[str] = open('input.txt', 'r').readlines()
directives: List[tuple] = [(x[0],int(x[1:])) for x in strings]
print(run(directives))