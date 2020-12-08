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
            return (-1, "loop")
        if index == len(program):
            return (acc, "finished")
        processedIndices.append(index)
        (index, acc) = executeLine(index,acc,program)

def nopJumpIndices(program: List[tuple]) -> List[int]:
    indices = []
    for index in range(len(program)):
        (op, arg) = program[index]
        if op == "jmp" or op == "nop":
            indices.append(index)
    return indices

def swapInstruction(op: str):
    if op == "nop":
        return "jmp"
    if op == "jmp":
        return "nop"

def programWithSwappedInstruction(program: List[tuple], index: int) -> List[tuple]:
    (op, arg) = program[index]
    program[index] = (swapInstruction(op),arg)
    return program

def tryAll(program: List[tuple]):
    for index in nopJumpIndices(program):
        (result, status) = runProgram(programWithSwappedInstruction(program,index))
        program = programWithSwappedInstruction(program, index)
        if status == "finished":
            return result
    return "not found"



groups: List[str] = open('input.txt', 'r').readlines()
program: List[tuple] = [(op, int(arg.replace("\n", ""))) for (op, arg) in [a.split(" ") for a in groups]]
(result, status) = runProgram(program)
print(tryAll(program))


