from functools import reduce
from typing import List
#assuming only steps 1 and 3
## 11 = 2      = 1+1  = 1+1                 # 456 46
## 111 = 4     = 1+3  = 1+2+1               # 4567 457 467 47
## 1111 = 7    = 1+6  = 1+3+3               # 45678 4568 4578 4678 478 468 458
## 11111 = 11  = 1+10 = 1+4+4+2             # 456789 45679 45689 45789 46789 4569 4589 4789 4679 479 469
## 111111 = 24        = 1+5+10+7+1          # 3456789 345679 345689 345789 346789 356789 + (5 choose 2) + ((5 choose 3) -3 consec) + 1

weight: dict = {0:1,1:1,2:2,3:4,4:7,5:11,6:24} #apparently 4 was already enough

strings: List[str] = open('input.txt', 'r').readlines()
ints: List[int] = sorted([int(x) for x in strings])
diffs: List[int] = [ints[x+1] - ints[x] for x in range(len(ints)-1)]
diffs = [ints[0]] + diffs + [3]
strdiffs = [str(x) for x in diffs]
joined: str = ''.join(strdiffs)
segments: List[int] = [len(x) for x in joined.split("3")]
print(reduce((lambda x, y: x * y), [weight.get(x) for x in segments]))

