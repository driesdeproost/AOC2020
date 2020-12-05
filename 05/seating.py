from typing import List

seatsPerRow: int = 8


def customToBin(s: str) -> str:
    return s.replace("B","1").replace("R","1").replace("F","0").replace("L","0")


def binToDec(s: str) -> int:
    return int(s, 2)


def value(s: str) -> int:
    FB: str = s[:7]
    LR: str = s[-3:]
    return binToDec(customToBin(FB))*seatsPerRow + binToDec(customToBin(LR))


lines: List[str] = [line.rstrip() for line in open('input.txt')]
print(max(map(value, lines)))
