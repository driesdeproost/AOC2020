import copy
from itertools import product
from typing import List

floor : str = "."
empty: str = "L"
occupied: str = "#"

def nextSeatValue(x: int, y: int, grid:List[List[str]]) -> str:
    current: str = grid[x][y]
    if current == floor:
        return floor
    n = neighbours(x, y, grid)
    if current == empty and occupyCount(n, grid) == 0:
        return occupied
    if current == occupied and occupyCount(n, grid) >= 4:
        return empty
    return current

def occupyCount(t: List[tuple], grid:List[List[str]]) -> int:
    acc: int = 0
    for (x, y) in t:
        if grid[x][y] == occupied:
            acc+=1
    return acc

def neighbours(xOG , yOG: int, grid:List[List[str]]) -> List[tuple]:
    a: List[tuple] = []
    for (x, y) in product(range(xOG-1,xOG+2),range(yOG-1,yOG+2)):
        if validNeighbour(x, y, xOG, yOG, len(grid)-1, len(grid[0])-1):
            a.append((x,y))
    return a

def validNeighbour(x: int, y: int, xOG: int, yOG: int, xMax: int, yMax: int) -> bool:
    if x == xOG and y == yOG:
        return False
    if x < 0 or y < 0 or x > xMax or y > yMax:
        return False
    return True

def yeehawsh(anything) -> int:
    return hash(str(anything))

def advanceGrid(grid:List[List[str]]) -> List[List[str]]:
    grid2 = copy.deepcopy(grid)
    for (x, y) in product(range(len(grid)), range(len(grid[0]))):
        grid2[x][y] = nextSeatValue(x, y, grid)
    return grid2

def advGridUntilEquilibirium(grid:List[List[str]]):
    h = 0
    while yeehawsh(grid) != h:
        h = yeehawsh(grid)
        grid = advanceGrid(grid)
    return grid

strings: List[str] = [line.rstrip() for line in open('input.txt')]
grid = [[x for x in s] for s in strings]
print(sum([s.count(occupied) for s in [x for x in advGridUntilEquilibirium(grid)]]))

