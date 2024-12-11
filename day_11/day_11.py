import math
from functools import cache

stones = open('input.txt').read().split()
blinks = 75

@cache
def solve(stone, depth):
    if depth == 0:
        return 1
    if stone == 0:
        return solve(1, depth-1)
    z = math.floor(math.log10(stone)) + 1
    if z % 2 == 1:
        return solve(stone * 2024, depth-1)

    l = solve(stone // 10 ** (z // 2), depth-1)
    r = solve(stone % 10 ** (z // 2), depth-1)
    return l + r

ans = 0
for stone in stones:
    ans += solve(int(stone), blinks)
print(ans)
print(solve.cache_info())