from typing import List


def wait_time(now: int, id: int):
    return id - (now % id)

file = open('input.txt', 'r')
now: int = int(file.readline())
strings: List[str] = file.readline().split(",")
a = [(int(x),wait_time(now, int(x))) for x in filter(lambda x: x != "x",strings)]
a.sort(key=lambda x: x[1])
print(a[0][0]*a[0][1])
