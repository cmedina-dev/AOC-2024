schematics = [line.split('\n') for line in open("input.txt").read().split('\n\n')]
locks = []
keys = []
for schema in schematics:
    lock = [-1,-1,-1,-1,-1]
    key = [-1,-1,-1,-1,-1]
    is_lock = False
    if schema[0][0] == '#': is_lock = True
    else: is_lock = False
    for height in schema:
        for i in range(len(height)):
            if height[i] == '#':
                if is_lock: lock[i] += 1
                else: key[i] += 1
    if is_lock: locks.append(lock)
    else: keys.append(key)

ans = 0
for lock in locks:
    for key in keys:
        is_valid = True
        for i in range(len(lock)):
            if lock[i] + key[i] > 5:
                is_valid = False
                break
        if is_valid: ans += 1
print(ans)