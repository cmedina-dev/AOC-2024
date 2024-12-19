from functools import cache

file = open('input.txt', 'r')
patterns = [item.strip(' ') for item in list(sorted(file.readline().strip().split(','), key=len, reverse=True))]
file.readline()
designs = [item.strip() for item in file.readlines()]

@cache
def search(design):
    count = 0
    if design in patterns: count = 1
    for pattern in patterns:
        if design[:len(pattern)] == pattern:
            count += search(design[len(pattern):])
    return count

ans = 0
for design in designs:
    ans += search(design)
print(ans)