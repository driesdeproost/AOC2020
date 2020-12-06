from typing import List

groups: List[str] = open('input.txt', 'r').read().split('\n\n')
groupLetters: List[str] = [s.replace("\n","").replace(" ","") for s in groups]
groupSets: List[set] = [set(s) for s in groupLetters]
counts: List[int] = [len(set) for set in groupSets]
print(sum(counts))