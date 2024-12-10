import numpy as np

t_map = np.array([list(e) for e in open('input.txt').read().split('\n')], dtype=int)
trailheads = np.argwhere(t_map == 0)


def seek(trail, tmap, visited, p2=False):
    vec = [(1,0), (-1,0), (0,1), (0,-1)]
    t_val = tmap[trail[0], trail[1]]
    viz = np.array(tmap.copy(), dtype=str)
    viz[trail[0], trail[1]] = '#'
    score = 0
    if t_val == 9:
        if p2: return 1
        else:
            if (trail[0], trail[1]) not in visited:
                visited.add((trail[0], trail[1]))
                return 1
            return 0
    for v in vec:
        check = trail + v
        if 0 <= check[0] < len(tmap) and 0 <= check[1] < len(tmap[0]):
            if tmap[check[0], check[1]] != t_val + 1:
                continue
            score += seek(check, tmap, visited, p2)
    return score

def part_two():
    ans = 0
    for t in trailheads:
        visited = set()
        score = seek(t, t_map.copy(), visited, p2=True)
        ans += score
    print(ans)
part_two()

def part_one():
    ans = 0
    for t in trailheads:
        visited = set()
        score = seek(t, t_map.copy(), visited)
        ans += score
    print(ans)