import numpy as np
f = open('input.txt').readlines()
m = np.array([list(line.strip()) for line in f])

def sim(mp, p2=False):
    vec = np.array([(-1, 0), (0, 1), (1, 0), (0, -1)])
    dirs = ['^','>','v','<']
    cols, rows = mp.shape
    locs = set()
    pos = np.array(np.where(mp == '^')).flatten()
    d_ptr = 0
    while 0 <= pos[1] <= cols and 0 <= pos[0] <= rows:
        x = pos + vec[d_ptr]
        if x[0] >= rows or x[1] >= cols:
            locs.add((int(pos[0]), int(pos[1])))
            break
        if mp[x[0], x[1]] == '#':
            d_ptr += 1
            if d_ptr >= len(vec):
                d_ptr = 0
        else:
            # We store the unit vector to help with cycle detection.
            # If we've traversed a node in the same direction before,
            # we are guaranteed to be in a cycle and can terminate early.
            loc = (int(pos[0]), int(pos[1]), d_ptr)
            if loc in locs:
                return True
            locs.add(loc)
            pos += vec[d_ptr]
        mp[pos[0], pos[1]] = dirs[d_ptr]
    if p2:
        return len(set(locs))
    else:
        return False

def part_one():
    sim(m)

def part_two():
    cycles = 0
    map_count = 1
    for i in range(len(m)):
        for j in range(len(m[i])):
            # Skip invalid maps
            if m[i][j] == '#' or m[i][j] == '^': continue
            m_ = m.copy()
            m_[i][j] = '#'
            is_cycle = sim(m_)
            if is_cycle:
                cycles += 1
                print(f'Map {map_count}: Cycle found, now at {cycles} cycles.')
            else:
                print(f'Map {map_count}: Edge reached.')
            map_count += 1
    print(cycles)
part_two()