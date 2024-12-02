import sys
import itertools

sys.stdin = open('input.txt')
data = sys.stdin.read().splitlines()
safes = 0

def check_safe(ins):
    i = 1
    safe = True
    increasing = False
    series = [int(ins[0])]
    if int(ins[0]) < int(ins[1]):
        increasing = True
    while i < len(ins):
        if increasing and int(ins[i]) < int(series[-1]):
            safe = False
            break
        elif not increasing and int(ins[i]) > int(series[-1]):
            safe = False
            break
        elif abs(int(ins[i]) - int(series[-1])) > 3:
            safe = False
            break
        elif abs(int(ins[i]) - int(series[-1])) < 1:
            safe = False
            break
        elif int(ins[i]) == int(series[-1]):
            safe = False
            break
        else:
            series.append(int(ins[i]))
        i += 1
    return safe


for line in data:
    ins = [int(i) for i in line.split()]
    safe = False
    warn = False
    increasing = ins[0] < ins[1]
    for combination in itertools.combinations(ins, len(ins)-1):
        safe = check_safe(combination)
        if safe:
            break
    if safe:
        safes += 1
print(safes)