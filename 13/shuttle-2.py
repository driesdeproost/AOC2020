from typing import List
# blatantly stolen from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python
# Python 3.6
from functools import reduce


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

# end thievery


file = open('input.txt', 'r')
now: int = int(file.readline())
strings: List[str] = file.readline().split(",")
withIndices = [f for f in filter(lambda x: x[0] != "x", [(strings[x].replace("\n", ""), x) for x in range(len(strings))])]
n: List[int] = [int(x) for (x,y) in withIndices]
a: List[int] = [(int(xx)-yy) % int(xx) for (xx,yy) in withIndices]
print(chinese_remainder(n,a))

