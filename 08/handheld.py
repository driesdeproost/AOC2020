from typing import List

# returns tuple of next index and acc
def executeLine(index: int, acc: int, program: List[tuple]) -> tuple:
    (op, arg) = program[index]
    if op == "nop":
        return (index+1, acc)
    if op == "acc":
        return (index+1, acc+arg)
    if op == "jmp":
        return (index+arg, acc)

def runProgram(program: List[tuple]) -> tuple:
    index = 0
    acc = 0
    processedIndices = []
    breakk = False
    while(not breakk):
        if index in processedIndices:
            return (acc, "loop")
        processedIndices.append(index)
        (index, acc) = executeLine(index,acc,program)
    return (acc, "finished")



groups: List[str] = open('input.txt', 'r').readlines()
program: List[tuple] = [(op, int(arg.replace("\n", ""))) for (op, arg) in [a.split(" ") for a in groups]]
(result, status) = runProgram(program)
print(result)


