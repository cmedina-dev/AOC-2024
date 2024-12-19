from numba import jit

file = open('input.txt')
file.readline()
file.readline()
file.readline()
file.readline()
instructions = list(reversed(file.readline().split(': ')[1].split(',')))

sums = []
i = len(instructions) - 1
ptr = 0
while i >= 0:
    print(i, instructions[ptr])
    sums.append(int(instructions[ptr]) * (8 ** (i + 1)))
    i -= 1
    ptr += 1
print(sum(sums))