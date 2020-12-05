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
seats: List[int] = [x for x in range(1024)]
for code in lines:
    seats.remove(value(code))
print(seats)
if (len(seats) == 1):
    print(seats[0])
else:
    for x in range(1,len(seats)-1):
        if seats[x] - seats[x-1] > 1:
            print(seats[x])
            break